#include <stdio.h>

int read_positive(void){
    int z;
    z=-1;
    while (z<0){
        printf("正の数を入力してください。");
        scanf("%d",&z);
    }
}

int gcd(int x,int y){
    int r;
    while (y !=0){
        r=x%y;
        x=y;
        y=r;
    }
    return x;
}


int main(void){ 
    int    x,y;
    printf("x?"); 
    x=read_positive();
    printf("y?");
    y=read_positive();
    printf("gcd(%d,%d)=%d\n",x,y,gcd(x,y));
    return 0;
}
