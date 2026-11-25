# -*- coding: utf-8 -*-
import json, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, "..", "data", "self_rows.json"), encoding="utf-8"))
R = json.load(open(os.path.join(HERE, "..", "results", "pattern_results.json"), encoding="utf-8"))
groups = collections.OrderedDict()
for r in rows:
    if "行キー" in r:
        line = r["行キー"]
    else:
        b = (r["修正前"] or "").strip(); a = (r["修正後"] or "").strip()
        line = b if b and b != "（追加）" else "A:" + a
    if r["出典"].startswith("claude") or r["分類コード"].startswith("L") or r["分類コード"] == "E5":
        k = ("uniq", r["_i"])
    else:
        k = (r["ファイル"], r["日時"], line)
    groups.setdefault(k, []).append(r)
pri = lambda c: (0 if c.startswith("E") else 1 if c.startswith("W") else 2, int(c[1:]) if c[1:].isdigit() else 0)
E4 = {48: "P05", 208: "P05", 67: "P06a", 85: "P06b", 98: "P06c", 110: "P06d", 215: "P06e", 229: "P06f", 194: "P06g"}
W10 = {5: "P26", 27: "P27", 102: "P28", 139: "P29", 221: "P30"}

def pattern(g):
    codes = sorted({x["分類コード"] for x in g}, key=pri); code = codes[0]
    i0 = g[0]["_i"]; msg = " ".join(x["内容"] for x in g)
    for x in g:
        if x["_i"] in E4: return E4[x["_i"]]
    if code == "E1": return "P01"
    if code == "E2": return "P02"
    if code == "E3": return "P04"
    if code == "E4": return E4[i0]
    if code == "E5": return "P07"
    if code == "W1":
        if ("‘int *’, but argument 2 has type ‘int’" in msg) or ("‘double *’, but argument 2 has type ‘double’" in msg): return "P10"
        return "P11"
    if code == "W2": return "P13" if i0 == 199 else "P12"
    if code == "W3":
        if "too many arguments" in msg: return "P15"
        if "‘int *’ argument" in msg: return "P16"
        return "P14"
    if code == "W4": return "P17"
    if code == "W5":
        if "did you mean" in msg or any(t in msg for t in ("uselep", "tiem", "sfancf", "sfcanf", "scnaf")): return "P18"
        return "P19"
    if code == "W6": return "P21"
    if code == "W7": return "P22"
    if code == "W8": return "P23"
    if code == "W9": return "P24" if i0 == 93 else "P25"
    if code == "W10": return W10[i0]
    if i0 == 293: return "P41"
    return {"L1": "P40a", "L2": "P40b", "L3": "P40c", "L4": "P42", "L5": "P43", "L6": "P44", "L7": "P45"}[code]

def rust_class(r):
    if r["rustc_before"][0] == "エラー": return "コンパイルエラー"
    if r["google_before"][0] == "エラー": return "Google設定でエラー"
    run = r.get("run", "")
    if r["same_code"] and run == "正しく動く": return "書けない（そのまま正しく動く）"
    if run.startswith("実行時に停止"): return "実行時に停止"
    return "見逃し（結果が違う）"

mist = []
for k, g in groups.items():
    pid = pattern(g); r = R[pid]
    codes = sorted({x["分類コード"] for x in g}, key=pri)
    m = dict(rows=[x["_i"] for x in g], code=codes[0], pid=pid, pname=r["name"],
             gcc=r["gcc_before"][0], wall=r["gccwall_before"][0], rustc=r["rustc_before"][0], google=r["google_before"][0],
             rclass=rust_class(r), rmsg=(r["rustc_before"][1] or r["google_before"][1] or r.get("run", "")))
    mist.append(m)
json.dump(mist, open(os.path.join(HERE, "..", "results", "mistakes.json"), "w"), ensure_ascii=False, indent=0)
N = len(mist)
C = collections.Counter
print("mistakes", N)
print("gcc(no opt)", C(m["gcc"] for m in mist))
print("gcc -Wall ", C(m["wall"] for m in mist))
print("rustc      ", C(m["rustc"] for m in mist))
print("google     ", C(m["google"] for m in mist))
print("rust class ", C(m["rclass"] for m in mist))
print("pattern use", C(m["pid"] for m in mist))
# gcc がビルドを止めなかったミス
slip = [m for m in mist if m["gcc"] != "エラー"]
print("gcc slipped", len(slip), C(m["rclass"] for m in slip))
stopped = [m for m in mist if m["gcc"] == "エラー"]
print("gcc stopped", len(stopped), C(m["rclass"] for m in stopped))
print("by code:")
for code in sorted({m['code'] for m in mist}):
    s=[m for m in mist if m['code']==code]
    print(code, len(s), C(m['gcc'] for m in s), C(m['rclass'] for m in s))
