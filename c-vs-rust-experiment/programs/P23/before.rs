//! 実験用プログラム
#![forbid(unsafe_code)]

fn main() {
    let s: Vec<char> = "my".chars().collect();
    if s[0] == 'my' {
        println!("found");
    }
}
