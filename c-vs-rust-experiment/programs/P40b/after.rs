//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let (x1, y1, x2, y2) = (1.0, 2.0, 3.0, 8.0);
    let a = (y2 - y1) / (x2 - x1);
    let b = y2 - a * x2;
    println!("{a} {b}");
}
