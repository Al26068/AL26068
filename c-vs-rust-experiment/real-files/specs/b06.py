# -*- coding: utf-8 -*-
# 追加ルール：fread/fwrite（1バイトずつ）→ 標準入出力の read/write、scanf("%c") → 1バイト読み、
# 初期化していない変数を読む書き方（ミス以外の部分）は、Rust では必須なので 0 で初期化する。
S = {}

BYTES = r'''
use std::io::{Read, Write};

/// fread の代わり：標準入力から1バイト読む（読めなければ None）
fn fread_byte() -> Option<u8> {
    let mut b = [0_u8; 1];
    match std::io::stdin().read(&mut b) {
        Ok(1) => Some(b[0]),
        _ => None,
    }
}

/// fwrite の代わり：標準出力に1バイト書く
fn fwrite_byte(b: u8) {
    let _ = std::io::stdout().write_all(&[b]);
}
'''

S["pro2/Week4/ex4-1.c"] = dict(pre=BYTES, base=r'''
const LEN: usize = 256;

fn main() {
    let mut x: usize;
    let mut y: usize;
    let mut color: usize;
    let mut i: usize;
    let mut color_in = vec![[[0_u8; 3]; LEN]; LEN]; // 色（BGR）の配列（入力用）
    let mut color_out = vec![[[0_u8; 3]; LEN]; LEN]; // 色（BGR）の配列（出力用）

    // ファイル（標準入力）の処理
    i = 0;
    while i < 54 {
        // 標準入力の先頭54バイトを標準出力へコピー
        let a = fread_byte().unwrap_or(0);
        fwrite_byte(a);
        i += 1;
    }
    y = 0;
    while y < LEN {
        x = 0;
        while x < LEN {
            color = 0;
            while color < 3 {
                color_in[y][x][color] = fread_byte().unwrap_or(0);
                color += 1;
            }
            x += 1;
        }
        y += 1;
    }

    // 右90度回転処理
    y = 0;
    while y < LEN {
        x = 0;
        while x < LEN {
            color = 0;
            while color < 3 {
                color_out[LEN - 1 - x][LEN - 1 - y][color] = color_in[x][y][color];
                color += 1;
            }
            x += 1;
        }
        y += 1;
    }

    // 各pixelの色を標準出力へ出力
    y = 0;
    while y < LEN {
        x = 0;
        while x < LEN {
            color = 0;
            while color < 3 {
                fwrite_byte(color_out[y][x][color]);
                color += 1;
            }
            x += 1;
        }
        y += 1;
    }
}
''', stdin="".join(chr(65 + (k * 7) % 26) for k in range(54 + 256 * 256 * 3)), m={
    233: dict(ctx=[("= color_in[x][y][color];", "= color_in[y][x][color];")],
              bug=[("color_out[LEN - 1 - x][LEN - 1 - y][color] = color_in[y][x][color];", "color_out[x][LEN - 1 - y][color] = color_in[y][x][color];")]),
    234: dict(bug=[("= color_in[x][y][color];", "= color_in[y][x][color];")]),
})

S["pro2/Week4/ex4-2.c"] = dict(pre="\nuse std::io::Read;\n", base=r'''
const LEN: usize = 200000;

fn main() {
    let mut romeo = vec![0_u8; LEN]; // ファイル全体の文字列格納
    let mut i: usize; // 配列の添字用
    let mut num: usize; // ファイル全体の文字数カウント
    let mut count_a: i32; // aのカウント
    let mut count_my: i32;

    num = 0;
    // この部分はファイル処理です。
    i = 0;
    while i < LEN {
        num += 1;
        let mut b = [0_u8; 1];
        if std::io::stdin().read(&mut b).unwrap_or(0) == 0 {
            break;
        }
        romeo[i] = b[0];
        i += 1;
    }

    count_a = 0;
    i = 0;
    while i < num {
        if romeo[i] == b'a' {
            count_a += 1;
        }
        i += 1;
    }
    println!("'a'は{count_a}回出現しました。");

    count_my = 0;
    i = 0;
    while i < num - 1 {
        if romeo[i] == b'm' && romeo[i + 1] == b'y' {
            count_my += 1;
        }
        i += 1;
    }
    println!("myは{count_my}回出現しました。");
}
''', stdin="my name is romeo. call me my love, and I will be new baptized.\n", m={
    140: dict(bug=[("if romeo[i] == b'm' && romeo[i + 1] == b'y' {", "if romeo[i] == b'my' {")]),
    235: dict(bug=[("    while i < num - 1 {", "    while i < num {")]),
})

S["pro2/Week6/ex6-3.c"] = dict(base=r'''
fn sort(p: &mut [i32], size: usize) {
    let mut i: usize;
    let mut x: i32;
    let mut change: i32 = 1;
    while change == 1 {
        change = 0;
        i = 0;
        while i < size - 1 {
            if p[i] > p[i + 1] {
                x = p[i];
                p[i] = p[i + 1];
                p[i + 1] = x;
                change = 1;
            }
            i += 1;
        }
    }
}

fn main() {
    let mut a = [0_i32; 5];
    let mut i: usize;
    i = 0;
    while i < 5 {
        print!("a[{i}]=");
        read_into::<i32>(&mut a[i]);
        i += 1;
    }
    println!("ソート後:");
    sort(&mut a, 5);
    i = 0;
    while i < 5 {
        println!("a[{}]={}", i, a[i]);
        i += 1;
    }
}
''', m={
    180: dict(ctx=[("    sort(&mut a, 5);\n", "")], bug=[('println!("a[{}]={}", i, a[i]);', 'println!("a[{}]={}", i, sort(&mut a, 5));')]),
})

