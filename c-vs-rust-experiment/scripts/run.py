# -*- coding: utf-8 -*-
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patterns import P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build")
os.makedirs(OUT, exist_ok=True)
GOOGLE = ["-A", "deprecated", "-D", "missing-docs", "-D", "warnings",
          "-A", "clippy::type-complexity", "-A", "clippy::unnecessary-wraps", "-A", "clippy::unusual-byte-groupings"]


def sh(cmd, stdin=None, timeout=20):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, input=stdin, timeout=timeout)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return "timeout", "", ""


def gcc(src, exe, flags, std):
    cmd = ["gcc"] + (["-std=" + std] if std else []) + flags + [src, "-o", exe, "-lm"]
    rc, _, err = sh(cmd)
    errs = [l for l in err.splitlines() if ": error:" in l or "ld returned" in l or "undefined reference" in l]
    warns = [l for l in err.splitlines() if ": warning:" in l]
    if rc != 0:
        return "エラー", (errs or err.splitlines()[-1:])[0]
    if warns:
        return "警告のみ", warns[0]
    return "何も出ない", ""


def rust(src, exe, google):
    cmd = (["clippy-driver"] if google else ["rustc"]) + ["--edition", "2021"] + (GOOGLE if google else []) + [src, "-o", exe]
    rc, _, err = sh(cmd, timeout=60)
    lines = err.splitlines()
    errs = [l for l in lines if l.startswith("error")]
    warns = [l for l in lines if l.startswith("warning") and "generated" not in l]
    if rc != 0:
        e = [l for l in errs if not l.startswith("error: aborting")]
        return "エラー", (e or ["error"])[0]
    if warns:
        return "警告のみ", warns[0]
    return "何も出ない", ""


def short(msg):
    msg = re.sub(r"^/\S+?:\d+:\d+: ", "", msg)
    msg = re.sub(r"\s+", " ", msg)
    return msg[:110]


res = {}
for pid, p in P.items():
    d = os.path.join(OUT, pid)
    os.makedirs(d, exist_ok=True)
    r = {"name": p["name"], "note": p["note"]}
    for side in ("before", "after"):
        cs = os.path.join(d, f"{side}.c"); open(cs, "w").write(p["c_" + side])
        rsrc = os.path.join(d, f"{side}.rs"); open(rsrc, "w").write(p["rs_" + side])
        r[f"gcc_{side}"] = gcc(cs, os.path.join(d, f"{side}_c"), [], p["cstd"])
        r[f"gccwall_{side}"] = gcc(cs, os.path.join(d, f"{side}_c"), ["-Wall"], p["cstd"])
        r[f"rustc_{side}"] = rust(rsrc, os.path.join(d, f"{side}_rs"), False)
        r[f"google_{side}"] = rust(rsrc, os.path.join(d, f"{side}_rsg"), True)
    # 実行（Rust の修正前がコンパイルを通るときだけ）
    r["same_code"] = p["rs_before"] == p["rs_after"]
    if r["rustc_before"][0] != "エラー":
        rc_b, out_b, err_b = sh([os.path.join(d, "before_rs")], stdin=p["stdin"], timeout=5)
        rc_a, out_a, _ = sh([os.path.join(d, "after_rs")], stdin=p["stdin"], timeout=5)
        if rc_b == "timeout":
            r["run"] = "終わらない"
        elif rc_b != 0 and "panicked" in err_b:
            r["run"] = "実行時に停止（panic）: " + short([l for l in err_b.splitlines() if l.strip()][-1] if err_b else "")
            r["panic"] = short(next((l for l in err_b.splitlines() if "panicked" in l or "attempt" in l or "index out" in l), err_b))
        elif out_b == out_a:
            r["run"] = "正しく動く"
        else:
            r["run"] = f"結果が違う（{out_b.strip()[:20]} ≠ 正しくは {out_a.strip()[:20]}）"
    res[pid] = r

json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "pattern_results.json"), "w"), ensure_ascii=False, indent=1)
bad = []
for pid, r in res.items():
    for k in ("gcc_after", "gccwall_after", "rustc_after", "google_after"):
        if r[k][0] != "何も出ない":
            bad.append((pid, k, short(r[k][1])))
    print(f"{pid:5} gcc={r['gcc_before'][0]:5} wall={r['gccwall_before'][0]:5} rustc={r['rustc_before'][0]:5} google={r['google_before'][0]:5} run={r.get('run','-')}  | {short(r['rustc_before'][1] or r['google_before'][1])[:70]}")
print("--- control failures (after should be clean):")
for b in bad:
    print(b)
