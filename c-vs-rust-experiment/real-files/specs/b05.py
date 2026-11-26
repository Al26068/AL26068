# -*- coding: utf-8 -*-
# 追加ルール：stdlib.h の srand/rand/RAND_MAX と time.h の time は、同じ名前の関数を持つ小さなモジュールに置き換え、#include は use にする。
S = {}

CLIB = r'''
mod cstdlib {
    //! stdlib.h の代わり（srand / rand / RAND_MAX だけ）
    use std::cell::Cell;
    thread_local! {
        static SEED: Cell<u64> = const { Cell::new(1) };
    }
    /// 乱数の最大値
    pub const RAND_MAX: i32 = 2_147_483_647;
    /// 乱数の種を決める
    pub fn srand(s: u32) {
        SEED.with(|c| c.set(u64::from(s)));
    }
    /// 乱数を返す
    pub fn rand() -> i32 {
        SEED.with(|c| {
            let v = c.get().wrapping_mul(6_364_136_223_846_793_005).wrapping_add(1);
            c.set(v);
            ((v >> 33) % 2_147_483_648) as i32
        })
    }
}

mod ctime {
    //! time.h の代わり（time だけ）
    /// 1970年からの秒数
    pub fn time() -> u64 {
        std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .map_or(0, |d| d.as_secs())
    }
}
use ctime::time;
use cstdlib::{rand, srand, RAND_MAX};
'''

S["pro1/samp3/samp3-4.c"] = dict(pre=CLIB, base=r'''
fn main() {
    let answer: i32;
    srand(time() as u32);
    answer = (f64::from(rand()) / (f64::from(RAND_MAX) + 1.0) * 1000.0) as i32;
    let mut x: i32 = 0;
    print!("いくつだと思いますか？");
    read_into::<i32>(&mut x);
    while x != answer {
        if x > answer {
            println!("大きすぎます");
        } else {
            println!("小さすぎます");
        }
        print!("いくつだと思いますか？");
        read_into::<i32>(&mut x);
    }
    print!("あたりですよくできましたさすがです");
}
''', m={
    97: dict(bug=[('    print!("いくつだと思いますか？");\n    read_into::<i32>(&mut x);\n    while', '    prinft!("いくつだと思いますか？");\n    read_into::<i32>(&mut x);\n    while')]),
    98: dict(bug=[("use cstdlib::{rand, srand, RAND_MAX};\n", "")]),
    99: dict(bug=[("srand(time() as u32);", "srand(tiem() as u32);")]),
})

S["pro1/samp5/samp5-4.c"] = dict(base=r'''
fn main() {
    let mut a = [[0_i32; 10]; 10];
    let mut i: usize;
    let mut j: usize;

    // 9x9を計算
    i = 0;
    while i < 9 {
        j = 0;
        while j < 9 {
            a[i][j] = ((i + 1) * (j + 1)) as i32;
            j += 1;
        }
        i += 1;
    }

    // 9x9の内容を表示
    i = 0;
    while i < 9 {
        j = 0;
        while j < 9 {
            print!("{} ", a[i][j]);
            j += 1;
        }
        println!();
        i += 1;
    }
}
''', m={
    221: dict(bug=[('            print!("{} ", a[i][j]);\n            j += 1;', '            print!("{} ", a[i][j]);\n            i += 1;')]),
    222: dict(bug=None, exclude=True, why="見直したらミスではなかった（当時のループは 0〜8 で 9×9 の配列に収まっていた。本当の原因は #221 の ++i）"),
})

S["pro2/Week6/6-2.c"] = dict(base=r'''
fn average_of(seiseki: &[i32], length: i32) -> f64 {
    let mut average: i32 = 0;
    let mut i: i32 = 0;
    while i < length {
        average += seiseki[i as usize];
        i += 1;
    }
    f64::from(average) / f64::from(length)
}

fn main() {
    let mut score = [0_i32; 117];
    let average: i32;
    let mut i: usize;
    let n: i32;
    n = 0;

    i = 0;
    while i < 117 {
        read_into::<i32>(&mut score[i]);
        i += 1;
    }

    print!("平均点は{:.2}点です", average_of(&score, 117));
}
''', stdin="80\n90\n70\n" * 39, m={
    170: dict(bug=[("average_of(&score, 117));", "average(&score, 117));")]),
    171: dict(bug=[("let mut score = [0_i32; 117];", "let mut score = [0.0_f64; 117];"), ("read_into::<i32>(&mut score[i]);", "read_into::<f64>(&mut score[i]);")]),
    243: dict(bug=[("    let mut average: i32 = 0;", "    let mut average: i32;")]),
    244: dict(bug=[("    f64::from(average) / f64::from(length)", "    average / 117")]),
    245: dict(bug=[("    f64::from(average) / f64::from(length)", "    f64::from(average) / 117.0")]),
})

