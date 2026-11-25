//! 実験用プログラム
#![forbid(unsafe_code)]

fn twice(a: i32) -> i32 {
    a * 2
}

fn main() {
    println!("{}", twice(1, 2));
}
