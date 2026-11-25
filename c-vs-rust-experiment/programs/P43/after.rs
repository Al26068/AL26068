//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let a = [1, 2, 3];
    let mut sum = 0;
    let mut i = 0;
    while i < 3 {
        sum += a[i];
        i += 1;
    }
    println!("{sum}");
}
