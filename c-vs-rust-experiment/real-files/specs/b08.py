# -*- coding: utf-8 -*-
# 追加ルール：Rust の予約語と同じ変数名（in など）は後ろに _ を付ける。
S = {}

S["pro1/ex2/Challenge2-A.c"] = dict(base=r'''
fn main() {
    let mut dest: i32 = 0;
    let mut in_: i32 = 0;
    let mut cost: i32 = 0;
    let mut ret: i32 = 0;
    let mut a: i32 = 0;
    let mut b: i32 = 0;
    let mut c: i32 = 0;
    let mut d: i32 = 0;
    let mut e: i32 = 0;
    let mut f: i32 = 0;
    let mut g: i32 = 0;
    let mut h: i32 = 0;
    let mut i: i32 = 0;
    let mut j: i32 = 0;
    let mut k: i32 = 0;
    println!("行先\n土呂-->1\n大宮-->2\n新都心-->3\n浦和-->4\n赤羽-->5\n尾久-->6\n上野-->7");
    read_into::<i32>(&mut dest);

    if dest == 1 {
        cost = 150;
    } else if dest == 2 {
        cost = 190;
    } else if dest == 3 {
        cost = 200;
    } else if dest == 4 {
        cost = 240;
    } else if dest == 5 {
        cost = 420;
    } else if dest == 6 {
        cost = 510;
    } else if dest == 7 {
        cost = 590;
    }
    print!("料金は{cost}です。投入金額を入力\n1000-->");
    read_into::<i32>(&mut a);
    print!("500-->");
    read_into::<i32>(&mut b);
    print!("100-->");
    read_into::<i32>(&mut c);
    print!("50-->");
    read_into::<i32>(&mut d);
    print!("10-->");
    read_into::<i32>(&mut e);

    in_ = 1000 * a + 500 * b + 100 * c + 50 * d + 10 * e;
    ret = in_ - cost;
    if ret / 1000 > 0 {
        f = ret / 1000;
        ret -= f * 1000;
    }
    if ret / 500 > 0 {
        g = ret / 500;
        ret -= g * 500;
    }
    if ret / 100 > 0 {
        h = ret / 100;
        ret -= h * 100;
    }
    if ret / 50 > 0 {
        i = ret / 50;
        ret -= i * 50;
    }
    if ret / 10 > 0 {
        j = ret / 10;
        ret -= j * 10;
    }
    print!("釣銭\n1000-->{f}\n500-->{g}\n100-->{h}\n50-->{i}\n10-->{j}");
}
''', stdin="3\n1\n0\n0\n1\n3\n", extra="最終版にも printf(\"500-->\",cost) のような余分な引数が残っていた（Rust ではコンパイルエラーになるので外して書いた）", m={
    16: dict(bug=[("read_into::<i32>(&mut dest);", "read_into::<i32>(dest);")]),
    17: dict(bug=[("read_into::<i32>(&mut a);", "read_into::<i32>(a);")]),
    18: dict(bug=[("read_into::<i32>(&mut b);", "read_into::<i32>(b);")]),
    19: dict(bug=[("read_into::<i32>(&mut c);", "read_into::<i32>(c);")]),
    20: dict(bug=[("read_into::<i32>(&mut d);", "read_into::<i32>(d);")]),
    21: dict(bug=[("read_into::<i32>(&mut e);", "read_into::<i32>(e);")]),
    22: dict(bug=[("""    let mut dest: i32 = 0;
    let mut in_: i32 = 0;
    let mut cost: i32 = 0;
    let mut ret: i32 = 0;
    let mut a: i32 = 0;
    let mut b: i32 = 0;
    let mut c: i32 = 0;
    let mut d: i32 = 0;
    let mut e: i32 = 0;
    let mut f: i32 = 0;
    let mut g: i32 = 0;
    let mut h: i32 = 0;
    let mut i: i32 = 0;
    let mut j: i32 = 0;
    let mut k: i32 = 0;
""", """    let mut dest: i32;
    let mut in_: i32;
    let mut cost: i32;
    let mut ret: i32;
    let mut a: i32;
    let mut b: i32;
    let mut c: i32;
    let mut d: i32;
    let mut e: i32;
    let mut f: i32;
    let mut g: i32;
    let mut h: i32;
    let mut i: i32;
    let mut j: i32;
    let mut k: i32;
    let _ = (dest, in_, cost, ret, a, b, c, d, e, f, g, h, i, j, k = 0);
""")]),
    188: dict(bug=[("50 * d + 10 * e;", "50 * d + 10 + e;")]),
    189: dict(bug=[("        ret -= h * 100;", "        ret -= h * 500;")]),
    190: dict(bug=[("        ret -= j * 10;", "        ret -= i * 10;")]),
    191: dict(bug=[("    ret = in_ - cost;", "    ret = cost - in_;")]),
})

