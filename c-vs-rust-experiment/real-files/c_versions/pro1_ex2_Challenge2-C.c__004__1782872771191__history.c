/*#include <stdio.h>

int main(void){
    double p1,p2,q1,q2,x1,x2,y1,y2,a1,a2,dp,dq,dx,dy;
    printf("P0の座標を入力\n");
    scanf("%lf",&p1);
    scanf("%lf",&q1);
    printf("P1の座標を入力\n");
    scanf("%lf",&p2);
    scanf("%lf",&q2);
    printf("Q0の座標を入力\n");
    scanf("%lf",&x1);
    scanf("%lf",&y1);
    printf("Q1の座標を入力\n");
    scanf("%lf",&x2);
    scanf("%lf",&y2);
    dq=q2-q1;
    dp=p2-p1;
    dx=x2-x1;
    dy=y2-y1;
    if(dp==0||dq==0||dx==0||dy==0){
        printf("交差する");
    }
    a1=dq/dp;
    a2=dy/dx;
    if(a1 != a2){
        printf("交差する");
    }else{
        printf("交差しない");
    }
}*/


// strategy1 値をそのままdy/dxのようにする⇒これだとマイナス、マイナスの処理をやると分母がプラスになり、バグ理始める
//　strategy2 入力値以外に中間処理用の変数を用意し、正負を判断したうえでdy/dx系に持ち込む
//　new problem1 これじゃあえげつないくらいめんどくさい量のコードかくんじゃね？
//　new view 上のはあくまで直線に限定した話で線分の話ではない＝つまり、アウト
//　from ChatGPT　二つの点がもう一方の直線をまたいでいるかを双方で確認する。
//　二つがまたぐことで必要十分条件化、この計算には外積を使う⇒外積まだ知らん

#include <stdio.h>

typedef struct {
    double x, y;
} Point;

double cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

int on_segment(Point a, Point b, Point p) {
    double minx = a.x < b.x ? a.x : b.x;
    double maxx = a.x > b.x ? a.x : b.x;
    double miny = a.y < b.y ? a.y : b.y;
    double maxy = a.y > b.y ? a.y : b.y;
    return minx <= p.x && p.x <= maxx && miny <= p.y && p.y <= maxy;
}

int intersects(Point p0, Point p1, Point q0, Point q1) {
    double d1 = cross(p0, p1, q0);
    double d2 = cross(p0, p1, q1);
    double d3 = cross(q0, q1, p0);
    double d4 = cross(q0, q1, p1);

    if (d1 * d2 < 0 && d3 * d4 < 0)
        return 1;

    if (d1 == 0 && on_segment(p0, p1, q0)) return 1;
    if (d2 == 0 && on_segment(p0, p1, q1)) return 1;
    if (d3 == 0 && on_segment(q0, q1, p0)) return 1;
    if (d4 == 0 && on_segment(q0, q1, p1)) return 1;

    return 0;
}

int main(void) {
    Point p0, p1, q0, q1;

    printf("P0の座標 (x y): ");
    scanf("%lf %lf", &p0.x, &p0.y);
    printf("P1の座標 (x y): ");
    scanf("%lf %lf", &p1.x, &p1.y);
    printf("Q0の座標 (x y): ");
    scanf("%lf %lf", &q0.x, &q0.y);
    printf("Q1の座標 (x y): ");
    scanf("%lf %lf", &q1.x, &q1.y);

    if (intersects(p0, p1, q0, q1))
        printf("交差する\n");
    else
        printf("交差しない\n");

    return 0;
}
