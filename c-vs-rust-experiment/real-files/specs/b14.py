# -*- coding: utf-8 -*-
S = {}
_b05 = {}
exec(open("specs/b05.py", encoding="utf-8").read(), _b05)
CLIB = _b05["CLIB"]

TERMINALMODE2_INT = r'''
mod terminalmode2 {
    //! 授業のヘッダー terminalmode2.h の代わり（C と同じく座標は int）
    use std::cell::RefCell;

    /// 赤
    pub const AKA: u8 = 1;
    /// 青
    pub const AO: u8 = 2;
    /// 黄
    pub const KI: u8 = 3;
    /// 緑
    pub const MIDORI: u8 = 4;
    /// 白
    pub const SHIRO: u8 = 5;

    thread_local! {
        static CANVAS: RefCell<Vec<Vec<u8>>> = const { RefCell::new(Vec::new()) };
    }

    /// キャンバスの大きさを決める
    pub fn led_canvas_setsize(r: i32, c: i32) {
        CANVAS.with(|cv| *cv.borrow_mut() = vec![vec![0; c as usize]; r as usize]);
    }

    /// 端末の設定（ここでは何もしない）
    pub fn set_terminal_reset() {}

    /// 行の数（LED_ROW）
    pub fn led_row() -> i32 {
        CANVAS.with(|cv| cv.borrow().len() as i32)
    }

    /// 列の数（LED_COL）
    pub fn led_col() -> i32 {
        CANVAS.with(|cv| cv.borrow().first().map_or(0, Vec::len) as i32)
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
    pub fn led_canvas_set_pixel(row: i32, col: i32, color: u8) {
        CANVAS.with(|cv| cv.borrow_mut()[row as usize][col as usize] = color);
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

    /// usleep の代わり
    pub fn usleep(us: u64) {
        std::thread::sleep(std::time::Duration::from_micros(us));
    }
}
use terminalmode2::*;
'''

