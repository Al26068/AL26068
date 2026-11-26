# -*- coding: utf-8 -*-
S = {}

BASE = r'''
fn main() {
    let mut i: usize;
    let mut l: usize;
    let mut m: usize;
    let mut n: usize;
    let sum: f64;
    let avg: f64;
    let mut spread: f64;
    let standard: f64;
    let mut score = [0.0_f64; 10];
    let mut standardvalue = [0.0_f64; 10];
    i = 0;
    while i < 10 {
        read_into::<f64>(&mut score[i]);
        i += 1;
    }

    // 平均
    sum = score[0] + score[1] + score[2] + score[3] + score[4] + score[5] + score[6] + score[7] + score[8] + score[9];
    avg = sum / 10.0;
    // 分散
    spread = 0.0;
    l = 0;
    while l < 10 {
        spread += (score[l] - avg).powf(2.0);
        l += 1;
    }
    spread /= 10.0;
    // 標準偏差
    standard = spread.powf(0.5);

    // 偏差値
    m = 0;
    while m < 10 {
        standardvalue[m] = ((score[m] - avg) / standard) * 10.0 + 50.0;
        m += 1;
    }
    n = 0;
    while n < 10 {
        println!("得点{:.0}の偏差値は{:.2}です", score[n], standardvalue[n]);
        n += 1;
    }
}
'''

INT_SCORE = [  # 当時は score が int 配列だった状態（C の暗黙の変換は f64::from で明示）
    ("let mut score = [0.0_f64; 10];", "let mut score = [0_i32; 10];"),
    ("read_into::<f64>(&mut score[i]);", "read_into::<i32>(&mut score[i]);"),
    ("    sum = score[0] + score[1] + score[2] + score[3] + score[4] + score[5] + score[6] + score[7] + score[8] + score[9];",
     "    sum = f64::from(score[0] + score[1] + score[2] + score[3] + score[4] + score[5] + score[6] + score[7] + score[8] + score[9]);"),
    ("spread += (score[l] - avg).powf(2.0);", "spread += (f64::from(score[l]) - avg).powf(2.0);"),
    ("standardvalue[m] = ((score[m] - avg) / standard)", "standardvalue[m] = ((f64::from(score[m]) - avg) / standard)"),
]

S["pro1/ex5/ex5-3.c"] = dict(base=BASE, stdin="50\n60\n70\n80\n90\n55\n65\n75\n85\n95\n", m={
    67: dict(ctx=[("    let sum: f64;", "    let mut sum: f64;\n    let mut k: usize;"),
                  ("    sum = score[0] + score[1] + score[2] + score[3] + score[4] + score[5] + score[6] + score[7] + score[8] + score[9];",
                   "    sum = 0.0;\n    k = 0;\n    while k < 10 {\n        sum += score[k];\n        k += 1;\n    }")],
             bug=[("        sum += score[k];", "        sum += a[k];")]),
    68: dict(bug=[("        spread += (score[l] - avg).powf(2.0);\n        l += 1;\n    }\n", "        spread += (score[l] - avg).powf(2.0);\n        l += 1;\n        while\n    }\n")]),
    69: dict(bug=[("    let mut spread: f64;", "    let mut spread: [f64; 10];")]),
    70: dict(bug=[("    standard = spread.powf(0.5);", "    standard")]),
    71: dict(bug=[("read_into::<f64>(&mut score[i]);", "raed_into::<f64>(&mut score[i]);")]),
    72: dict(bug=[("    n = 0;\n    while n < 10 {", "    n = 0;\n    while (n, 10) {")]),
    73: dict(ctx=INT_SCORE, bug=[("read_into::<i32>(&mut score[i]);", "read_into::<f64>(&mut score[i]);")]),
    74: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    75: dict(bug=[("let mut score = [0.0_f64; 10];", "let mut score = [0_i32; 10];")]),
    206: dict(bug=[("spread += (score[l] - avg).powf(2.0);", "spread += (score[i] - avg).powf(2.0);")]),
    207: dict(bug=[("    standard = spread.powf(0.5);", "    standard = spread.powf(1 / 2);")]),
    208: dict(bug=[("score[0] + score[1] + score[2]", "score[0] + score[2]")]),
    209: dict(bug=[("standardvalue[m] = ((score[m] - avg) / standard)", "standardvalue[m] = ((score[i] - avg) / standard)")]),
    210: dict(bug=[("spread += (score[l] - avg).powf(2.0);", "spread = (score[l] - avg).powf(2.0);")]),
    211: dict(bug=[("    spread = 0.0;\n", "")]),
})
