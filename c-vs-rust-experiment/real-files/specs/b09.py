# -*- coding: utf-8 -*-
S = {}
_b05 = {}
exec(open("specs/b05.py", encoding="utf-8").read(), _b05)
CLIB = _b05["CLIB"]

S["pro1/ex3/Challenge3-B.c"] = dict(base=r'''
fn main() {
    let mut tutu = [0_i32; 5];
    let mut zaiko = [0_i32; 5];
    let mut uketori = [0_i32; 5];
    let mut oturi = [0_i32; 5];
    let azukari: i32;
    let mut bangou: i32 = 0;
    let mut okaeshi: i32 = 0;
    let mut hituyou: i32;
    let mut i: usize;
    let mut turiari: i32 = 0;
    i = 0;
    while i < 5 {
        zaiko[i] = 4;
        tutu[i] = 5;
        oturi[i] = 0;
        i += 1;
    }
    let okane: [i32; 5] = [1000, 500, 100, 50, 10];

    let syouhin: [&str; 5] = ["1 麦茶:120円", "2 緑茶:130円", "3 珈琲:140円", "4 紅茶;150円", "5 牛乳:160円"];
    let nedan: [i32; 5] = [120, 130, 140, 150, 160];

    i = 0;
    while i < 5 {
        println!("{} {} ", syouhin[i], zaiko[i]);
        i += 1;
    }

    println!("お金を入れてください\n 1000円-->\n500円-->\n100円-->\n50円-->\n10円-->");
    i = 0;
    while i < 5 {
        read_into::<i32>(&mut uketori[i]);
        tutu[i] += uketori[i];
        if tutu[i] > 10 {
            oturi[i] = tutu[i] - 10;
        }
        i += 1;
    }
    let turi = 0;

    i = 0;
    while i < 5 {
        if oturi[i] > 0 {
            turiari = 1;
        }
        i += 1;
    }
    if turiari == 1 {
        println!("すでに筒がいっぱいです,お返しします.\n1000円-->{}\n500円-->{}\n100円-->{}\n50円-->{}\n10円-->{}", oturi[0], oturi[1], oturi[2], oturi[3], oturi[4]);
        i = 0;
        while i < 5 {
            uketori[i] -= oturi[i];
            i += 1;
        }
        i = 0;
        while i < 5 {
            oturi[i] = 0;
            i += 1;
        }
    }
    azukari = 1000 * uketori[0] + 500 * uketori[1] + 100 * uketori[2] + 50 * uketori[3] + 10 * uketori[4];
    print!("お預かりは{azukari}円です\n買える商品は以下です");
    i = 0;
    while i < 5 {
        if nedan[i] < azukari {
            println!("{}", syouhin[i]);
        }
        i += 1;
    }
    print!("購入番号を入力してください");
    read_into::<i32>(&mut bangou);
    bangou -= 1;
    if bangou >= 6 {
        print!("番号がエラーです");
    }
    i = 0;
    while i < 5 {
        if bangou == i as i32 {
            okaeshi = azukari - nedan[i];
        }
        i += 1;
    }
    if okaeshi == 0 {
        print!("商品はこちらです(ガタッ)");
        zaiko[bangou as usize] -= 1;
    }

    i = 0;
    while i < 5 {
        hituyou = okaeshi / okane[i];
        if hituyou > tutu[i] {
            oturi[i] = tutu[i];
        } else {
            oturi[i] = hituyou;
        }
        okaeshi -= oturi[i] * okane[i];
        i += 1;
    }
    if okaeshi == 0 {
        println!("商品とおつりです\nおつりは{}円です", 1000 * oturi[0] + 500 * oturi[1] + 100 * oturi[2] + 50 * oturi[3] + 10 * oturi[4]);
        println!("1000円-->{}\n500円-->{}\n100円-->{}\n50円-->{}\n10円-->{}", oturi[0], oturi[1], oturi[2], oturi[3], oturi[4]);
        zaiko[bangou as usize] -= 1;
    } else {
        print!("おつりにトラブルが発生しました。残念に思います。");
        println!("お金をお返しします(チャリン)");
    }
}
''', stdin="0\n0\n2\n0\n0\n3\n", extra="最終版の okaeshi は番号が範囲外のとき初期化されないまま使われていた（Rust では 0 で初期化しないと通らない）", m={
    36: dict(bug=[('        println!("{} {} ", syouhin[i], zaiko[i]);', '        print!("{}", syouhin[])')]),
    37: dict(bug=[("    let okane: [i32; 5] = [1000, 500, 100, 50, 10];", "    let okane: [i32; i] = [1000, 500, 100, 50, 10];")]),
    38: dict(bug=[("    let mut hituyou: i32;\n", "    let mut hituyou: i32;\n    let ;\n")]),
    39: dict(bug=[('        println!("お金をお返しします(チャリン)");\n    }\n}\n', '        println!("お金をお返しします(チャリン)");\n    }\n')]),
    40: dict(bug=[("    let okane: [i32; 5] = [1000, 500, 100, 50, 10];", "    let okane: [i32; 5] [1000, 500, 100, 50, 10];")]),
    41: dict(bug=[("    let okane: [i32; 5] = [1000, 500, 100, 50, 10];", '    let okane: [i32; 5] = ["1000", "500", "100", "50", "10"];')]),
    42: dict(bug=[("    let mut tutu = [0_i32; 5];\n", "    let mut tutu = [0_i32; 5];\n    let okane = [0_i32; 5];\n")]),
    43: dict(bug=[('        println!("お金をお返しします(チャリン)");\n    }\n}\n', '        println!("お金をお返しします(チャリン)");\n    }\n    prinft!("{},{},{},{},{}", azukari, turiari, bangou, okaeshi, hituyou);\n}\n')]),
    44: dict(bug=[("    if turiari == 1 {", "    if turiari = 1 {")]),
    194: dict(bug=[("    i = 0;\n    while i < 5 {\n        read_into::<i32>(&mut uketori[i]);", "    i = 0;\n    while i < 4 {\n        read_into::<i32>(&mut uketori[i]);")]),
    195: dict(bug=[("        if nedan[i] < azukari {", "        if nedan[i] > azukari {")]),
    196: dict(ctx=[("    i = 0;\n    while i < 5 {\n        println!(\"{} {} \", syouhin[i], zaiko[i]);",
                   "    while zaiko[0] > 0 || zaiko[1] > 0 || zaiko[2] > 0 || zaiko[3] > 0 || zaiko[4] > 0 {\n    i = 0;\n    while i < 5 {\n        println!(\"{} {} \", syouhin[i], zaiko[i]);"),
                  ('        println!("お金をお返しします(チャリン)");\n    }\n}\n', '        println!("お金をお返しします(チャリン)");\n    }\n    break;\n    }\n}\n')],
              bug=[("    while zaiko[0] > 0 || zaiko[1] > 0 || zaiko[2] > 0 || zaiko[3] > 0 || zaiko[4] > 0 {",
                    "    while zaiko[0] == 0 && zaiko[1] == 0 && zaiko[2] == 0 && zaiko[3] == 0 && zaiko[4] == 0 {")]),
})

