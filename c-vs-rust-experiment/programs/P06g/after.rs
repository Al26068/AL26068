//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let mut p = [[0; 2]; 2];
    p[0][0] = 1;
    println!("{}", p[0][0]);
}
