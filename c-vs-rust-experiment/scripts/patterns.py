# -*- coding: utf-8 -*-
# 実験用：ミスのパターンごとに「正しいC／ミス入りC／正しいRust／ミス入りRust」を用意する。
# Rust は Google（Android）の方針に合わせる：unsafe 禁止、Google 既定の lint（-D warnings ほか）と clippy で警告0。
# 書き換えルール（固定）
#   R1 int→i32, double→f64。暗黙の型変換はしない（必要なら f64::from で明示）
#   R2 &x（ポインタ渡し）→ &mut x、配列を渡す → スライス &[T]
#   R3 scanf("%d",&x) → read_into::<i32>(&mut x)（%lf なら f64）
#   R4 printf → println!（%d %f → {}）
#   R5 for(初期化;条件;更新){本体} → 初期化; while 条件 { 本体; 更新; }
#   R6 x = x + y → x += y（clippy に合わせる）、宣言と初期化はまとめる
#   R7 #include → use
#   R8 C のカンマ演算子 → タプル式、i++ を式で使う → { let t = i; i += 1; t }

RS_HEAD = "//! 実験用プログラム\n#![forbid(unsafe_code)]\n"
READ = '''
fn read_into<T: std::str::FromStr>(v: &mut T) {
    let mut s = String::new();
    let _ = std::io::stdin().read_line(&mut s);
    if let Ok(x) = s.trim().parse() {
        *v = x;
    }
}
'''


def c(body, pre="", inc="#include <stdio.h>\n"):
    return f"{inc}{pre}int main(void)\n{{\n{body}    return 0;\n}}\n"


def rs(body, pre="", read=False):
    return RS_HEAD + (READ if read else "") + pre + "\nfn main() {\n" + body + "}\n"


P = {}


def add(pid, name, cb, ca, rb, ra, stdin="3\n", cstd=None, note=""):
    P[pid] = dict(name=name, c_before=cb, c_after=ca, rs_before=rb, rs_after=ra, stdin=stdin, cstd=cstd, note=note)


# ---- C でもエラーになるミス ----
add("P01", "宣言していない変数を使う",
    c("    x = 1;\n    printf(\"%d\\n\", x);\n"),
    c("    int x;\n    x = 1;\n    printf(\"%d\\n\", x);\n"),
    rs("    x = 1;\n    println!(\"{x}\");\n"),
    rs("    let x = 1;\n    println!(\"{x}\");\n"))
add("P02", "文法の書き間違い（; 忘れなど）",
    c("    int x = 1;\n    x = x * 2\n    printf(\"%d\\n\", x);\n"),
    c("    int x = 1;\n    x = x * 2;\n    printf(\"%d\\n\", x);\n"),
    rs("    let mut x = 1;\n    x *= 2\n    println!(\"{x}\");\n"),
    rs("    let mut x = 1;\n    x *= 2;\n    println!(\"{x}\");\n"))
add("P04", "同じ変数を2回宣言する",
    c("    int i = 0;\n    int i = 0;\n    printf(\"%d\\n\", i);\n"),
    c("    int i = 0;\n    printf(\"%d\\n\", i);\n"),
    rs("    let i = 0;\n    let i = 0;\n    println!(\"{i}\");\n"),
    rs("    let i = 0;\n    println!(\"{i}\");\n"),
    note="Rust は同じ名前の再宣言（シャドーイング）を許す")
add("P05", "条件の中で == を = にして代入できない式になる",
    c("    int a = 0, b = 0;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    if (a == 0 || b = 0) {\n        printf(\"zero\\n\");\n    }\n"),
    c("    int a = 0, b = 0;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    if (a == 0 || b == 0) {\n        printf(\"zero\\n\");\n    }\n"),
    rs("    let mut a: i32 = 0;\n    let mut b: i32 = 0;\n    read_into::<i32>(&mut a);\n    read_into::<i32>(&mut b);\n    if a == 0 || b = 0 {\n        println!(\"zero\");\n    }\n", read=True),
    rs("    let mut a: i32 = 0;\n    let mut b: i32 = 0;\n    read_into::<i32>(&mut a);\n    read_into::<i32>(&mut b);\n    if a == 0 || b == 0 {\n        println!(\"zero\");\n    }\n", read=True),
    stdin="1\n2\n")
