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
    dy=y2-y1;
    dx=x2-x1;
    a=(dy/dx);
    printf("\n%f",a);
    if(a==0){}
    b=y2-a*x2;
    if(b<0){
        printf("関数はY=%fX%fです",a,b);
    } else if(b>0){
        printf("関数はY=%fX+%fです",a,b);
    } else {
        printf("関数はY=%fXです",a);
    }
    return 0;
}