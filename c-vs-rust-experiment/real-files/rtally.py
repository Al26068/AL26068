# 実ファイルでの実験結果をまとめる
import json, collections
T = json.load(open("targets.json"))
C = {o["gid"]: o for o in json.load(open("results/c_real.json"))}
CT = {int(k): v for k, v in json.load(open("results/c_tail.json")).items()}
R = json.load(open("results/r_real.json"))
R["258"] = dict(file="pro1/ex3/Challenge3-Kaguya.c", rustc="何も出ない", google="何も出ない", run="書けない", rmsg="",
                why="for の中で変数を宣言するのは Rust では普通の書き方なので、この規則違反は起きない")
rows = []
for t in T:
    g = t["gid"]; r = R[str(g)]
    if r["run"] == "除外":
        rows.append(dict(gid=g, nos=t["nos"], file=t["file"], code=t["code"], excluded=True, why=r["why"])); continue
    if g in CT: cg, cw = CT[g]
    elif g == 258: cg, cw = "エラー", "エラー"   # 学校の古い gcc（C89）でのエラー。今の gcc では通る
    else: cg, cw = C[g]["c_gcc"], C[g]["c_wall"]
    if r["rustc"] == "エラー": cls = "コンパイルエラー"
    elif r["google"] == "エラー": cls = "Google設定でエラー"
    elif r["run"] == "書けない": cls = "書けない（そのまま正しく動く）"
    elif r["run"].startswith("実行時に停止"): cls = "実行時に停止"
    elif r["run"] == "同じ結果" and not t["code"].startswith("L"): cls = "書けない（そのまま正しく動く）"
    else: cls = "見逃し（結果が違う）"
    rows.append(dict(gid=g, nos=t["nos"], file=t["file"], code=t["code"], excluded=False, c_gcc=cg, c_wall=cw,
                     rustc=r["rustc"], google=r["google"], run=r["run"], rclass=cls, rmsg=r.get("rmsg", ""), why=r.get("why", "")))
json.dump(rows, open("results/real_results.json", "w"), ensure_ascii=False, indent=0)
use = [x for x in rows if not x["excluded"]]
Cn = collections.Counter
print("対象", len(rows), "除外", len(rows) - len(use), "→", len(use))
print("gcc  ", Cn(x["c_gcc"] for x in use)); print("wall ", Cn(x["c_wall"] for x in use))
print("rustc", Cn(x["rustc"] for x in use)); print("google", Cn(x["google"] for x in use))
print("class", Cn(x["rclass"] for x in use))
slip = [x for x in use if x["c_gcc"] != "エラー"]
print("gccを通り抜けた", len(slip), Cn(x["rclass"] for x in slip))
st = [x for x in use if x["c_gcc"] == "エラー"]
print("gccで止まった", len(st), Cn(x["rclass"] for x in st))
rust_left = sum(1 for x in use if x["rclass"] in ("実行時に停止", "見逃し（結果が違う）"))
print("通り抜け C", len(slip), "→ Rust", rust_left, f"減少 {1 - rust_left / len(slip):.1%}")
prevented = sum(1 for x in use if x["rclass"] in ("コンパイルエラー", "Google設定でエラー", "書けない（そのまま正しく動く）"))
print("コンパイル時に防げた: C", len(st), f"({len(st)/len(use):.0%})", "Rust", prevented, f"({prevented/len(use):.0%})",
      "止まった", sum(1 for x in use if x["rclass"] in ("コンパイルエラー","Google設定でエラー")))
for code in sorted({x["code"] for x in use}, key=lambda c: (c[0] != "E", c[0] != "W", int(c[1:]))):
    s = [x for x in use if x["code"] == code]
    print(code, len(s), dict(Cn(x["c_gcc"] for x in s)), dict(Cn(x["rclass"] for x in s)))
print("Google だけで止まったもの:", [(x["gid"], x["code"], x["rmsg"][:60]) for x in use if x["rclass"] == "Google設定でエラー"])
