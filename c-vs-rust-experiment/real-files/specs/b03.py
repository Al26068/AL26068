# -*- coding: utf-8 -*-
# 追加ルール：C で引数に代入している関数は Rust でも mut 引数、char 配列の文字列は String、
# fgets → read_line、strchr → find、strlen → len()、pow(x,y) → x.powf(y)
S = {}

S["pro2/Week3/ex3-2.c"] = dict(base=r'''
fn main() {
    // xは入力された数,yは桁数,zは1の位,10の位・・・
    let mut x: i32 = 0;
    let mut y: i32;
    let mut z: i32;
    print!("正の数を入力してください");
    read_into::<i32>(&mut x);
    y = 0;
    z = 1;
    while x % z != x && x / z > 0 {
        println!("{}の位は{}です。", z, (x / z) % 10);
        z *= 10;
        y += 1;
    }
    print!("{x}は{y}桁の数です。");
}
''', stdin="4321\n", m={
    136: dict(bug=[('    print!("{x}は{y}桁の数です。");', '    pritn!("{x}は{y}桁の数です。");')]),
    229: dict(bug=[("while x % z != x && x / z > 0 {", "while x % z != x {")], stdin="2000000000\n"),
})

S["pro1/ex5/ex5-2.c"] = dict(base=r'''
fn main() {
    let mut max: i32;
    let mut min: i32;
    let mut a = [0_i32; 10];
    let mut i: usize = 0;
    let mut j: usize;
    max = 0;
    min = 0;
    while i < 10 {
        read_into::<i32>(&mut a[i]);
        i += 1;
    }
    j = 0;
    while j < 10 {
        if a[j] > max {
            max = a[j];
        } else if a[j] < min {
            min = a[j];
        }
        j += 1;
    }
    println!("最大値は{max}\n最小値は{min}");
}
''', m={
    66: dict(bug=[("read_into::<i32>(&mut a[i]);", "read_into::<i32>(a[i]);")]),
})

S["pro1/samp6/samp6-2.c"] = dict(base=r'''
fn fact(n: i32) -> i32 {
    let mut answer: i32;
    let mut i: i32;
    answer = 1;
    i = 1;
    while i <= n {
        answer *= i;
        i += 1;
    }
    answer
}

fn main() {
    let mut n: i32 = 0;
    let mut r: i32 = 0;
    print!("n?");
    read_into::<i32>(&mut n);
    print!("r?");
    read_into::<i32>(&mut r);
    println!("nCr={}", fact(n) / fact(r) / fact(n - r));
}
''', m={
    103: dict(bug=[("    answer\n}\n", "    answer\n\n")]),
})

S["pro2/Week8/8-1.c"] = dict(base=r'''
fn main() {
    let mut moji = String::new();
    let x: usize;
    print!("英文を入力してください:");
    let _ = std::io::stdin().read_line(&mut moji);
    if let Some(p) = moji.find('\n') {
        moji.truncate(p);
    }
    x = moji.len();
    print!("あなたが入力した文字数は{x}です");
}
''', stdin="hello world\n", m={
    181: dict(bug=[("    let _ = std::io::stdin().read_line(&mut moji);\n", "    read_into::<i32>()\n    let _ = std::io::stdin().read_line(&mut moji);\n")]),
    182: dict(bug=[("read_line(&mut moji);", "read_line(&mut moji[100]);")]),
    183: dict(bug=[("    if let Some(p) = moji.find('\\n') {\n        moji.truncate(p);\n    }\n", "    stcher\n")]),
})

S["pro1/ex2/ex2-3.c"] = dict(base=r'''
fn main() {
    let mut shincho: f64 = 0.0;
    let mut taijyu: f64 = 0.0;
    let risou: f64;
    print!("身長は？");
    println!("体重は？");
    read_into::<f64>(&mut shincho);
    read_into::<f64>(&mut taijyu);
    risou = shincho * shincho * 22.0 / 10000.0;
    if taijyu > (risou + 5.0) {
        print!("甘いものを減らしましょう");
    } else if taijyu < (risou - 5.0) {
        print!("もっと食べましょう");
    } else {
        print!("その調子！");
    }
}
''', m={
    35: dict(bug=[('    println!("体重は？");', '    println!("体重は？")')]),
})

