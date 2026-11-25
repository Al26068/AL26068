//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let p = 7;
    let mut c = 0;
    let mut i = 0;
    while i < p {
        if p % i == 0 {
            c += 1;
        }
        i += 1;
    }
    println!("{c}");
}
