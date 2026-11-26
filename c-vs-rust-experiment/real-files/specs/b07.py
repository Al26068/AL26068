# -*- coding: utf-8 -*-
# 追加ルール：C のグローバル変数は自動で 0 になるので、Rust でも 0 で初期化した変数にする。
# 戻り値を返し忘れている関数など、ミス一覧にない「最終版に残っていた問題」は、Rust では通らないので直して書く（別に記録）。
S = {}
from_b05 = {}
exec(open("specs/b05.py", encoding="utf-8").read(), from_b05)
CLIB = from_b05["CLIB"]

S["pro1/ex6/ex6-4.c"] = dict(base=r'''
fn read_positive() -> i32 {
    let mut z: i32;
    z = -1;
    while z < 0 {
        print!("正の数を入力してください。");
        read_into::<i32>(&mut z);
    }
    z
}

fn gcd(mut x: i32, mut y: i32) -> i32 {
    let mut r: i32;
    while y != 0 {
        r = x % y;
        x = y;
        y = r;
    }
    x
}

fn main() {
    let x: i32;
    let y: i32;
    print!("x?");
    x = read_positive();
    print!("y?");
    y = read_positive();
    println!("gcd({},{})={}", x, y, gcd(x, y));
}
''', stdin="12\n18\n", extra="最終版の read_positive は return z; が抜けていた（C は通るが、Rust では値を返さない関数はコンパイルエラーになる）", m={
    77: dict(bug=[('    print!("y?");', '    pirnt!("y?");')]),
    78: dict(bug=[("    while y != 0 {", "    while (r == 0) {")]),
    214: dict(bug=[("    while z < 0 {", "    while z <= 0 {")]),
})

S["pro2/Week2/ex2-1.c"] = dict(base=r'''
fn main() {
    let mut a: i32 = 0;
    let mut b: i32 = 0;
    let mut i: i32;
    let mut j: i32;
    let mut g: i32 = 0;
    let c: i32 = 0;
    let d: i32;
    let mut n: i32 = 0;
    let mut x = [0_i32; 1000];
    let mut y = [0_i32; 1000];
    println!("正の整数を入力してください");
    println!("正の整数を入力してください");
    read_into::<i32>(&mut a);
    read_into::<i32>(&mut b);

    i = 1;
    while i <= a {
        if a % i == 0 {
            x[n as usize] = i;
            n += 1;
        }
        i += 1;
    }
    let na = n;
    n = 0;
    i = 1;
    while i <= b {
        if b % i == 0 {
            y[n as usize] = i;
            n += 1;
        }
        i += 1;
    }
    let nb = n;

    i = 0;
    while i < na {
        j = 0;
        while j < nb {
            if x[i as usize] == y[j as usize] {
                g = x[i as usize];
            }
            j += 1;
        }
        i += 1;
    }
    d = a / g * b;
    println!("最小公倍数は{d}");
}
''', stdin="12\n18\n", m={
    126: dict(bug=None, why="型なしのグローバル変数 n=0; → main の中の let mut n = 0; は Rust では型推論で正しく動く"),
    227: dict(bug=[("    d = a / g * b;", "    d = g * b * c;")]),
})

S["pro2/Week4/ex4-4.c"] = dict(base=r'''
fn main() {
    let mut a = [[0_i32; 2]; 2];
    let mut n: i32 = 0;
    let mut i: i32;
    let mut p = [[0_i32; 2]; 2];
    let mut t = [[0_i32; 2]; 2];
    p[0][0] = 1;
    p[0][1] = 0;
    p[1][0] = 0;
    p[1][1] = 1;

    println!("行列aを入力してください");
    print!("a[0][0]=");
    read_into::<i32>(&mut a[0][0]);
    print!("a[0][1]=");
    read_into::<i32>(&mut a[0][1]);
    print!("a[1][0]=");
    read_into::<i32>(&mut a[1][0]);
    print!("a[1][1]=");
    read_into::<i32>(&mut a[1][1]);
    print!("何乗しますか:");
    read_into::<i32>(&mut n);
    i = 0;
    while i < n {
        t[0][0] = p[0][0];
        t[0][1] = p[0][1];
        t[1][0] = p[1][0];
        t[1][1] = p[1][1];
        p[0][0] = t[0][0] * a[0][0] + t[0][1] * a[1][0];
        p[0][1] = t[0][0] * a[0][1] + t[0][1] * a[1][1];
        p[1][0] = t[1][0] * a[0][0] + t[1][1] * a[1][0];
        p[1][1] = t[1][0] * a[0][1] + t[1][1] * a[1][1];
        i += 1;
    }

    print!("行列aの{n}乗は");
    println!("p[0][0]={}", p[0][0]);
    println!("p[0][1]={}", p[0][1]);
    println!("p[1][0]={}", p[1][0]);
    println!("p[1][1]={}", p[1][1]);
}
''', stdin="1\n2\n3\n4\n3\n", m={
    153: dict(bug=[("    p[0][0] = 1;\n", "    let p[0][0] = 1;\n")]),
    236: dict(ctx=[("    i = 0;\n    while i < n {", "    p = a;\n    i = 0;\n    while i < n - 1 {")],
              bug=[("    while i < n - 1 {", "    while i < n {")]),
    237: dict(bug=[("    p[1][1] = 1;\n", "    p[1][0] = 1;\n")]),
    238: dict(bug=[("p[1][1] = t[1][0] * a[0][1] + t[1][1] * a[1][1];", "p[1][1] = t[1][0] * a[1][0] + t[1][1] * a[1][1];")]),
})