S["pro1/game/fireworks.c"] = dict(pre=CLIB + TERMINALMODE2_INT, base=r'''
// 地面描画
fn draw_ground() {
    let mut i: i32 = 0;
    while i <= 39 {
        led_canvas_set_pixel(18, i, MIDORI);
        led_canvas_set_pixel(19, i, MIDORI);
        i += 1;
    }
}

// 残像
fn draw_trail(start: i32, y: i32, z: i32) {
    let mut i: i32 = start;
    while i > y {
        led_canvas_set_pixel(i, z, SHIRO);
        i -= 1;
    }
}

// 近似式
fn my_isqrt(n: i32) -> i32 {
    let mut x = 0;
    while (x + 1) * (x + 1) <= n {
        x += 1;
    }
    x
}

// 大玉用（円形爆発）
fn explode_circle(y: i32, z: i32, r: i32, color: u8) {
    let mut dy: i32 = -r;
    while dy <= r {
        let dz = my_isqrt(r * r - dy * dy) * 2;
        let py = y + dy;
        let pz1 = z - dz;
        let pz2 = z + dz;
        if py >= 0 && py < led_row() {
            if pz1 >= 0 && pz1 < led_col() {
                led_canvas_set_pixel(py, pz1, color);
            }
            if pz2 >= 0 && pz2 < led_col() {
                led_canvas_set_pixel(py, pz2, color);
            }
        }
        dy += 1;
    }
}

// 爆発の形状
fn explode_shape(y: i32, z: i32, r: i32, shape: i32, color: u8) {
    if shape == 0 || shape == 2 {
        if y - r >= 0 && z - r >= 0 {
            led_canvas_set_pixel(y - r, z - r, color);
        }
        if y - r >= 0 && z + r < led_col() {
            led_canvas_set_pixel(y - r, z + r, color);
        }
        if y + r < led_row() && z - r >= 0 {
            led_canvas_set_pixel(y + r, z - r, color);
        }
        if y + r < led_row() && z + r < led_col() {
            led_canvas_set_pixel(y + r, z + r, color);
        }
    }
    if shape == 0 || shape == 1 {
        if y - r >= 0 {
            led_canvas_set_pixel(y - r, z, color);
        }
        if y + r < led_row() {
            led_canvas_set_pixel(y + r, z, color);
        }
        if z - r >= 0 {
            led_canvas_set_pixel(y, z - r, color);
        }
        if z + r < led_col() {
            led_canvas_set_pixel(y, z + r, color);
        }
    }
    if shape == 3 {
        explode_circle(y, z, r, color);
    }
}

// 打ち上げ要因
fn launch_ascend(z: i32) {
    let mut y: i32 = 19;
    while y > 5 {
        led_canvas_clear();
        draw_ground();
        draw_trail(19, y, z);
        led_canvas_set_pixel(y, z, AKA);
        led_canvas_display();
        usleep(100000);
        y -= 1;
    }
}

// 爆発要因
fn launch_explode(z: i32, shape: i32, color: u8) {
    let mut r: i32 = 1;
    while r <= 8 {
        led_canvas_clear();
        draw_ground();
        led_canvas_set_pixel(5, z, AKA);
        explode_shape(5, z, r, shape, color);
        led_canvas_display();
        usleep(50000);
        r += 1;
    }
}

// フィナーレ用
fn launch_finale_simple(fireworks_color: [u8; 4]) {
    let (z1, z2, z3) = (10, 20, 30);
    let mut y: i32;
    let mut r: i32;
    let c = (rand() % 4) as usize;

    // 3本同時上昇
    y = 19;
    while y > 5 {
        led_canvas_clear();
        draw_ground();
        draw_trail(19, y, z1);
        draw_trail(19, y, z2);
        draw_trail(19, y, z3);
        led_canvas_set_pixel(y, z1, AKA);
        led_canvas_set_pixel(y, z2, AKA);
        led_canvas_set_pixel(y, z3, AKA);
        led_canvas_display();
        usleep(100000);
        y -= 1;
    }

    // 3本同時爆発
    r = 1;
    while r <= 8 {
        led_canvas_clear();
        draw_ground();
        explode_shape(5, z1, r, 0, fireworks_color[c]);
        explode_shape(5, z2, r, 0, fireworks_color[c]);
        explode_shape(5, z3, r, 0, fireworks_color[c]);
        led_canvas_display();
        usleep(50000);
        r += 1;
    }
}

fn main() {
    println!("****************************************");
    println!("*              FireWorks               *");
    println!("****************************************");
    println!();
    println!("夏が来たようだ。。。。。");

    usleep(2000000);

    srand(time() as u32);

    let mut k: i32;
    let mut m: usize;

    led_canvas_setsize(20, 40);
    set_terminal_reset();

    // 星空生成(コメントアウト中だが座標だけ用意)
    let mut star_col = [0_i32; 20];
    let mut star_low = [0_i32; 40];
    m = 0;
    while m < 19 {
        star_col[m] = rand() % led_col();
        star_low[m] = rand() % 5;
        m += 1;
    }

    let fireworks_color: [u8; 4] = [SHIRO, AO, KI, MIDORI];

    // 最初の地面表示
    led_canvas_clear();
    draw_ground();
    led_canvas_display();
    usleep(10000);

    // 5発分の打ち上げ
    k = 1;
    while k <= 5 {
        if k < 5 {
            let shape = rand() % 4;
            let z = rand() % 30 + 5;
            let c = (rand() % 4) as usize;
            launch_ascend(z);
            launch_explode(z, shape, fireworks_color[c]);
        } else {
            launch_finale_simple(fireworks_color);
        }
        k += 1;
    }

    led_canvas_display();
}
''', m={
    83: dict(bug=[("            let c = (rand() % 4) as usize;\n            launch_ascend(z);", "            launch_ascend(z);")]),
    84: dict(bug=[("    led_canvas_display();\n}\n", "    led_canvas_display();\n")]),
    85: dict(bug=[("    // 最初の地面表示\n    led_canvas_clear();\n    draw_ground();\n    led_canvas_display();", "    // 最初の地面表示\n    led_canvas_clear();\n    draw_ground();\n    led\\led_canvas_display();")]),
    86: dict(bug=[("        led_canvas_set_pixel(y, z3, AKA);", "        l       led_canvas_set_pixel(y, z3, AKA);")]),
    87: dict(bug=[("        led_canvas_set_pixel(y, z3, AKA);", "        l")]),
    88: dict(bug=[("        led_canvas_set_pixel(y, z3, AKA);", "        l       led_canvas_set_pixel(y, z3, AKA);")]),
    89: dict(bug=[("    r = 1;\n    while r <= 8 {\n        led_canvas_clear();\n        draw_ground();\n        explode_shape(5, z1", "    while (r=) {\n        led_canvas_clear();\n        draw_ground();\n        explode_shape(5, z1")]),
    90: dict(bug=[("    led_canvas_display();\n}\n", "    led_canvas_display();\n}\n    return 0;\n}\n")]),
    91: dict(bug=[("        explode_shape(5, z3, r, 0, fireworks_color[c]);\n        led_canvas_display();\n        usleep(50000);\n", "        explode_shape(5, z3, r, 0, fireworks_color[c]);\n        led_canvas_display();\n        usleep(50000)\n")]),
    92: dict(bug=[("fn launch_finale_simple(fireworks_color: [u8; 4]) {", "fn launch_finale_simple(fireworks_color: u8, )")]),
})