add("P06a", "int の配列を文字列で初期化する",
    c("    int a[2] = \"10\";\n    printf(\"%d\\n\", a[0]);\n"),
    c("    int a[2] = {10, 5};\n    printf(\"%d\\n\", a[0]);\n"),
    rs("    let a: [i32; 2] = \"10\";\n    println!(\"{}\", a[0]);\n"),
    rs("    let a: [i32; 2] = [10, 5];\n    println!(\"{}\", a[0]);\n"))
add("P06b", "double に % を使う",
    c("    double pi = 2.5;\n    int i = 3;\n    if (pi % 2 == 0) {\n        printf(\"even\\n\");\n    }\n    printf(\"%f %d\\n\", pi, i);\n"),
    c("    double pi = 2.5;\n    int i = 3;\n    if (i % 2 == 0) {\n        printf(\"even\\n\");\n    }\n    printf(\"%f %d\\n\", pi, i);\n"),
    rs("    let pi = 2.5_f64;\n    let i = 3;\n    if pi % 2 == 0 {\n        println!(\"even\");\n    }\n    println!(\"{pi} {i}\");\n"),
    rs("    let pi = 2.5_f64;\n    let i = 3;\n    if i % 2 == 0 {\n        println!(\"even\");\n    }\n    println!(\"{pi} {i}\");\n"))
add("P06c", "配列そのものに代入する",
    c("    int s[3] = {0, 0, 0};\n    s = 1;\n    printf(\"%d\\n\", s[0]);\n"),
    c("    int s[3] = {0, 0, 0};\n    s[0] = 1;\n    printf(\"%d\\n\", s[0]);\n"),
    rs("    let mut s = [0; 3];\n    s = 1;\n    println!(\"{}\", s[0]);\n"),
    rs("    let mut s = [0; 3];\n    s[0] = 1;\n    println!(\"{}\", s[0]);\n"))
add("P06d", "関数に渡す引数が多すぎる",
    c("    printf(\"%d\\n\", twice(1, 2));\n", pre="int twice(int a)\n{\n    return a * 2;\n}\n"),
    c("    printf(\"%d\\n\", twice(1));\n", pre="int twice(int a)\n{\n    return a * 2;\n}\n"),
    rs("    println!(\"{}\", twice(1, 2));\n", pre="\nfn twice(a: i32) -> i32 {\n    a * 2\n}\n"),
    rs("    println!(\"{}\", twice(1));\n", pre="\nfn twice(a: i32) -> i32 {\n    a * 2\n}\n"))
AVG_C = "double average(int a[], int n)\n{\n    int i, s = 0;\n    for (i = 0; i < n; i++) {\n        s = s + a[i];\n    }\n    return (double)s / n;\n}\n"
AVG_R = "\nfn average(a: &[i32]) -> f64 {\n    let mut s = 0;\n    let mut i = 0;\n    while i < a.len() {\n        s += a[i];\n        i += 1;\n    }\n    f64::from(s) / a.len() as f64\n}\n"
add("P06e", "関数と同じ名前の変数を作って関数が呼べなくなる",
    c("    int score[3] = {1, 2, 3};\n    double average;\n    average = average(score, 3);\n    printf(\"%f\\n\", average);\n", pre=AVG_C),
    c("    int score[3] = {1, 2, 3};\n    double ave;\n    ave = average(score, 3);\n    printf(\"%f\\n\", ave);\n", pre=AVG_C),
    rs("    let score = [1, 2, 3];\n    let average: f64;\n    average = average(&score);\n    println!(\"{average}\");\n", pre=AVG_R),
    rs("    let score = [1, 2, 3];\n    let ave = average(&score);\n    println!(\"{ave}\");\n", pre=AVG_R))
