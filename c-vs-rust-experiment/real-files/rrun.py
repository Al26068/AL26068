# 実ファイルを Rust に書き直した版に、実際のミスを1つずつ戻してコンパイル・実行する
import json, os, re, subprocess, sys, collections, importlib, glob, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
PRELUDE = '''//! 授業課題を Rust に書き直したもの（実験用）
#![forbid(unsafe_code)]

/// 標準入力から1行読んで、その型として解釈する（scanf の代わり）
#[allow(dead_code)]
fn read_into<T: std::str::FromStr>(v: &mut T) {
    let mut s = String::new();
    let _ = std::io::stdin().read_line(&mut s);
    if let Ok(x) = s.trim().parse() {
        *v = x;
    }
}
'''
GOOGLE = ["-A", "deprecated", "-D", "missing-docs", "-D", "warnings",
          "-A", "clippy::type-complexity", "-A", "clippy::unnecessary-wraps", "-A", "clippy::unusual-byte-groupings"]
BUILD = os.path.join(HERE, "rbuild"); os.makedirs(BUILD, exist_ok=True)
S = {}
for f in sorted(glob.glob(os.path.join(HERE, "specs", "b*.py"))):
    ns = {}
    exec(open(f, encoding="utf-8").read(), ns)
    S.update(ns["S"])

def apply(src, reps, where):
    for a, b in reps:
        n = src.count(a)
        if n != 1:
            raise SystemExit(f"[{where}] '{a[:60]}' は {n} 回見つかった（1回のはず）")
        src = src.replace(a, b)
    return src

def diags(err):
    out = collections.Counter()
    for l in err.splitlines():
        m = re.match(r"^(error|warning)(\[\w+\])?: (.*)", l)
        if m and "aborting" not in l and "generated" not in m.group(3) and "emitted" not in m.group(3):
            out[(m.group(1), m.group(2) or "", re.sub(r"`[^`]*`", "`_`", m.group(3)))] += 1
    return out

def compile_(src, tag, google):
    h = hashlib.md5((src + str(google)).encode()).hexdigest()[:10]
    p = os.path.join(BUILD, f"{tag}_{h}.rs"); exe = p[:-3] + ("_g" if google else "")
    if not os.path.exists(p): open(p, "w").write(src)
    cmd = (["clippy-driver"] if google else ["rustc"]) + ["--edition", "2021"] + (GOOGLE if google else []) + [p, "-o", exe]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    return r.returncode, diags(r.stderr), exe, r.stderr

def judge(b, a):
    rcb, db, _, eb = b; rca, da, _, _ = a
    new = db - da
    if rcb != 0 and rca == 0: return "エラー", first_err(eb)
    if any(k[0] == "error" for k in new): return "エラー", next(" ".join(k[1:]) for k in new if k[0] == "error")
    if any(k[0] == "warning" for k in new): return "警告のみ", next(" ".join(k[1:]) for k in new if k[0] == "warning")
    return "何も出ない", ""

def first_err(e):
    for l in e.splitlines():
        if l.startswith("error") and "aborting" not in l: return l[:140]
    return "error"

def run(exe, stdin):
    try:
        r = subprocess.run([exe], input=stdin, capture_output=True, text=True, timeout=5)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return "timeout", "", ""

if __name__ == "__main__":
    only = sys.argv[1:]
    res = {}
    prev = {}
    rp = os.path.join(HERE, "results", "r_real.json")
    if os.path.exists(rp): prev = json.load(open(rp))
    for f, spec in S.items():
        if only and f not in only: continue
        base = PRELUDE + spec.get("pre", "") + spec["base"]
        tag = re.sub(r"\W", "_", f)
        # base は rustc で通ること
        rb = compile_(base, tag + "_base", False)
        if rb[0] != 0:
            print("BASE FAIL", f); print(rb[3][:3000]); sys.exit(1)
        for gid, m in spec["m"].items():
            where = f"{f} #{gid}"
            after = apply(base, m.get("ctx", []), where + " ctx")
            stdin = m.get("stdin", spec.get("stdin", "5\n3\n4\n2\n1\n6\n7\n8\n9\n10\n" * 3))
            if m.get("bug") is None:
                if m.get("exclude"):
                    res[str(gid)] = dict(file=f, rustc="", google="", run="除外", why=m.get("why", ""), rmsg="")
                    continue
                ra = compile_(after, tag + f"_{gid}a", False)
                if ra[0] != 0: print("AFTER FAIL", where); print(ra[3][:2000]); sys.exit(1)
                res[str(gid)] = dict(file=f, rustc="何も出ない", google="何も出ない", run="書けない", why=m.get("why", ""), rmsg="")
                continue
            before = apply(after, m["bug"], where + " bug")
            ra, rbf = compile_(after, tag + f"_{gid}a", False), compile_(before, tag + f"_{gid}b", False)
            if ra[0] != 0: print("AFTER FAIL", where); print(ra[3][:2000]); sys.exit(1)
            ga, gb = compile_(after, tag + f"_{gid}a", True), compile_(before, tag + f"_{gid}b", True)
            r1 = judge(rbf, ra); r2 = judge(gb, ga)
            if r2[0] == "警告のみ": r2 = ("エラー", r2[1])
            runres = ""
            if rbf[0] == 0:
                ob = run(rbf[2], stdin); oa = run(ra[2], stdin)
                if ob[0] == "timeout": runres = "終わらない"
                elif ob[0] != 0 and "panicked" in ob[2]: runres = "実行時に停止: " + next((l for l in ob[2].splitlines() if "panicked" in l or "attempt" in l or "index out" in l), "")[:120]
                elif ob[1] == oa[1]: runres = "同じ結果"
                else: runres = "結果が違う"
            res[str(gid)] = dict(file=f, rustc=r1[0], google=r2[0], run=runres, rmsg=(r1[1] or r2[1])[:160], why=m.get("why", ""))
    prev.update(res)
    json.dump(prev, open(rp, "w"), ensure_ascii=False, indent=0)
    for g, r in res.items(): print(g, r["file"], r["rustc"], r["google"], r["run"], "|", r["rmsg"][:90])