S["pro1/ex3/ex3-4.c"] = dict(pre=CLIB, base=r'''
fn main() {
    let answer: i32;
    srand(time() as u32);
    answer = (f64::from(rand()) / (f64::from(RAND_MAX) + 1.0) * 1000.0) as i32;
    let mut x: i32 = 0;
    let mut i: i32;
    i = 1;
    print!("いくつだと思いますか？");
    read_into::<i32>(&mut x);
    while x != answer {
        if x > answer {
            if x >= answer + 100 {
                println!("とても大きい");
                i += 1;
            } else if x >= answer + 10 {
                println!("大きい");
                i += 1;
            } else {
                println!("少し大きい");
                i += 1;
            }
        }
        if x < answer {
            if x <= answer - 100 {
                println!("とても小きい");
                i += 1;
            } else if x <= answer - 10 {
                println!("小さい");
                i += 1;
            } else {
                println!("少し小さい");
                i += 1;
            }
        }
        print!("いくつだと思いますか？");
        read_into::<i32>(&mut x);
    }
    print!("あたりです{i}回でできました！");
}
''', m={
    46: dict(bug=[('    print!("あたりです{i}回でできました！");\n}\n', '    print!("あたりです{i}回でできました！");\n')]),
    199: dict(bug=[("    i = 1;\n", "    i = 0;\n")]),
    200: dict(bug=None, exclude=True, why="見直したらミスではなかった（整数では x>answer+9 と x>=answer+10 は同じ意味）"),
})

S["pro1/ex2/Challenge2-C#.c"] = dict(base=r'''
fn main() {
    let a: f64;
    let b: f64;
    let c: f64;
    let d: f64;
    let e: f64;
    let mut p1: f64 = 0.0;
    let mut p2: f64 = 0.0;
    let mut q1: f64 = 0.0;
    let mut q2: f64 = 0.0;
    let mut x1: f64 = 0.0;
    let mut x2: f64 = 0.0;
    let mut y1: f64 = 0.0;
    let mut y2: f64 = 0.0;
    let dp: f64;
    let dq: f64;
    let dx: f64;
    let dy: f64;
    println!("P0の座標を入力");
    read_into::<f64>(&mut p1);
    read_into::<f64>(&mut q1);
    println!("P1の座標を入力");
    read_into::<f64>(&mut p2);
    read_into::<f64>(&mut q2);
    println!("Q0の座標を入力");
    read_into::<f64>(&mut x1);
    read_into::<f64>(&mut y1);
    println!("Q1の座標を入力");
    read_into::<f64>(&mut x2);
    read_into::<f64>(&mut y2);
    dy = y2 - y1;
    dx = x2 - x1;
    a = dy / dx;
    b = y2 - a * x2;
    if dx == 0.0 {
        e = x1;
        if x1 < e && x2 > e || x1 > e && x2 < e {}
    } else if (y1 > a * x1 + b && y2 < a * x2 + b) || (y1 < a * x1 + b && y2 > a * x2 + b) {
        dp = p2 - p1;
        dq = q2 - q1;
        c = dq / dp;
        d = q2 - c * p2;
        if (q1 > a * p1 + b && q2 < a * p2 + b) || (q1 < a * p1 + b && q2 > a * p2 + b) {
            print!("直交する");
        } else {
            print!("直行しない");
        }
    } else {
        print!("直交しない");
    }
}
''', stdin="0\n0\n2\n2\n0\n2\n2\n0\n",
    extra="最終版では b=y2-a*x2; が a=dy/dx; より先にあり、a を初期化前に使っていた（Rust ではコンパイルエラーになるので順番を直して書いた）", m={
    30: dict(bug=[("    let a: f64;\n", "")]),
    31: dict(bug=[("    let c: f64;\n", ""), ("        c = dq / dp;\n", "        c = dq / dp\n")]),
    32: dict(bug=[("    let mut p1: f64 = 0.0;\n", "    let mut g.h.ip1: f64 = 0.0;\n")]),
})
