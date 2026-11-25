//! 実験用プログラム
#![forbid(unsafe_code)]

fn circ(r: f64) -> f64 {
    2.0 * std::f64::consts::PI * r
}

fn main() {
    let r = 1.0;
    println!("{:.2}", circ(r));
    println!("{r}");
}
