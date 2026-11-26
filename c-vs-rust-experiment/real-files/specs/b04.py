# -*- coding: utf-8 -*-
# 追加ルール：授業のヘッダー terminalmode2.h は同じ名前の関数を持つ Rust のモジュールに置き換える（unsafe なし）。
# C の暗黙の型変換（double を int の引数に渡すなど）は Rust では as で明示する。
S = {}

TERMINALMODE2 = r'''
mod terminalmode2 {
    //! 授業のヘッダー terminalmode2.h の代わり（同じ名前の関数だけ用意）
    use std::cell::RefCell;

    /// 緑
    pub const MIDORI: u8 = 4;

    thread_local! {
        static CANVAS: RefCell<Vec<Vec<u8>>> = const { RefCell::new(Vec::new()) };
    }

    /// キャンバスの大きさを決める
    pub fn led_canvas_setsize(r: usize, c: usize) {
        CANVAS.with(|cv| *cv.borrow_mut() = vec![vec![0; c]; r]);
    }

    /// 行の数
    pub fn led_max_row() -> usize {
        CANVAS.with(|cv| cv.borrow().len())
    }

    /// 列の数
    pub fn led_max_col() -> usize {
        CANVAS.with(|cv| cv.borrow().first().map_or(0, Vec::len))
    }

    /// 全部消す
    pub fn led_canvas_clear() {
        CANVAS.with(|cv| {
            for row in cv.borrow_mut().iter_mut() {
                row.fill(0);
            }
        });
    }

    /// 1マス塗る
    pub fn led_canvas_set_pixel(row: usize, col: usize, color: u8) {
        CANVAS.with(|cv| cv.borrow_mut()[row][col] = color);
    }

    /// 表示する
    pub fn led_canvas_display() {
        CANVAS.with(|cv| {
            for row in cv.borrow().iter() {
                let line: String = row.iter().map(|&c| if c == 0 { ' ' } else { '#' }).collect();
                println!("|{line}|");
            }
        });
    }
}
use terminalmode2::*;
'''

S["pro1/ex4/Challenge4-A2.c"] = dict(pre=TERMINALMODE2, base=r'''
fn main() {
    let mut row: usize;
    let mut col: usize;

    led_canvas_setsize(24, 24);
    led_canvas_clear();

    row = 0;
    while row < led_max_row() {
        col = row * led_max_col() / led_max_row();
        while col < led_max_col() {
            if (row + col) % 2 == 0 {
                led_canvas_set_pixel(row, col, MIDORI);
            }
            col += 1;
        }
        row += 1;
    }

    led_canvas_display();
}
''', m={
    49: dict(bug=[("        while col < led_max_col() {", "        while i < led_max_col() {")]),
    50: dict(bug=[("    led_canvas_display();\n}\n", "    led_canvas_display();\n")]),
})

S["pro1/ex4/ex4-3.c"] = dict(base=r'''
fn main() {
    let mut pi: f64;
    let mut i: f64;
    let mut n: f64 = 0.0;
    pi = 0.0;
    println!("n?");
    read_into::<f64>(&mut n);
    i = 0.0;
    while i <= n {
        pi += (-1.0_f64).powf(i) / (2.0 * i + 1.0);
        i += 1.0;
    }
    pi *= 4.0;
    print!("第{:.6}項までの近似値は{:.6}です。", n, pi);
}
''', stdin="100\n", m={
    51: dict(bug=[("        pi += (-1.0_f64).powf(i) / (2.0 * i + 1.0);\n", "        pi += ((-1) ^ i) / (2 * i + 1)\n")]),
    52: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    53: dict(bug=[("    pi = 0.0;\n", "    let mut pi: f64 = 0.0;\n")]),
    54: dict(ctx=[("let mut n: f64 = 0.0;", "let mut n: i32 = 0;"), ("read_into::<f64>(&mut n);", "read_into::<i32>(&mut n);"),
                  ("while i <= n {", "while i <= f64::from(n) {")],
             bug=[("read_into::<i32>(&mut n);", "read_into::<f64>(&mut n);")]),
    55: dict(bug=None, why="pow は Rust では数値の powf メソッドなので、#include（use）忘れが起きない"),
    56: dict(bug=[("read_into::<f64>(&mut n);", "read_into::<i32>(&mut n);")]),
    57: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    58: dict(bug=[("        pi += (-1.0_f64).powf(i) / (2.0 * i + 1.0);\n", "        if pi % 2 == 0 {\n            pi += 1.0 / (2.0 * i + 1.0);\n        }\n")]),
    202: dict(bug=None, exclude=True, why="見直したらミスではなかった（1.0 があるので C でも小数で計算される）"),
    203: dict(bug=[("while i <= n {", "while i < n {")]),
})