SORT_C = "void sort(int a[], int n)\n{\n    int i, j, t;\n    for (i = 0; i < n; i++) {\n        for (j = 0; j + 1 < n - i; j++) {\n            if (a[j] > a[j + 1]) {\n                t = a[j];\n                a[j] = a[j + 1];\n                a[j + 1] = t;\n            }\n        }\n    }\n}\n"
SORT_R = "\nfn sort(a: &mut [i32]) {\n    a.sort_unstable();\n}\n"
add("P06f", "値を返さない関数の結果を表示しようとする",
    c("    int a[3] = {3, 1, 2};\n    int i = 0;\n    printf(\"a[%d]=%d\\n\", i, sort(a, 3));\n", pre=SORT_C),
    c("    int a[3] = {3, 1, 2};\n    int i = 0;\n    sort(a, 3);\n    printf(\"a[%d]=%d\\n\", i, a[i]);\n", pre=SORT_C),
    rs("    let mut a = [3, 1, 2];\n    let i = 0;\n    println!(\"a[{i}]={}\", sort(&mut a));\n", pre=SORT_R),
    rs("    let mut a = [3, 1, 2];\n    let i = 0;\n    sort(&mut a);\n    println!(\"a[{i}]={}\", a[i]);\n", pre=SORT_R),
    )
add("P06g", "配列の要素への代入を宣言の形で書く",
    c("    int p[2][2] = {{0, 0}, {0, 0}};\n    int p[0][0] = 1;\n    printf(\"%d\\n\", p[0][0]);\n"),
    c("    int p[2][2] = {{0, 0}, {0, 0}};\n    p[0][0] = 1;\n    printf(\"%d\\n\", p[0][0]);\n"),
    rs("    let mut p = [[0; 2]; 2];\n    let p[0][0] = 1;\n    println!(\"{}\", p[0][0]);\n"),
    rs("    let mut p = [[0; 2]; 2];\n    p[0][0] = 1;\n    println!(\"{}\", p[0][0]);\n"))
add("P07", "古いCの規則（for の中で変数宣言）",
    c("    for (int i = 0; i < 3; i++) {\n        printf(\"%d\\n\", i);\n    }\n"),
    c("    int i;\n    for (i = 0; i < 3; i++) {\n        printf(\"%d\\n\", i);\n    }\n"),
    rs("    let mut i = 0;\n    while i < 3 {\n        println!(\"{i}\");\n        i += 1;\n    }\n"),
    rs("    let mut i = 0;\n    while i < 3 {\n        println!(\"{i}\");\n        i += 1;\n    }\n"),
    cstd="gnu89", note="学校の古いgccに合わせて -std=gnu89 で測る。Rust にはこの規則がない")

# ---- C では警告だけ／何も出ないミス ----
add("P10", "scanf の & 忘れ",
    c("    int x = 0;\n    scanf(\"%d\", x);\n    printf(\"%d\\n\", x);\n"),
    c("    int x = 0;\n    scanf(\"%d\", &x);\n    printf(\"%d\\n\", x);\n"),
    rs("    let mut x: i32 = 0;\n    read_into::<i32>(x);\n    println!(\"{x}\");\n", read=True),
    rs("    let mut x: i32 = 0;\n    read_into::<i32>(&mut x);\n    println!(\"{x}\");\n", read=True))
add("P11", "scanf の書式と変数の型が違う",
    c("    int n = 0;\n    scanf(\"%lf\", &n);\n    printf(\"%d\\n\", n);\n"),
    c("    double n = 0;\n    scanf(\"%lf\", &n);\n    printf(\"%f\\n\", n);\n"),
    rs("    let mut n: i32 = 0;\n    read_into::<f64>(&mut n);\n    println!(\"{n}\");\n", read=True),
    rs("    let mut n: f64 = 0.0;\n    read_into::<f64>(&mut n);\n    println!(\"{n}\");\n", read=True))
