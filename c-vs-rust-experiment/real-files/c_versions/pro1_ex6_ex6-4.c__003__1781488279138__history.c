#include <stdio.h>

int read_positive(void){
    int z;
    scanf("%d",&z);
    while (z<0){
        printf("正の数を入力しなおしてください。");
        scanf("%d",&z);
    }
}

int gcd(int x,int y){
    int r;
    while(r==0){
    r=x%y;
    if(r==0){
        int gcd=y;
    }
    x=y;
    y=r;
}
}

int mian(void){ 
    int    x,y;
    printf("x?"); 
    x=read_positive();
    printf("y?");
    y=read_positive();
printf("gcd(%d,%d)=%d\n",x,y,gcd(x,y));
}
