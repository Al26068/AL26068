#include <stdio.h>

double triangle(double x,double y){
    double x,y,S;
    S=x*y*0.5;
}

int main(void){
    printf("底辺?");
    scanf("%lf",&x);
    printf("高さ？");
    scanf("%lf",&y);
    printf("三角形の面積は%f\n",triangle(x,y));
    return 0;
}