add("P12", "printf の書式と値の型が違う",
    c("    double a = 1.5;\n    printf(\"%d\\n\", a);\n"),
    c("    double a = 1.5;\n    printf(\"%f\\n\", a);\n"),
    rs("    let a = 1.5;\n    println!(\"{a}\");\n"),
    rs("    let a = 1.5;\n    println!(\"{a}\");\n"),
    note="Rust の {} は型を書かないので、このミスは書けない")
CIRC_C = "double circ(double r)\n{\n    return 2 * 3.14159 * r;\n}\n"
CIRC_R = "\nfn circ(r: f64) -> f64 {\n    2.0 * std::f64::consts::PI * r\n}\n"
add("P13", "関数を () なしで表示しようとする",
    c("    double r = 1.0;\n    printf(\"%.2f\\n\", circ);\n    printf(\"%f\\n\", r);\n", pre=CIRC_C),
    c("    double r = 1.0;\n    printf(\"%.2f\\n\", circ(r));\n    printf(\"%f\\n\", r);\n", pre=CIRC_C),
    rs("    let r = 1.0;\n    println!(\"{:.2}\", circ);\n    println!(\"{r}\");\n", pre=CIRC_R),
    rs("    let r = 1.0;\n    println!(\"{:.2}\", circ(r));\n    println!(\"{r}\");\n", pre=CIRC_R))
add("P14", "printf の値の書き忘れ",
    c("    int y = 2019;\n    printf(\"%d年は令和元年です。\\n\");\n    printf(\"%d\\n\", y);\n"),
    c("    int y = 2019;\n    printf(\"%d年は令和元年です。\\n\", y);\n    printf(\"%d\\n\", y);\n"),
    rs("    let y = 2019;\n    println!(\"{}年は令和元年です。\");\n    println!(\"{y}\");\n"),
    rs("    let y = 2019;\n    println!(\"{y}年は令和元年です。\");\n    println!(\"{y}\");\n"))
add("P15", "printf の書式の書き忘れ（値が余る）",
    c("    int p = 1;\n    printf(\"p=\\n\", p);\n"),
    c("    int p = 1;\n    printf(\"p=%d\\n\", p);\n"),
    rs("    let p = 1;\n    println!(\"p=\", p);\n"),
    rs("    let p = 1;\n    println!(\"p={p}\");\n"))
add("P16", "scanf の入れ先の書き忘れ",
    c("    int x = 0;\n    scanf(\"%d\");\n    printf(\"%d\\n\", x);\n"),
    c("    int x = 0;\n    scanf(\"%d\", &x);\n    printf(\"%d\\n\", x);\n"),
    rs("    let x: i32 = 0;\n    read_into::<i32>();\n    println!(\"{x}\");\n", read=True),
    rs("    let mut x: i32 = 0;\n    read_into::<i32>(&mut x);\n    println!(\"{x}\");\n", read=True))
add("P17", "if の == を = にする",
    c("    int x = 0;\n    scanf(\"%d\", &x);\n    if (x = 1) {\n        printf(\"one\\n\");\n    }\n"),
    c("    int x = 0;\n    scanf(\"%d\", &x);\n    if (x == 1) {\n        printf(\"one\\n\");\n    }\n"),
    rs("    let mut x: i32 = 0;\n    read_into::<i32>(&mut x);\n    if x = 1 {\n        println!(\"one\");\n    }\n", read=True),
    rs("    let mut x: i32 = 0;\n    read_into::<i32>(&mut x);\n    if x == 1 {\n        println!(\"one\");\n    }\n", read=True))
add("P18", "関数名の打ち間違い（prinft など）",
    c("    prinft(\"hi\\n\");\n"),
    c("    printf(\"hi\\n\");\n"),
    rs("    prinltn!(\"hi\");\n"),
    rs("    println!(\"hi\");\n"))
