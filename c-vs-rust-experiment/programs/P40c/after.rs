//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let (a, e) = (1, 2);
    let total = 1000 * a + 10 * e;
    println!("{total}");
}
