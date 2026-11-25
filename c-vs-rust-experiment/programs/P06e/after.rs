//! 実験用プログラム
#![forbid(unsafe_code)]

fn average(a: &[i32]) -> f64 {
    let mut s = 0;
    let mut i = 0;
    while i < a.len() {
        s += a[i];
        i += 1;
    }
    f64::from(s) / a.len() as f64
}

fn main() {
    let score = [1, 2, 3];
    let ave = average(&score);
    println!("{ave}");
}
