#include <stdio.h>

int main(void){
    double a,b,p1,p2,q1,q2,x1,x2,y1,y2,a1,a2,dp,dq,dx,dy;
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
    dy=y2-y1;
    dx=x2-x1;
    b=y2-a*x2;
    a=(dy/dx);
    if((y1>a*x1+b&&y2<a*x2+b)||(y1<a*x1+b&&y2>a*x2+b)){
        dp=p2-p1;
        dq=q2-q1;
        c=(dq/dp)
        d=q2-c*p2
        if((q1>a*p1+b&&q2<a*p2+b)||(q1<a*p1+b&&q2>a*p2+b)){
            printf("直交する")
        }
    }else {
        printf("直交しない");
    }
    return 0;
}