add("P19", "#include <math.h> 忘れ（pow, abs）",
    c("    double x = 2.0;\n    printf(\"%f\\n\", pow(x, 3.0));\n"),
    c("    double x = 2.0;\n    printf(\"%f\\n\", pow(x, 3.0));\n", inc="#include <stdio.h>\n#include <math.h>\n"),
    rs("    let x = 2.0_f64;\n    println!(\"{}\", x.powf(3.0));\n"),
    rs("    let x = 2.0_f64;\n    println!(\"{}\", x.powf(3.0));\n"),
    note="Rust の powf / abs は数値に付いた機能なので読み込み自体がいらない")
RNG = "\nmod rng {\n    //! 乱数（stdlib.h の代わり）\n    /// 乱数を返す\n    pub fn rand() -> i32 {\n        7\n    }\n    /// 乱数の最大値\n    pub const RAND_MAX: i32 = 32767;\n}\n"
add("P20", "#include <stdlib.h> 忘れ（rand, RAND_MAX）",
    c("    int r;\n    srand(1);\n    r = rand() % 10;\n    printf(\"%d %d\\n\", r, RAND_MAX);\n"),
    c("    int r;\n    srand(1);\n    r = rand() % 10;\n    printf(\"%d %d\\n\", r, RAND_MAX);\n", inc="#include <stdio.h>\n#include <stdlib.h>\n"),
    rs("    let r = rand() % 10;\n    println!(\"{r} {RAND_MAX}\");\n", pre=RNG),
    rs("    let r = rand() % 10;\n    println!(\"{r} {RAND_MAX}\");\n", pre=RNG + "use rng::{rand, RAND_MAX};\n"))
FIRST_C = "int first(int a[])\n{\n    return a[0];\n}\n"
FIRST_R = "\nfn first(a: &[i32]) -> i32 {\n    a[0]\n}\n"
add("P21", "配列を渡すところに要素（数）を渡す",
    c("    int s[3] = {1, 2, 3};\n    printf(\"%d\\n\", first(s[2]));\n", pre=FIRST_C),
    c("    int s[3] = {1, 2, 3};\n    printf(\"%d\\n\", first(s));\n", pre=FIRST_C),
    rs("    let s = [1, 2, 3];\n    println!(\"{}\", first(s[2]));\n", pre=FIRST_R),
    rs("    let s = [1, 2, 3];\n    println!(\"{}\", first(&s));\n", pre=FIRST_R))
add("P22", "int に入りきらない計算",
    c("    printf(\"%d\\n\", 1024 * 1024 * 1024 * 2 * 2);\n"),
    c("    printf(\"%d\\n\", 1024 * 1024 * 1024);\n"),
    rs("    println!(\"{}\", 1024 * 1024 * 1024 * 2 * 2);\n"),
    rs("    println!(\"{}\", 1024 * 1024 * 1024);\n"))
add("P23", "2文字を '' で囲む",
    c("    char s[] = \"my\";\n    if (s[0] == 'my') {\n        printf(\"found\\n\");\n    }\n"),
    c("    char s[] = \"my\";\n    if (s[0] == 'm' && s[1] == 'y') {\n        printf(\"found\\n\");\n    }\n"),
    rs("    let s: Vec<char> = \"my\".chars().collect();\n    if s[0] == 'my' {\n        println!(\"found\");\n    }\n"),
    rs("    let s: Vec<char> = \"my\".chars().collect();\n    if s[0] == 'm' && s[1] == 'y' {\n        println!(\"found\");\n    }\n"))
add("P24", "if の後ろに ; を付けて空の if になる",
    c("    int n = 0;\n    scanf(\"%d\", &n);\n    if (n % 2 != 0);\n    {\n        printf(\"odd\\n\");\n    }\n"),
    c("    int n = 0;\n    scanf(\"%d\", &n);\n    if (n % 2 != 0) {\n        printf(\"odd\\n\");\n    }\n"),
    rs("    let mut n: i32 = 0;\n    read_into::<i32>(&mut n);\n    if n % 2 != 0;\n    {\n        println!(\"odd\");\n    }\n", read=True),
    rs("    let mut n: i32 = 0;\n    read_into::<i32>(&mut n);\n    if n % 2 != 0 {\n        println!(\"odd\");\n    }\n", read=True),
    stdin="4\n")
