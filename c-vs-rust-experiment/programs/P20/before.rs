//! 実験用プログラム
#![forbid(unsafe_code)]

mod rng {
    //! 乱数（stdlib.h の代わり）
    /// 乱数を返す
    pub fn rand() -> i32 {
        7
    }
    /// 乱数の最大値
    pub const RAND_MAX: i32 = 32767;
}

fn main() {
    let r = rand() % 10;
    println!("{r} {RAND_MAX}");
}