S["pro1/ex3/ex3-5.c"] = dict(pre=CLIB, base=r'''
fn main() {
    let mut x: i32;
    let mut y: i32;
    let mut z: i32;
    let mut moji: i32 = 0;
    let mut hiku: i32 = 0;
    let crand: i32 = 0;
    let mut p0: i32;
    let mut c0: i32;
    x = 5;
    y = 7;
    z = 9;
    p0 = 0;
    c0 = 0;

    while x != 0 || y != 0 || z != 0 {
        println!("現在のx,y,zの値はx={},y={},z={}です。引きたい文字を選んでください.", x, y, z);
        read_into::<i32>(&mut moji);
        if moji == 1 && x > 0 {
            println!("引く数を選んでください");
            read_into::<i32>(&mut hiku);
            x -= hiku;

            if x <= 0 {
                println!("xが0になりました");
                if x == 0 && y == 0 && z == 0 {
                    print!("ユーザーの勝利です！");
                    break;
                }
            }
            if x > 0 {
                srand(time() as u32);
                let crand = rand() % x + 1;
                x -= crand;
                if x <= 0 {
                    println!("x=0になりました。");
                    if x == 0 && y == 0 && z == 0 {
                        print!("comの勝利です");
                        break;
                    }
                }
            }

            println!("COMは{}を引きました現在のxは{}です", crand, x);
        } else if moji == 1 && x <= 0 {
            print!("すでにxは０です。別の文字を入力してください。");
        } else if moji == 2 && y > 0 {
            println!("引く数を選んでください");
            read_into::<i32>(&mut hiku);
            y -= hiku;

            if y <= 0 {
                println!("yが0になりました！");
                if x == 0 && y == 0 && z == 0 {
                    print!("ユーザーの勝利です！");
                    break;
                }
            }
            if y > 0 {
                srand(time() as u32);
                let crand = rand() % y + 1;
                y -= crand;
                if y <= 0 {
                    println!("COMは{}を引きました現在のy={}です", crand, y);
                    if x == 0 && y == 0 && z == 0 {
                        print!("comの勝利です");
                        break;
                    }
                }
            }
        } else if moji == 2 && y <= 0 {
            println!("すでにxは０です。別の文字を入力してください。");
        } else if moji == 3 && z > 0 {
            println!("引く数を選んでください");
            read_into::<i32>(&mut hiku);
            z -= hiku;

            if z <= 0 {
                println!("zが0になりました！");
                p0 += 1;
                if x == 0 && y == 0 && z == 0 {
                    print!("ユーザーの勝利です！");
                    break;
                }
            }
            if z > 0 {
                srand(time() as u32);
                let crand = rand() % z + 1;
                z -= crand;
                println!("COMは{}を引きました現在のz={}です", crand, z);
                if z <= 0 {
                    println!("z=0になりました。");
                    c0 += 1;
                    if x == 0 && y == 0 && z == 0 {
                        print!("comの勝利です");
                        break;
                    }
                }
            }
        } else if moji == 3 && z <= 0 {
            println!("すでにzは０です。別の文字を入力してください。");
        }
    }
}
''', extra="最終版でも x の分岐の最後の printf が、初期化されていない外側の crand を表示していた（Rust では 0 で初期化しないと通らない）", m={
    47: dict(bug=[("                    c0 += 1;\n", "                    cwin += 1;\n")]),
    48: dict(bug=[("                    c0 += 1;\n", "                    c0 += 1;\n                }\n")]),
})
