//! 実験用プログラム
#![forbid(unsafe_code)]

fn sort(a: &mut [i32]) {
    a.sort_unstable();
}

fn main() {
    let mut a = [3, 1, 2];
    let i = 0;
    sort(&mut a);
    println!("a[{i}]={}", a[i]);
}
