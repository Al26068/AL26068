//! 実験用プログラム
#![forbid(unsafe_code)]

fn read_into<T: std::str::FromStr>(v: &mut T) {
    let mut s = String::new();
    let _ = std::io::stdin().read_line(&mut s);
    if let Ok(x) = s.trim().parse() {
        *v = x;
    }
}

fn main() {
    let mut n: i32 = 0;
    read_into::<i32>(&mut n);
    let mut sum = 0;
    let mut i = 1;
    while i <= n {
        sum += i;
        i += 1;
    }
    println!("{sum}");
}
