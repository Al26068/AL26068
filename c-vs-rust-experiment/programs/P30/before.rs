//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let mut i: i32;
    let _ = (i = 0, i < 2);
    while { let t = i; i += 1; t } {
        println!("{i}");
    }
}
