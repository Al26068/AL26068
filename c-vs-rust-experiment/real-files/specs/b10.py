# -*- coding: utf-8 -*-
S = {}
_b05 = {}
exec(open("specs/b05.py", encoding="utf-8").read(), _b05)
CLIB = _b05["CLIB"]

S["pro1/samp3/samp3-5.c"] = dict(pre=CLIB, base=r'''
fn main() {
    let mut x: i32;
    let mut y: i32;
    let mut z: i32;
    let mut moji: i32 = 0;
    let mut hiku: i32 = 0;
    let crand: i32 = 0;
    let mut pwin: i32;
    let mut cwin: i32;
    x = 5;
    y = 7;
    z = 9;
    pwin = 0;
    cwin = 0;

    while x != 0 || y != 0 || z != 0 {
        println!("現在のx,y,zの値はx={},y={},z={}です。引きたい文字を選んでください.", x, y, z);
        read_into::<i32>(&mut moji);
        if moji == 1 && x > 0 {
            print!("引く数を選んでください");
            read_into::<i32>(&mut hiku);
            x -= hiku;

            if x <= 0 {
                print!("おめでとうございますxが0になりました！");
                pwin += 1;
            }
            if x > 0 {
                srand(time() as u32);
                let crand = rand() % x + 1;
                x -= crand;
            }

            if x <= 0 {
                print!("残念ですx=0になりました。コンピューターの勝ちです。");
                cwin += 1;
            }
            print!("COMは{}を引きました現在のxは{}です", crand, x);
        } else if moji == 1 && x <= 0 {
            print!("すでにxは０です。別の文字を入力してください。");
        } else if moji == 2 && y > 0 {
            print!("引く数を選んでください");
            read_into::<i32>(&mut hiku);
            y -= hiku;

            if y <= 0 {
                print!("おめでとうございますyが0になりました！");
                pwin += 1;
            }
            if y > 0 {
                srand(time() as u32);
                let crand = rand() % y + 1;
                y -= crand;
            }
            if y <= 0 {
                println!("COMは{}を引きました現在のy={}です", crand, y);
                print!("残念ですy=0になりました。コンピューターの勝ちです。");
                cwin += 1;
            }
            print!("COMは{}を引きました現在のy={}です", crand, y);
        } else if moji == 2 && y <= 0 {
            print!("すでにxは０です。別の文字を入力してください。");
        } else if moji == 3 && z > 0 {
            print!("引く数を選んでください");
            read_into::<i32>(&mut hiku);
            z -= hiku;

            if z <= 0 {
                print!("おめでとうございますzが0になりました！");
                pwin += 1;
            }
            if z > 0 {
                srand(time() as u32);
                let crand = rand() % z + 1;
                z -= crand;
            }
            if z <= 0 {
                println!("COMは{}を引きました現在のz={}です", crand, z);
                print!("残念ですz=0になりました。コンピューターの勝ちです。");
                cwin += 1;
            }
            print!("COMは{}を引きました現在のz={}です", crand, z);
        } else if moji == 3 && z <= 0 {
            print!("すでにzは０です。別の文字を入力してください。");
        }
    }
    if cwin > pwin {
        print!("comの勝ちです。対戦ありがとうございました");
    } else {
        print!("おめでとうございます。プレイヤーの勝利です");
    }
}
''', stdin="1\n5\n2\n7\n3\n9\n" * 5, extra="最終版でも COM が引いた数の表示が、初期化されていない外側の crand を使っていた（Rust では 0 で初期化しないと通らない）", m={
    100: dict(bug=[("        } else if moji == 3 && z > 0 {", "        } else if moji = 3 {")]),
    101: dict(bug=[("        read_into::<i32>(&mut moji);", "        read_into::<i32>(moji);")]),
    218: dict(bug=[('            if y <= 0 {\n                print!("おめでとうございますyが0になりました！");', '            if x <= 0 {\n                print!("おめでとうございますyが0になりました！");')]),
    219: dict(bug=[("            read_into::<i32>(&mut hiku);\n            y -= hiku;", "            read_into::<i32>(&mut hiku);\n            x -= hiku;")]),
})

S["pro2/Week5/ex5-1.c"] = dict(base=r'''
fn fibonachi(n: i32) -> i32 {
    let mut i: i32;
    let mut fn_ = [0_i32; 3];
    // fn[0]=fn
    // fn[1]=f(n-1)
    // fn[2]=f(n-2)
    if n == 0 {
        print!("F(0)=0");
        return 0;
    }

    if n == 1 {
        print!("F(1)=1");
        return 1;
    }

    if n >= 2 {
        fn_[1] = 1;
        fn_[2] = 0;
        i = 1;
        while i <= n {
            fn_[0] = fn_[1] + fn_[2];
            fn_[2] = fn_[1];
            fn_[1] = fn_[0];
            i += 1;
        }
    }
    fn_[0]
}

fn main() {
    let mut n: i32 = 0;
    print!("0以上の整数を入力:");
    read_into::<i32>(&mut n);
    if n == 0 {
        print!("F(0)=0");
    } else if n == 1 {
        print!("F(1)=1");
    } else {
        print!("F({})={}", n, fibonachi(n));
    }
}
''', stdin="10\n", m={
    159: dict(bug=[("        i = 1;\n        while i <= n {", "        while (i = 0, i < n, i += 1) {")]),
    160: dict(bug=[("    fn_[0]\n}", "    fn_\n}")]),
    161: dict(bug=[("    if n == 0 {\n        print!(\"F(0)=0\");\n        return 0;", "    if n = 0 {\n        print!(\"F(0)=0\");\n        return 0;")]),
    162: dict(bug=[("    if n == 1 {\n        print!(\"F(1)=1\");\n        return 1;", "    if n = 1 {\n        print!(\"F(1)=1\");\n        return 1;")]),
    163: dict(bug=[("    read_into::<i32>(&mut n);", "    read_itno::<i32>(&mut n);")]),
    164: dict(bug=[("        while i <= n {", "        while i < n = n {")]),
})
