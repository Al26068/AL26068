# -*- coding: utf-8 -*-
S = {}

S["pro1/samp1-3.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    print!("数字を入力してください");
    read_into::<i32>(&mut x);
    println!("入力された値は{x}です");
    print!("2倍の値を入力してください");
    read_into::<i32>(&mut y);
    println!("入力された値は{y}です");
}
''', m={
    93: dict(bug=[('    print!("数字を入力してください");', '    pfint!("数字を入力してください")')]),
})

S["pro2/Week1/c.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 0;
    print!("整数を入力して下さい:");
    read_into::<i32>(&mut x);
    if x % 5 != 0 {
        println!("その数は5でわりきれません");
    } else {
        println!("その数は5で割り切れます");
    }
}
''', m={
    110: dict(bug=[("read_into::<i32>(&mut x);", "raed_inot::<i32>(&mut x);")]),
    111: dict(bug=[("read_into::<i32>(&mut x);", "raed_into::<i32>(&mut x);")]),
    112: dict(bug=[("read_into::<i32>(&mut x);", "read_into::<i32>();")]),
    113: dict(bug=None, why="Rust は if に { } が必須なので、{ } なしで2行目が if の外に出るミスが書けない"),
    114: dict(bug=[("\nfn main() {", "\nfm main() {")]),
})

S["pro1/ex3/ex3-2.c"] = dict(base=r'''
fn main() {
    let mut i: i32 = 1;
    let mut max: i32 = 0;
    println!("数を入力してください");
    read_into::<i32>(&mut max);
    while i <= max {
        if max % i == 0 {
            println!("{i}");
        }
        i += 1;
    }
}
''', stdin="12\n", m={
    197: dict(bug=[("while i <= max {", "while i == 100 {")]),
})

S["pro1/ex4/ex4-1.c"] = dict(base=r'''
fn main() {
    let mut i: i32;
    let mut max: i32 = 0;
    println!("max?");
    read_into::<i32>(&mut max);
    i = 1;
    while i <= max {
        if max % i == 0 {
            println!("{i}");
        }
        i += 1;
    }
}
''', stdin="12\n", m={
    201: dict(bug=[("while i <= max {", "while i == max {")]),
})

S["pro1/ex4/ex4-4.c"] = dict(base=r'''
fn main() {
    let mut i: i32;
    let mut j: i32;
    let mut n: i32 = 0;
    println!("n?");
    read_into::<i32>(&mut n);
    i = 1;
    while i <= n {
        j = 1;
        while j <= n {
            if i != j && i < j {
                println!("({i},{j})");
            }
            j += 1;
        }
        i += 1;
    }
}
''', stdin="4\n", m={
    59: dict(bug=[("    let mut n: i32 = 0;\n", "")]),
    60: dict(bug=[("    i = 1;\n    while i <= n {", "    while (i = 1, i <= n, i += 1) {")]),
    61: dict(bug=[('                println!("({i},{j})");\n', "                }\n")]),
    62: dict(bug=[("        i += 1;\n    }\n}\n", "        i += 1;\n    }\n")]),
})

S["pro1/samp5/samp5-3.c"] = dict(base=r'''
fn main() {
    let mut a = [0.0_f64; 365];
    let mut sum: f64;
    let mut i: usize = 0;
    while i < 365 {
        read_into::<f64>(&mut a[i]);
        i += 1;
    }
    sum = 0.0;
    i = 0;
    while i < 365 {
        sum += a[i];
        i += 1;
    }
    println!("{:.6}", sum / 365.0);
}
''', stdin="1.5\n" * 365, m={
    102: dict(bug=[("        sum += a[i];\n", "        sum = sum; a[i];\n")]),
})

S["pro2/Week4/4-1.c"] = dict(base=r'''
fn main() {
    let mut score = [0_i32; 117];
    let mut i: usize = 0;
    let mut n: i32 = 0;
    while i < 117 {
        read_into::<i32>(&mut score[i]);
        if score[i] >= 80 {
            n += 1;
        }
        i += 1;
    }
    print!("80点以上の人は{n}人です");
}
''', stdin="80\n90\n70\n" * 39, m={
    139: dict(bug=[("        read_into::<i32>(&mut score[i]);\n", "        read_into::<i32>(&mut score[i])\n")]),
    231: dict(bug=[("[0_i32; 117]", "[0_i32; 100]")]),
    232: dict(bug=[("if score[i] >= 80 {", "if score[i] > 80 {")]),
})

S["pro1/ex2/ex2-1.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    println!("xの値を入力");
    println!("yの値を入力");
    read_into::<i32>(&mut x);
    read_into::<i32>(&mut y);
    if x > y {
        print!("大きい値は{x}です");
    } else {
        print!("大きい値は{y}です");
    }
}
''', m={
    33: dict(bug=[("read_into::<i32>(&mut x);", "read_into::<i32>(x);")]),
    34: dict(bug=[("read_into::<i32>(&mut y);", "read_into::<i32>(y);")]),
})

S["pro1/ex3/ex3-3.c"] = dict(base=r'''
fn main() {
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    println!("2つの異なる数を入力してください");
    read_into::<i32>(&mut x);
    read_into::<i32>(&mut y);
    while x == y {
        print!("同じ数です、2つの異なる数を入力してください");
        read_into::<i32>(&mut x);
        read_into::<i32>(&mut y);
    }
    print!("{x}と{y}が入力されました");
}
''', stdin="3\n3\n4\n5\n", m={
    198: dict(bug=[("while x == y {", "while x != y {")]),
})

S["pro1/samp1-4.c"] = dict(base=r'''
fn main() {
    // ガチャガチャの関数
    let atari: i32 = 3;
    let mut x: i32 = 0;
    print!("1から10までの数字を入力してください");
    read_into::<i32>(&mut x);
    if x == atari {
        println!("当たりです");
    } else {
        println!("はずれです");
    }
}
''', m={
    94: dict(bug=[('        println!("はずれです");\n    }\n}\n', '        println!("はずれです");\n    }\n')]),
})

S["pro1/ex6/ex6-1.c"] = dict(base=r'''
fn triangle(x: f64, y: f64) -> f64 {
    let s: f64 = x * y * 0.5;
    s
}

fn main() {
    let mut x: f64 = 0.0;
    let mut y: f64 = 0.0;
    print!("底辺?");
    read_into::<f64>(&mut x);
    print!("高さ？");
    read_into::<f64>(&mut y);
    println!("三角形の面積は{:.6}", triangle(x, y));
}
''', m={
    76: dict(bug=[("    let s: f64 = x * y * 0.5;", "    let x: f64;\n    let y: f64;\n    let s: f64 = x * y * 0.5;")]),
})

S["pro2/Week2/2-2.c"] = dict(base=r'''
fn main() {
    let mut i: i32;
    let mut n: i32 = 0;
    print!("正の整数を入力してください");
    read_into::<i32>(&mut n);
    print!("{n}約数を小さい順に列挙すると、");
    i = 1;
    while i < n {
        if n % i == 0 {
            print!("{i},");
        }
        i += 1;
    }
    print!("{n}");
    print!("である。");
}
''', stdin="12\n", m={
    226: dict(ctx=[("while i < n {", "while i <= n {"), ('    print!("{n}");\n', "")],
              bug=[("while i <= n {", "while i < n {")]),
})
