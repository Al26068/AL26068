# 実ファイル（編集履歴に残っているミスあり版）を gcc に通して、ミスの行に何が出るかを記録する
import json, os, re, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(HERE, "realmap_sel.json")))
T = json.load(open(os.path.join(HERE, "targets.json")))
cache = {}
def build(vf, flags):
    k = (vf, tuple(flags))
    if k in cache: return cache[k]
    src = os.path.join(HERE, "c_versions", vf)
    r = subprocess.run(["gcc"] + flags + ["-I", os.path.join(HERE, "inc"), src, "-o", "/tmp/cm.out", "-lm"],
                       capture_output=True, text=True, timeout=60)
    diags = []
    for l in r.stderr.splitlines():
        m = re.match(r".*?:(\d+):\d+: (error|warning): (.*)", l)
        if m: diags.append((int(m.group(1)), m.group(2), m.group(3)))
        m2 = re.search(r"undefined reference to `([^']+)'", l)
        if m2: diags.append((None, "link", m2.group(1)))
    cache[k] = (r.returncode, diags)
    return cache[k]
def judge(vf, line, flags):
    rc, diags = build(vf, flags)
    txt = open(os.path.join(HERE, "c_versions", vf), errors="ignore").read().splitlines()
    ltxt = txt[line - 1] if line and 0 < line <= len(txt) else ""
    at = [d for d in diags if d[0] == line]
    if any(d[1] == "error" for d in at): return "エラー", next(d[2] for d in at if d[1] == "error")
    links = [d for d in diags if d[1] == "link" and re.search(r"\b%s\b" % re.escape(d[2]), ltxt)]
    if links: return "エラー", "リンクエラー: " + links[0][2]
    if any(d[1] == "warning" for d in at): return "警告のみ", next(d[2] for d in at if d[1] == "warning")
    return "何も出ない", ""
SEV = {"エラー": 2, "警告のみ": 1, "何も出ない": 0}
out = []
for t in T:
    res = {}
    for flags, name in (([], "gcc"), (["-Wall"], "wall")):
        best = ("何も出ない", "")
        for n in t["nos"]:
            m = M.get(str(n))
            if not m or not m.get("before"): continue
            j = judge(m["before"], m["line"], flags)
            if SEV[j[0]] > SEV[best[0]]: best = j
        res[name] = best
    out.append({"gid": t["gid"], "nos": t["nos"], "file": t["file"], "code": t["code"], "pid": t["pid"],
                "c_gcc": res["gcc"][0], "c_gcc_msg": res["gcc"][1][:120], "c_wall": res["wall"][0], "c_wall_msg": res["wall"][1][:120],
                "has_version": any(M.get(str(n), {}).get("before") for n in t["nos"])})
json.dump(out, open(os.path.join(HERE, "results", "c_real.json"), "w"), ensure_ascii=False, indent=0)
C = collections.Counter
print(len(out), "no version:", [o["gid"] for o in out if not o["has_version"]])
print("gcc ", C(o["c_gcc"] for o in out if o["has_version"]))
print("wall", C(o["c_wall"] for o in out if o["has_version"]))
old = {}
diff = [(o["gid"], o["code"], old[o["gid"]]["gcc"], o["c_gcc"], o["c_gcc_msg"][:60]) for o in out if o["has_version"] and old[o["gid"]]["gcc"] != o["c_gcc"]]
print("differs from pattern result:", len(diff))
for d in diff: print(d)
