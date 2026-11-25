//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let mut a = [0; 9];
    let mut i = 0;
    while i <= 9 {
        a[i] = i;
        i += 1;
    }
    println!("{}", a[8]);
}
