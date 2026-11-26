#include <stdio.h>

int main(void){
    double x1,y1,x2,y2,a,b;
    printf("P0の座標を入力\n");
    scanf("%lf",&x1);
    scanf("%lf",&y1);
    printf("P1の座標を入力\n");
    scanf("%lf",&x1);
    scanf("%lf",&y2);
    a=((y2-y1)/(x2-x1));
    printf("%d",a);
    if(a==0){
        b=y1;
        printf("関数はY=%dです",y1);
    }
    b=(y2-(a*y1));
    printf("関数はY=%dX+%dです",a,b);
    return 0;
}
