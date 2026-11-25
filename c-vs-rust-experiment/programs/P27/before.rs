//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let a: i32;
    let b: i32;
    let c: i32;
    let _ = (a, b, c = 0);
    println!("{a} {b} {c}");
}
