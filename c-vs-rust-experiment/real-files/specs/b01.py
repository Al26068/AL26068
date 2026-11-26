# -*- coding: utf-8 -*-
# 書き換えルール：グローバル変数は main の中の変数に（unsafe を使わないため）、scanf の入れ先は 0 で初期化、
# for → while、%d %f → {} {:.6}、int→i32 double→f64 long long→i64、変数名はスネークケースに。
S = {}

S["pro1/samp2-1.c"] = dict(base=r'''
fn main() {
    println!("{}", 1024 * 1024 * 1024);
}
''', m={
    95: dict(bug=[("1024 * 1024 * 1024)", "1024 * 1024 * 1024 * 2 * 2)")]),
    96: dict(bug=[("1024 * 1024 * 1024);", "1024 * 1024 * 1024;")]),
})

S["pro1/samp4/samp4-1.c"] = dict(base=r'''
fn main() {
    let mut i: i32 = 0;
    while i < 128 {
        println!("{} {}", i, char::from(i as u8));
        i += 1;
    }
}
''', m={
    220: dict(bug=[("""    while i < 128 {
        println!("{} {}", i, char::from(i as u8));
        i += 1;
    }""", """    while i < 128 {
        i += 1;
    }
    {
        println!("{} {}", i, char::from(i as u8));
    }""")]),
})

S["pro2/Week1/1-1.c"] = dict(base=r'''
fn main() {
    let mut money: i32 = 0;
    println!("金額を入力してください:");
    read_into::<i32>(&mut money);
    println!("消費税を含めた金額は{:.0}円です", f64::from(money) * 1.1);
}
''', m={
    105: dict(bug=[("read_into::<i32>(&mut money);", "read_into::<i32>(\\n);")]),
    106: dict(ctx=[("let mut money: i32 = 0;", "let mut money: f64 = 0.0;"),
                   ("read_into::<i32>(&mut money);", "read_into::<f64>(&mut money);"),
                   ("f64::from(money) * 1.1", "money * 1.1")],
              bug=[("read_into::<f64>(&mut money);", "read_into::<i32>(&mut money);")]),
    107: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    108: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
})

S["pro2/Week1/b.c"] = dict(base=r'''
fn main() {
    let average: f64 = f64::from(40 + 45) / 2.0;
    println!("average={average:.6}");
    let int_aver: i32 = average as i32;
    println!("average={int_aver}");
}
''', m={
    109: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
})

S["pro2/Week5/5-1.c"] = dict(base=r'''
fn circumeference(radius: f64) -> f64 {
    2.0 * 3.14 * radius
}

fn main() {
    let mut r: f64 = 0.0;
    print!("円の半径を入力: ");
    read_into::<f64>(&mut r);
    println!("円周のの大きさは{:.2}です。", circumeference(r));
}
''', m={
    155: dict(bug=[("read_into::<f64>(&mut r);", "read_into::<f64>(&mut circumeference);")]),
    156: dict(bug=[("circumeference(r));", "circumeference);")]),
})

S["pro1/ex/ex1-1.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    let mut z: i32 = 0;
    let avg: i32;
    println!("3つの整数を入力してください");
    read_into::<i32>(&mut x);
    read_into::<i32>(&mut y);
    read_into::<i32>(&mut z);
    avg = (x + y + z) / 3;
    println!("平均は{avg}です");
}
''', m={
    82: dict(bug=[("    avg = (x + y + z) / 3;", "    let avg: i32 = (x + y + z) / 3;")]),
})

S["pro1/ex3/ex3-1.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 1;
    let mut max: i32 = 0;
    print!("数を入力");
    read_into::<i32>(&mut max);
    while x <= max {
        println!("{x}");
        x *= 2;
    }
}
''', stdin="40\n", m={
    45: dict(bug=[("        x *= 2;\n", "        x *= 2\n")]),
})

S["pro2/Week2/2-1.c"] = dict(base=r'''
fn main() {
    let mut i: i32 = 0;
    let mut j: i32;
    print!("整数を入力");
    read_into::<i32>(&mut i);
    j = i;
    while j >= 0 {
        println!("{j}");
        j -= 1;
    }
}
''', stdin="5\n", m={
    125: dict(bug=[("    j = i;\n    while j >= 0 {", "    while (j = i, j -= 1, j = 0) {")]),
    225: dict(bug=[("while j >= 0 {", "while j > 0 {")]),
})

S["pro2/Week2/ex2-3.c"] = dict(base=r'''
fn main() {
    let mut x: i64 = 10000000;
    let mut i: i32 = 1;
    while i < 51 {
        x += x / 10000;
        println!("{i}年後:{x}円");
        i += 1;
    }
}
''', m={
    128: dict(bug=[("    let mut x: i64 = 10000000;", "    let x = 10000000;\n    let mut x: i64 = 10000000;")],
              why="型なしのグローバル変数 x=10000000; → main の中の let x = 10000000;（同じ名前の2回目の宣言）"),
    129: dict(bug=[("    let mut x: i64 = 10000000;", "    let x = 10000000.0;\n    let mut x: i64 = 10000000;")],
              why="型なしのグローバル変数 x=10000000.0; → main の中の let x = 10000000.0;（同じ名前の2回目の宣言）"),
    130: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    131: dict(bug=[("let mut x: i64 = 10000000;", "let mut x: f64 = 10000000.0;"), ("x += x / 10000;", "x += x / 10000.0;")],
             why="%lld で double を表示 → Rust では表示はできるが、型を double のままにすると結果が整数でなくなる"),
})

S["pro2/Week3/3-1.c"] = dict(base=r'''
fn main() {
    let mut tuki: i32 = 0;
    print!("月を入力してください");
    read_into::<i32>(&mut tuki);
    if tuki > 8 && tuki < 12 {
        print!("{tuki}月は秋です。");
    } else {
        print!("{tuki}月は秋ではありません。");
    }
}
''', m={
    132: dict(bug=[('print!("{tuki}月は秋です。");', 'print!("{}月は秋です。");')]),
    133: dict(bug=[('print!("{tuki}月は秋ではありません。");', 'print!("{}月は秋ではありません。");')]),
})