S["pro2/Week3/ex3-3.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    let mut i: i32;
    // xは割られる数,yは割る数
    let mut amari: i32;
    print!("正の整数(割られる数)を入力してください:");
    read_into::<i32>(&mut x);
    print!("正の数(割る数)を入力してください:");
    read_into::<i32>(&mut y);
    print!("{}", x / y);
    amari = x % y;

    i = 0;
    while i < 50 {
        if amari == 0 {
            break;
        }
        if i == 0 {
            print!(".");
        }
        amari *= 10;
        x = amari;
        amari = x % y;
        print!("{}", x / y);
        i += 1;
    }
}
''', stdin="22\n7\n", m={
    137: dict(bug=None, why="printf の %f → Rust の {} は型を書かないので、型の食い違いが書けない"),
    138: dict(bug=[('    print!("{}", x / y);\n    amari = x % y;', '    prinft!("{}", x / y);\n    amari = x % y;')]),
    230: dict(ctx=[("        if i == 0 {", "        if i == 1 {")], bug=[("        if i == 1 {", "        if i == 0 {")]),
})

S["pro2/Week5/ex5-4.c"] = dict(base=r'''
fn is_prime(n: i32) -> i32 {
    let mut i: i32;
    let mut t: i32 = 0;
    i = 2;
    while i < n {
        if n % i == 0 {
            t = 0;
            break;
        } else {
            t = 1;
            break;
        }
    }
    t
}

fn main() {
    let mut x: i32 = 0;
    print!("正の整数を入力してください");
    read_into::<i32>(&mut x);

    if is_prime(x) == 0 {
        print!("{x}は素数ではありません");
    } else {
        print!("{x}は素数です。");
    }
}
''', stdin="9\n", m={
    167: dict(bug=[("    let mut i: i32;\n    let mut t: i32 = 0;\n    i = 2;", "    let mut i: i32;\n    let n: i32;\n    let mut t: i32 = 0;\n    i = 2;")]),
    240: dict(bug=[("    i = 2;\n    while i < n {", "    i = 1;\n    while i < n {")]),
    241: dict(ctx=[("    while i < n {", "    while i <= n {")], bug=[("    while i <= n {", "    while i < n {")]),
    242: dict(bug=[("    let mut t: i32 = 0;\n", "    let x: i32;\n    let mut t: i32 = 0;\n"), ("        if n % i == 0 {", "        if x % i == 0 {")]),
})

S["pro2/Week8/8-2.c"] = dict(base=r'''
fn count_spaces(s: &str) -> i32 {
    let b = s.as_bytes();
    let mut count = 0;
    let mut i: usize = 0;

    while i < b.len() && b[i] != b'\0' {
        if b[i] == b' ' {
            count += 1;
        }
        i += 1;
    }
    count
}

fn main() {
    let mut moji = String::new();

    print!("英語の文字列を入力してください:");
    let _ = std::io::stdin().read_line(&mut moji);
    if let Some(p) = moji.find('\n') {
        moji.truncate(p);
    }
    print!("文字列{}の中の空白の数は{}です", moji, count_spaces(&moji));
}
''', stdin="this is a pen\n", m={
    184: dict(bug=[('print!("文字列{}の中の空白の数は{}です", moji, count_spaces(&moji));', 'print!("文字列"{}"の中の空白の数は{}です", char[100], i);')]),
    185: dict(bug=[('print!("文字列{}の中の空白の数は{}です", moji, count_spaces(&moji));', 'print!("文字列{}の中の空白の数は{}です", count_spaces(&moji), i);')]),
    186: dict(bug=None, why="printf の %c → Rust の {} は型を書かないので、文字と文字列の食い違いが書けない"),
    187: dict(bug=[("if b[i] == b' ' {", "if b[i] == b'' {")]),
})

S["pro2/Week6/ex6-2.c"] = dict(base=r'''
fn min(p: &[i32], size: usize) -> i32 {
    let mut x: i32 = p[0];
    let mut i: usize;

    i = 0;
    while i < size {
        if x > p[i] {
            x = p[i];
        }
        i += 1;
    }
    x
}

fn main() {
    let mut a = [0_i32; 5];
    let mut i: usize;

    i = 0;
    while i < 5 {
        print!("a[{i}]=");
        read_into::<i32>(&mut a[i]);
        i += 1;
    }
    print!("最小値は{}です", min(&a, 5));
}
''', m={
    177: dict(bug=[('    i = 0;\n    while i < 5 {\n        print!("a[{i}]=");', '    while (i = 0, i < 5; i += 1)[\n        print!("a[{i}]=");')]),
    178: dict(bug=[("        if x > p[i] {", "        if x > a[i] {")]),
    179: dict(bug=[('print!("最小値は{}です", min(&a, 5));', 'print!("最小値は&dです", min(&a, 5));')]),
    247: dict(bug=[("let mut x: i32 = p[0];", "let mut x: i32 = 0;")]),
})
