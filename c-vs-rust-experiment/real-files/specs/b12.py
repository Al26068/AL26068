# -*- coding: utf-8 -*-
S = {}

S["pro2/Week1/ex1-1.c"] = dict(base=r'''
fn main() {
    let mut year: i32 = 0;
    let mut wareki: i32;
    println!("西暦(1896年以降)を入力してください:");
    read_into::<i32>(&mut year);
    if year > 2018 {
        wareki = year - 2018;
        if year == 2019 {
            print!("2019年は令和元年です。");
        } else {
            print!("{year}年は令和{wareki}年です。");
        }
    } else if year > 1988 {
        wareki = year - 1988;
        if year == 1989 {
            print!("1989年は平成元年です。");
        } else {
            print!("{year}年は平成{wareki}年です。");
        }
    } else if year > 1925 {
        wareki = year - 1925;
        if year == 1926 {
            print!("1926年は昭和元年です。");
        } else {
            print!("{year}年は昭和{wareki}年です。");
        }
    } else if year > 1911 {
        wareki = year - 1911;
        if year == 1912 {
            print!("1912年は大正元年です。");
        } else {
            print!("{year}年は大正{wareki}年です。");
        }
    } else if year > 1867 {
        if year == 1868 {
            print!("1868年は明治元年です。");
        } else {
            wareki = year - 1867;
            print!("{year}年は明治{wareki}年です。");
        }
    }
}
''', stdin="1915\n", m={
    115: dict(bug=[('print!("2019年は令和元年です。");', 'print!("{}年は令和元年です。");')]),
    116: dict(bug=[('print!("1989年は平成元年です。");', 'print!("{}年は平成元年です。");')]),
    117: dict(bug=[('print!("1926年は昭和元年です。");', 'print!("{}年は昭和元年です。");')]),
    118: dict(bug=[('print!("1912年は大正元年です。");', 'print!("{}年は大正元年です。");')]),
    119: dict(bug=[('print!("1868年は明治元年です。");', 'print!("{}年は明治元年です。");')]),
    120: dict(bug=[("if year == 2019 {", "if year = 2019 {")]),
    121: dict(bug=[("if year == 1989 {", "if year = 1989 {")]),
    122: dict(bug=[("if year == 1926 {", "if year = 1926 {")]),
    123: dict(bug=[("if year == 1912 {", "if year = 1912 {")]),
    124: dict(bug=[("if year == 1868 {", "if year = 1868 {")]),
    223: dict(bug=[("    } else if year > 1911 {", "    } else if year > 1988 {"), ("    } else if year > 1867 {", "    } else if year > 1988 {")]),
    224: dict(bug=[('print!("1926年は昭和元年です。");', 'print!("1925年は昭和元年です。");')]),
})
