#include <stdio.h>

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
    if(dp==0||dq==0||dx==0||dy=00){
        printf("交差する");
    }else if(a1 != a2){
        printf("交差する");
    }else{
        printf("交差しない");
    }
}
