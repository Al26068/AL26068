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
    let mut a: i32 = 0;
    let mut b: i32 = 0;
    read_into::<i32>(&mut a);
    read_into::<i32>(&mut b);
    if a == 0 || b == 0 {
        println!("zero");
    }
}
