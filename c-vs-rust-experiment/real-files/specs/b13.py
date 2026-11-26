# -*- coding: utf-8 -*-
S = {}

S["pro2/Week4/ex4-3.c"] = dict(base=r'''
fn main() {
    let mut a = [[0_i32; 2]; 2];
    let mut b = [[0_i32; 2]; 2];
    let mut p = [[0_i32; 2]; 2];
    println!("行列aを入力してください");
    print!("a[0][0]=");
    read_into::<i32>(&mut a[0][0]);
    print!("a[0][1]=");
    read_into::<i32>(&mut a[0][1]);
    print!("a[1][0]=");
    read_into::<i32>(&mut a[1][0]);
    print!("a[1][1]=");
    read_into::<i32>(&mut a[1][1]);
    println!("行列bを入力してください");
    print!("b[0][0]=");
    read_into::<i32>(&mut b[0][0]);
    print!("b[0][1]=");
    read_into::<i32>(&mut b[0][1]);
    print!("b[1][0]=");
    read_into::<i32>(&mut b[1][0]);
    print!("b[1][1]=");
    read_into::<i32>(&mut b[1][1]);
    p[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
    p[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1];
    p[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0];
    p[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1];
    println!("行列a,bの積は");
    println!("p[0][0]={}", p[0][0]);
    println!("p[0][1]={}", p[0][1]);
    println!("p[1][0]={}", p[1][0]);
    println!("p[1][1]={}", p[1][1]);
    print!("です。");
}
''', stdin="1\n2\n3\n4\n5\n6\n7\n8\n", m={
    141: dict(bug=[("read_into::<i32>(&mut a[0][0]);", "read_into::<i32>(a[0][0]);")]),
    142: dict(bug=[("read_into::<i32>(&mut a[0][1]);", "read_into::<i32>(a[0][1]);")]),
    143: dict(bug=[("read_into::<i32>(&mut a[1][0]);", "read_into::<i32>(a[1][0]);")]),
    144: dict(bug=[("read_into::<i32>(&mut a[1][1]);", "read_into::<i32>(a[1][1]);")]),
    145: dict(bug=[("read_into::<i32>(&mut b[0][0]);", "read_into::<i32>(b[0][0]);")]),
    146: dict(bug=[("read_into::<i32>(&mut b[0][1]);", "read_into::<i32>(b[0][1]);")]),
    147: dict(bug=[("read_into::<i32>(&mut b[1][0]);", "read_into::<i32>(b[1][0]);")]),
    148: dict(bug=[("read_into::<i32>(&mut b[1][1]);", "read_into::<i32>(b[1][1]);")]),
    149: dict(bug=[('println!("p[0][0]={}", p[0][0]);', 'println!("p[0][0]=", p[0][0]);')]),
    150: dict(bug=[('println!("p[0][1]={}", p[0][1]);', 'println!("p[0][1]=", p[0][1]);')]),
    151: dict(bug=[('println!("p[1][0]={}", p[1][0]);', 'println!("p[1][0]=", p[1][0]);')]),
    152: dict(bug=[('println!("p[1][1]={}", p[1][1]);', 'println!("p[1][1]=", p[1][1]);')]),
})