add("P25", "{ } なしの if で2行目が if の外に出る",
    c("    int n = 0;\n    scanf(\"%d\", &n);\n    if (n % 5 != 0)\n        printf(\"not 5\\n\");\n        printf(\"not divisible\\n\");\n"),
    c("    int n = 0;\n    scanf(\"%d\", &n);\n    if (n % 5 != 0) {\n        printf(\"not 5\\n\");\n        printf(\"not divisible\\n\");\n    }\n"),
    rs("    let mut n: i32 = 0;\n    read_into::<i32>(&mut n);\n    if n % 5 != 0 {\n        println!(\"not 5\");\n        println!(\"not divisible\");\n    }\n", read=True),
    rs("    let mut n: i32 = 0;\n    read_into::<i32>(&mut n);\n    if n % 5 != 0 {\n        println!(\"not 5\");\n        println!(\"not divisible\");\n    }\n", read=True),
    stdin="10\n", note="Rust は if に { } が必須なので、このミスは書けない")
add("P26", "for の初期化を n-1 と書く（代入になっていない）",
    c("    int n;\n    for (n - 1; n <= 3; n++) {\n        printf(\"%d\\n\", n);\n    }\n"),
    c("    int n;\n    for (n = 1; n <= 3; n++) {\n        printf(\"%d\\n\", n);\n    }\n"),
    rs("    let mut n: i32;\n    n - 1;\n    while n <= 3 {\n        println!(\"{n}\");\n        n += 1;\n    }\n"),
    rs("    let mut n = 1;\n    while n <= 3 {\n        println!(\"{n}\");\n        n += 1;\n    }\n"))
add("P27", "まとめて0にするつもりで , を使う（a,b,c=0;）",
    c("    int a, b, c;\n    a, b, c = 0;\n    printf(\"%d %d %d\\n\", a, b, c);\n"),
    c("    int a, b, c;\n    a = b = c = 0;\n    printf(\"%d %d %d\\n\", a, b, c);\n"),
    rs("    let a: i32;\n    let b: i32;\n    let c: i32;\n    let _ = (a, b, c = 0);\n    println!(\"{a} {b} {c}\");\n"),
    rs("    let (a, b, c) = (0, 0, 0);\n    println!(\"{a} {b} {c}\");\n"))
add("P28", "for の条件に , を書く（n,10）",
    c("    int n;\n    for (n = 0; n, 3; n++) {\n        printf(\"%d\\n\", n);\n    }\n"),
    c("    int n;\n    for (n = 0; n < 3; n++) {\n        printf(\"%d\\n\", n);\n    }\n"),
    rs("    let mut n = 0;\n    while (n, 3) {\n        println!(\"{n}\");\n        n += 1;\n    }\n"),
    rs("    let mut n = 0;\n    while n < 3 {\n        println!(\"{n}\");\n        n += 1;\n    }\n"))
add("P29", "+ を ; と打って足し算が消える（sum = sum ; a[i];）",
    c("    int a[3] = {1, 2, 3};\n    int sum = 0, i;\n    for (i = 0; i < 3; i++) {\n        sum = sum ; a[i];\n    }\n    printf(\"%d\\n\", sum);\n"),
    c("    int a[3] = {1, 2, 3};\n    int sum = 0, i;\n    for (i = 0; i < 3; i++) {\n        sum = sum + a[i];\n    }\n    printf(\"%d\\n\", sum);\n"),
    rs("    let a = [1, 2, 3];\n    let mut sum = 0;\n    let mut i = 0;\n    while i < 3 {\n        sum = sum; a[i];\n        i += 1;\n    }\n    println!(\"{sum}\");\n"),
    rs("    let a = [1, 2, 3];\n    let mut sum = 0;\n    let mut i = 0;\n    while i < 3 {\n        sum += a[i];\n        i += 1;\n    }\n    println!(\"{sum}\");\n"))
