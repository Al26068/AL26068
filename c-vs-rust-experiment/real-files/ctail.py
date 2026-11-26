# 版が残っていなかった3件は、最終版の C に当時のミスを戻して gcc に通す
import json, subprocess, os
M = json.load(open("realmap_sel.json")); T = json.load(open("targets.json"))
fixes = {
 209: ("standardvalue[m]= ((score[m] - avg) / standard)*10 + 50;", "standardvalue[m]= ((score[i] - avg) / standard)*10 + 50;"),
 218: ("            if(y<=0){\n                printf(\"おめでとうございますyが0になりました！\");", "            if(x<=0){\n                printf(\"おめでとうございますyが0になりました！\");"),
 223: ("    } else if(year>1911){", "    } else if(year>1988){"),
}
out = {}
for g, (a, b) in fixes.items():
    t = next(x for x in T if x["gid"] == g)
    fin = next(M[str(n)]["final"] for n in t["nos"] if M.get(str(n), {}).get("final"))
    src = open("c_versions/" + fin, errors="ignore").read()
    assert src.count(a) == 1, (g, src.count(a))
    open("/tmp/ct.c", "w").write(src.replace(a, b))
    res = []
    for flags in ([], ["-Wall"]):
        r = subprocess.run(["gcc"] + flags + ["-I", "inc", "/tmp/ct.c", "-o", "/tmp/ct", "-lm"], capture_output=True, text=True)
        line = src[:src.index(a)].count("\n") + 1
        at = [l for l in r.stderr.splitlines() if f":{line}:" in l or f":{line+1}:" in l]
        res.append("エラー" if r.returncode else ("警告のみ" if any("warning" in l for l in at) else "何も出ない"))
    out[g] = res
print(out)
json.dump(out, open("results/c_tail.json", "w"))