S["pro1/ex4/ex4-5.c"] = dict(base=r'''
fn main() {
    let mut max: i32 = 0;
    let mut i: i32;
    let mut j: i32;
    let mut x: i32;

    println!("max?");
    read_into::<i32>(&mut max);
    i = 2;
    while i <= max {
        x = 1;
        j = 2;
        while j < i {
            if i % j == 0 {
                x = 0;
                break;
            }
            j += 1;
        }
        if x == 1 {
            println!("{i}");
        }
        i += 1;
    }
}
''', stdin="30\n", m={
    63: dict(bug=[("        i += 1;\n    }\n}\n", "        i += 1;\n    }\n")]),
    64: dict(bug=[("        x = 1;\n        j = 2;", "        if max % i != 0;\n        j = 2;")]),
    204: dict(bug=[("            j += 1;\n", "            i += 1;\n")]),
})

S["pro1/ex6/ex6-5.c"] = dict(base=r'''
fn function(n: i32) -> f64 {
    let a: f64 = 0.0;
    let b: f64 = 1.0;
    let mut s: f64 = 0.0;
    let dx: f64 = (b - a) / f64::from(n);
    let mut i: i32 = 0;
    while i < n {
        let x: f64 = a + f64::from(i) * dx;
        s += x * x * dx;
        i += 1;
    }
    s
}

fn main() {
    let mut n: f64 = 0.0;
    print!("n?");
    read_into::<f64>(&mut n);
    print!("{:.6}", function(n as i32));
}
''', stdin="100\n", m={
    79: dict(bug=[("function(n as i32))", "function(a, b, x))")]),
    80: dict(bug=None, why="abs は Rust では数値の abs メソッドなので、#include 忘れも、double に int 用の abs を使うミスも起きない"),
    81: dict(bug=[("read_into::<f64>(&mut n);", "read_into::<i32>(&mut n);")]),
    215: dict(bug=[("let b: f64 = 1.0;", "let b: f64 = 0.0;")]),
    216: dict(bug=[("        s += x * x * dx;", "        s = x * x * dx;")]),
    217: dict(bug=[("let mut s: f64 = 0.0;", "let mut s: f64;")]),
})

S["pro2/Week2/ex2-2.c"] = dict(base=r'''
fn main() {
    let mut p: i32 = 0;
    let mut i: i32;
    let mut x: i32 = 1;
    print!("正の整数を入力してください");
    read_into::<i32>(&mut p);
    if p < 2 {
        x = 0;
    }
    i = 2;
    while i < p {
        if p % i == 0 {
            x = 0;
            break;
        }
        i += 1;
    }
    if x == 1 {
        print!("{p}は素数です");
    } else {
        println!("{p}は素数ではありません");
    }
}
''', stdin="7\n", m={
    127: dict(bug=None, why="型なしのグローバル変数 x=1; → main の中の let mut x = 1; は Rust では型推論で正しく動く"),
    228: dict(bug=[("    i = 2;\n    while i < p {", "    i = 0;\n    while i < p {")]),
})

S["pro2/Week5/ex5-2.c"] = dict(base=r'''
fn gcd(mut n: i32, mut m: i32) -> i32 {
    while m != 0 {
        let r: i32 = n % m;
        n = m;
        m = r;
    }
    n
}

fn main() {
    let mut n: i32 = 0;
    let mut m: i32 = 0;
    print!("正の整数を入力してください:");
    read_into::<i32>(&mut n);
    print!("正の整数を入力してください:");
    read_into::<i32>(&mut m);
    print!("{}と{}の最大公約数は{}です", n, m, gcd(n, m));
}
''', stdin="12\n18\n", m={
    165: dict(bug=[("    n\n}\n", "    a\n}\n")]),
    166: dict(bug=[("    while m != 0 {", "    while b != 0 {")]),
})