add("P30", "for の ; を , にして条件が i++ になる",
    c("    int i;\n    for (i = 0, i < 2; i++;) {\n        printf(\"%d\\n\", i);\n    }\n"),
    c("    int i;\n    for (i = 0; i < 2; i++) {\n        printf(\"%d\\n\", i);\n    }\n"),
    rs("    let mut i: i32;\n    let _ = (i = 0, i < 2);\n    while { let t = i; i += 1; t } {\n        println!(\"{i}\");\n    }\n"),
    rs("    let mut i = 0;\n    while i < 2 {\n        println!(\"{i}\");\n        i += 1;\n    }\n"))

# ---- ロジックのミス ----
add("P40a", "ループの範囲が1つずれる（i<n と i<=n など）",
    c("    int n = 0, i, sum = 0;\n    scanf(\"%d\", &n);\n    for (i = 1; i < n; i++) {\n        sum = sum + i;\n    }\n    printf(\"%d\\n\", sum);\n"),
    c("    int n = 0, i, sum = 0;\n    scanf(\"%d\", &n);\n    for (i = 1; i <= n; i++) {\n        sum = sum + i;\n    }\n    printf(\"%d\\n\", sum);\n"),
    rs("    let mut n: i32 = 0;\n    read_into::<i32>(&mut n);\n    let mut sum = 0;\n    let mut i = 1;\n    while i < n {\n        sum += i;\n        i += 1;\n    }\n    println!(\"{sum}\");\n", read=True),
    rs("    let mut n: i32 = 0;\n    read_into::<i32>(&mut n);\n    let mut sum = 0;\n    let mut i = 1;\n    while i <= n {\n        sum += i;\n        i += 1;\n    }\n    println!(\"{sum}\");\n", read=True),
    stdin="5\n")
add("P40b", "変数・添字の取り違え",
    c("    double x1 = 1, y1 = 2, x2 = 3, y2 = 8;\n    double a = (y2 - y1) / (x2 - x1);\n    double b = y2 - a * y1;\n    printf(\"%f %f\\n\", a, b);\n"),
    c("    double x1 = 1, y1 = 2, x2 = 3, y2 = 8;\n    double a = (y2 - y1) / (x2 - x1);\n    double b = y2 - a * x2;\n    printf(\"%f %f\\n\", a, b);\n"),
    rs("    let (x1, y1, x2, y2) = (1.0, 2.0, 3.0, 8.0);\n    let a = (y2 - y1) / (x2 - x1);\n    let b = y2 - a * y1;\n    println!(\"{a} {b}\");\n"),
    rs("    let (x1, y1, x2, y2) = (1.0, 2.0, 3.0, 8.0);\n    let a = (y2 - y1) / (x2 - x1);\n    let b = y2 - a * x2;\n    println!(\"{a} {b}\");\n"))
add("P40c", "計算式・初期値のミス（10*e を 10+e など）",
    c("    int a = 1, e = 2;\n    int total = 1000 * a + 10 + e;\n    printf(\"%d\\n\", total);\n"),
    c("    int a = 1, e = 2;\n    int total = 1000 * a + 10 * e;\n    printf(\"%d\\n\", total);\n"),
    rs("    let (a, e) = (1, 2);\n    let total = 1000 * a + 10 + e;\n    println!(\"{total}\");\n"),
    rs("    let (a, e) = (1, 2);\n    let total = 1000 * a + 10 * e;\n    println!(\"{total}\");\n"))
add("P41", "初期化していない変数を条件に使う（x%i）",
    c("    int n = 12, i = 3, t = 0, x;\n    if (x % i == 0) {\n        t = 1;\n    }\n    printf(\"%d %d\\n\", t, n);\n"),
    c("    int n = 12, i = 3, t = 0;\n    if (n % i == 0) {\n        t = 1;\n    }\n    printf(\"%d %d\\n\", t, n);\n"),
    rs("    let (n, i) = (12, 3);\n    let mut t = 0;\n    let x: i32;\n    if x % i == 0 {\n        t = 1;\n    }\n    println!(\"{t} {n}\");\n"),
    rs("    let (n, i) = (12, 3);\n    let mut t = 0;\n    if n % i == 0 {\n        t = 1;\n    }\n    println!(\"{t} {n}\");\n"))