S["pro2/Week4/ex4-5.c"] = dict(base=r'''
fn main() {
    let mut a = [0_i32; 16];
    let mut i: i32;
    let mut x: i32 = 0;
    let n: i32;
    let mut b: i32 = 0;
    print!("1から65535までの正の整数を入力してください:");
    read_into::<i32>(&mut x);
    n = x;
    i = 0;
    while i < 16 {
        a[i as usize] = x % 2;
        x /= 2;
        i += 1;
    }
    i = 0;
    while i < 16 {
        if a[i as usize] == 1 {
            b = i;
        }
        i += 1;
    }
    print!("{n}を2進数で表記すると、");
    i = b;
    while i >= 0 {
        print!("{}", a[i as usize]);
        i -= 1;
    }
    println!("です。");
}
''', stdin="10\n", m={
    154: dict(bug=[('    print!("{n}を2進数で表記すると、");', '    print!("{}を2進数で表記すると、" n);')]),
    239: dict(bug=[('        print!("{}", a[i as usize]);', '        print!("{}", a[(16 - i) as usize]);')]),
})

S["pro2/Week6/ex6-1.c"] = dict(base=r'''
fn inner_prod(a: &[f64], b: &[f64], length: usize) -> f64 {
    let mut i: usize = 0;
    let mut prod: f64 = 0.0;
    while i < length {
        prod += a[i] * b[i];
        i += 1;
    }
    prod
}

fn main() {
    let mut i: usize;
    let mut a = [0.0_f64; 3];
    let mut b = [0.0_f64; 3];
    i = 0;
    while i < 3 {
        print!("a[{i}]=");
        read_into::<f64>(&mut a[i]);
        i += 1;
    }
    i = 0;
    while i < 3 {
        print!("b[{i}]=");
        read_into::<f64>(&mut b[i]);
        i += 1;
    }

    print!("aとbの内積は{:.2}です", inner_prod(&a, &b, 3));
}
''', m={
    172: dict(bug=[("        read_into::<f64>(&mut a[i]);\n", "        read_into::<f64>(&mut a[i])\n")]),
    173: dict(bug=[("inner_prod(&a, &b, 3)", "inner_prod(a[3], b[3], 3)")]),
    174: dict(bug=[('    i = 0;\n    while i < 3 {\n        print!("a[{i}]=");', '    while (i = 0, i < 3; i += 1) {\n        print!("a[{i}]=");')]),
    175: dict(bug=[('    i = 0;\n    while i < 3 {\n        print!("a[{i}]=");\n        read_into::<f64>(&mut a[i]);\n        i += 1;\n    }',
                    '    let _ = (i = 0, i < 3);\n    while { let t = i; i += 1; t } {\n        print!("a[{i}]=");\n        read_into::<f64>(&mut a[i]);\n    }')]),
    176: dict(bug=[("fn inner_prod(a: &[f64], b: &[f64], length: usize)", "fn inner_prod(a: &[i32], b: &[i32], length: usize)")]),
    246: dict(bug=[("    let mut prod: f64 = 0.0;", "    let mut prod: i32 = 0;")]),
})

S["pro2/Week3/3-2.c"] = dict(base=r'''
fn main() {
    let mut a: i32 = 0;
    let mut b: i32 = 0;
    let x: i32 = 1;
    let mut n: i32 = 0;
    while x == 1 {
        print!("数値を入力");
        read_into::<i32>(&mut a);
        print!("数値を入力");
        read_into::<i32>(&mut b);
        if a > b {
            if a % b == 0 {
                print!("{b}は{a}の約数です");
            } else {
                print!("{b}は{a}の約数ではありません");
            }
        } else if b % a == 0 {
            print!("{a}は{b}の約数です");
        } else {
            print!("{a}は{b}の約数ではありません");
        }
        print!("[続ける:1,終了:0]");
        read_into::<i32>(&mut n);
        if x != n {
            break;
        }
    }
}
''', stdin="12\n4\n0\n", m={
    134: dict(bug=[("read_into::<i32>(&mut a);", "read_into::<i32>(a);")]),
    135: dict(bug=[("read_into::<i32>(&mut b);", "read_into::<i32>(b);")]),
})
