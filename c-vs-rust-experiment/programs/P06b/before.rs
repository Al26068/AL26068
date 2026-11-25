//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let pi = 2.5_f64;
    let i = 3;
    if pi % 2 == 0 {
        println!("even");
    }
    println!("{pi} {i}");
}
