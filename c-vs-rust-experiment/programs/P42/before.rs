//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let mut pi = 0.0;
    let mut i = 0;
    while i < 3 {
        pi += 1 / (2 * i + 1);
        i += 1;
    }
    println!("{pi}");
}
