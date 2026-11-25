//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let (n, i) = (12, 3);
    let mut t = 0;
    let x: i32;
    if x % i == 0 {
        t = 1;
    }
    println!("{t} {n}");
}