add("P42", "整数どうしの割り算で小数が消える（1/2 が 0）",
    c("    double pi = 0.0;\n    int i;\n    for (i = 0; i < 3; i++) {\n        pi = pi + 1 / (2 * i + 1);\n    }\n    printf(\"%f\\n\", pi);\n"),
    c("    double pi = 0.0;\n    int i;\n    for (i = 0; i < 3; i++) {\n        pi = pi + 1.0 / (2 * i + 1);\n    }\n    printf(\"%f\\n\", pi);\n"),
    rs("    let mut pi = 0.0;\n    let mut i = 0;\n    while i < 3 {\n        pi += 1 / (2 * i + 1);\n        i += 1;\n    }\n    println!(\"{pi}\");\n"),
    rs("    let mut pi = 0.0;\n    let mut i = 0;\n    while i < 3 {\n        pi += 1.0 / f64::from(2 * i + 1);\n        i += 1;\n    }\n    println!(\"{pi}\");\n"))
add("P43", "合計用の変数の初期化忘れ",
    c("    int a[3] = {1, 2, 3};\n    int sum, i;\n    for (i = 0; i < 3; i++) {\n        sum = sum + a[i];\n    }\n    printf(\"%d\\n\", sum);\n"),
    c("    int a[3] = {1, 2, 3};\n    int sum = 0, i;\n    for (i = 0; i < 3; i++) {\n        sum = sum + a[i];\n    }\n    printf(\"%d\\n\", sum);\n"),
    rs("    let a = [1, 2, 3];\n    let mut sum: i32;\n    let mut i = 0;\n    while i < 3 {\n        sum += a[i];\n        i += 1;\n    }\n    println!(\"{sum}\");\n"),
    rs("    let a = [1, 2, 3];\n    let mut sum = 0;\n    let mut i = 0;\n    while i < 3 {\n        sum += a[i];\n        i += 1;\n    }\n    println!(\"{sum}\");\n"))
add("P44", "配列が小さくて範囲外に書き込む",
    c("    int a[9], i;\n    for (i = 0; i <= 9; i++) {\n        a[i] = i;\n    }\n    printf(\"%d\\n\", a[8]);\n"),
    c("    int a[10], i;\n    for (i = 0; i <= 9; i++) {\n        a[i] = i;\n    }\n    printf(\"%d\\n\", a[8]);\n"),
    rs("    let mut a = [0; 9];\n    let mut i = 0;\n    while i <= 9 {\n        a[i] = i;\n        i += 1;\n    }\n    println!(\"{}\", a[8]);\n"),
    rs("    let mut a = [0; 10];\n    let mut i = 0;\n    while i <= 9 {\n        a[i] = i;\n        i += 1;\n    }\n    println!(\"{}\", a[8]);\n"))
add("P45", "0 で割る（i=0 から始めて p%i）",
    c("    int p = 7, i, c = 0;\n    for (i = 0; i < p; i++) {\n        if (p % i == 0) {\n            c++;\n        }\n    }\n    printf(\"%d\\n\", c);\n"),
    c("    int p = 7, i, c = 0;\n    for (i = 2; i < p; i++) {\n        if (p % i == 0) {\n            c++;\n        }\n    }\n    printf(\"%d\\n\", c);\n"),
    rs("    let p = 7;\n    let mut c = 0;\n    let mut i = 0;\n    while i < p {\n        if p % i == 0 {\n            c += 1;\n        }\n        i += 1;\n    }\n    println!(\"{c}\");\n"),
    rs("    let p = 7;\n    let mut c = 0;\n    let mut i = 2;\n    while i < p {\n        if p % i == 0 {\n            c += 1;\n        }\n        i += 1;\n    }\n    println!(\"{c}\");\n"))