S["pro2/Week5/5-2.c"] = dict(base=r'''
fn bmi(mut height: f64, weight: f64) -> f64 {
    height /= 100.0;
    weight / height.powf(2.0)
}

fn main() {
    let mut height: f64 = 0.0;
    let mut weight: f64 = 0.0;
    println!("身長(cm): ");
    read_into::<f64>(&mut height);
    print!("体重(kg): ");
    read_into::<f64>(&mut weight);
    println!("BMIは{:.1}です。", bmi(height, weight));
}
''', m={
    157: dict(bug=[("read_into::<f64>(&mut height);", "read_into::<f64>(hight);")]),
    158: dict(bug=[("read_into::<f64>(&mut weight);", "read_into::<f64>(weight);")]),
})

S["pro2/Week6/6-1.c"] = dict(base=r'''
fn num_of_grade_a(seiseki: &[i32], length: usize) -> i32 {
    let mut count = 0;
    let mut i: usize = 0;
    while i < length {
        if seiseki[i] >= 80 {
            count += 1;
        }
        i += 1;
    }
    count
}

fn main() {
    let mut i: usize = 0;
    let mut score = [0_i32; 117];
    while i < 117 {
        read_into::<i32>(&mut score[i]);
        i += 1;
    }
    println!("80点以上の人は{}人です", num_of_grade_a(&score, 117));
}
''', stdin="80\n90\n70\n" * 39, m={
    168: dict(bug=[("    let mut score = [0_i32; 117];\n", ""), ('    println!("80点以上の人は{}人です", num_of_grade_a(&score, 117));', '    println!("80点以上の人は{}人です", num_of_grade_a(score[i], 117))')]),
    169: dict(bug=[("num_of_grade_a(&score, 117)", "num_of_grade_a(score[117], 117)")]),
})

S["pro1/ex5/ex5-1.c"] = dict(base=r'''
fn main() {
    let mut a = [0_i32; 10];
    let mut i: usize = 0;
    let mut j: usize;
    while i < 10 {
        read_into::<i32>(&mut a[i]);
        i += 1;
    }
    j = 0;
    while j < 10 {
        if a[j] > 0 {
            println!("{}は正の数です", a[j]);
        } else if a[j] < 0 {
            println!("{}は負の数です", a[j]);
        } else {
            println!("0が入力されまました");
        }
        j += 1;
    }
}
''', stdin="5\n-3\n4\n2\n1\n6\n7\n8\n9\n-10\n", m={
    65: dict(bug=[('            println!("{}は負の数です", a[j]);', '            prinltn!("{}は負の数です", a[j]);')]),
    205: dict(bug=[("    while i < 10 {\n        read_into", "    while i < 9 {\n        read_into")]),
})

S["pro1/ex6/ex6-3.c"] = dict(base=r'''
fn power(x: f64, n: i32) -> f64 {
    let mut i: i32;
    let mut ans: f64 = 1.0;
    i = 0;
    while i < n {
        ans *= x;
        i += 1;
    }
    ans
}

fn main() {
    let mut x: f64 = 0.0;
    let mut n: i32 = 0;
    print!("x?");
    read_into::<f64>(&mut x);
    print!("n?");
    read_into::<i32>(&mut n);
    print!("{:.6}の{}乗は{:.6}", x, n, power(x, n));
}
''', stdin="2\n5\n", m={
    212: dict(ctx=[("    i = 0;\n    while i < n {", "    i = 1;\n    while i < n {")],
              bug=[("    i = 1;\n    while i < n {", "    i = 1;\n    while i <= n {")]),
    213: dict(bug=[("fn power(x: f64, n: i32) -> f64 {", "fn power(mut x: f64, n: i32) -> f64 {"),
                   ("    let mut ans: f64 = 1.0;\n", ""), ("        ans *= x;\n", "        x *= x;\n"), ("    ans\n}", "    x\n}")]),
})

S["pro1/samp6/samp6-4.c"] = dict(base=r'''
fn print_binary(mut n: i32) {
    let mut a = [0_i32; 8];
    let mut i: i32 = 0;
    while i < 8 {
        a[i as usize] = n % 2;
        n /= 2;
        i += 1;
    }
    i = 7;
    while i >= 0 {
        print!("{}", a[i as usize]);
        i -= 1;
    }
}

fn main() {
    let mut x: i32 = 0;
    let mut y: i32 = 0;
    print!("x?");
    read_into::<i32>(&mut x);
    print!("y?");
    read_into::<i32>(&mut y);
    print!(" x=");
    print_binary(x);
    println!(" {x}");
    print!(" y=");
    print_binary(y);
    println!(" {y}");
    print!(" x+y=");
    print_binary(x + y);
    println!(" {}", x + y);
}
''', m={
    104: dict(bug=[('    print!(" x+y=");', '    pritn!(" x+y=");')]),
})
