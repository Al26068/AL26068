#include <stdio.h>

int x,y,z;
//xは入力された数,yは桁数,zは1の位,10の位・・・
int main(void){
    printf("正の数を入力してください");
    scanf("%d",&x);
    y=0;
    z=1;
    while(x%z!=x){
        printf("%dの位は%dです。\n",z,(x/z)%10);
        z=z*10;
        y=y+1;
    }
    printf("%dは%d桁の数です。",x,y);
return 0;
}
