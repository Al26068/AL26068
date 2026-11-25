//! 実験用プログラム
#![forbid(unsafe_code)]

fn first(a: &[i32]) -> i32 {
    a[0]
}

fn main() {
    let s = [1, 2, 3];
    println!("{}", first(s[2]));
}