S["pro1/ex2/Challenge2-B.c"] = dict(base=r'''
fn main() {
    let mut x1: f64 = 0.0;
    let mut y1: f64 = 0.0;
    let mut x2: f64 = 0.0;
    let mut y2: f64 = 0.0;
    let a: f64;
    let mut b: f64;
    let dy: f64;
    let dx: f64;
    println!("P0の座標を入力");
    read_into::<f64>(&mut x1);
    read_into::<f64>(&mut y1);
    println!("P1の座標を入力");
    read_into::<f64>(&mut x2);
    read_into::<f64>(&mut y2);
    dy = y2 - y1;
    dx = x2 - x1;
    a = dy / dx;
    print!("\n{a:.6}");
    if a == 0.0 {
        b = y1;
        print!("関数はY={b:.6}です");
    }
    if dx == 0.0 {
        print!("関数はx={x1:.6}です");
    }
    if dy == 0.0 {
        print!("関数はy={y1:.6}です");
    }
    b = y2 - a * x2;
    if b < 0.0 {
        print!("関数はY={a:.6}X{b:.6}です");
    } else if b > 0.0 {
        print!("関数はY={:.6}X+{:.6}  または、 y={:.6}*(x-{:.6})+{:.6}", a, b, a, x1, y1);
    } else {
        print!("関数はY={a:.6}Xです");
    }
}
''', stdin="1\n2\n3\n8\n", m={
    23: dict(bug=[("\nfn main() {", "\nuse;\n\nfn main() {")]),
    24: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    25: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    26: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    27: dict(bug=None, why="printf の %d → Rust の {} は型を書かないので、型の食い違いが書けない"),
    28: dict(ctx=[("    b = y2 - a * x2;", "    b = y2 - a * y1;")], bug=[("    b = y2 - a * y1;", "    b = {y2 - (a * y1)};")]),
    192: dict(bug=[("    read_into::<f64>(&mut x2);", "    read_into::<f64>(&mut x1);")]),
    193: dict(bug=[("    b = y2 - a * x2;", "    b = y2 - a * y1;")]),
})

# 最終版の下半分は ChatGPT のコードなので、自分が書いた上半分（コメントアウトされた版）を元にした
S["pro1/ex2/Challenge2-C.c"] = dict(base=r'''
fn main() {
    let mut p1: f64 = 0.0;
    let mut p2: f64 = 0.0;
    let mut q1: f64 = 0.0;
    let mut q2: f64 = 0.0;
    let mut x1: f64 = 0.0;
    let mut x2: f64 = 0.0;
    let mut y1: f64 = 0.0;
    let mut y2: f64 = 0.0;
    let a1: f64;
    let a2: f64;
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
    dq = q2 - q1;
    dp = p2 - p1;
    dx = x2 - x1;
    dy = y2 - y1;
    if dp == 0.0 || dq == 0.0 || dx == 0.0 || dy == 0.0 {
        print!("交差する");
    }
    a1 = dq / dp;
    a2 = dy / dx;
    if a1 != a2 {
        print!("交差する");
    } else {
        print!("交差しない");
    }
}
''', m={
    29: dict(bug=[("|| dy == 0.0 {", "|| dy = 0.0 {")]),
})
