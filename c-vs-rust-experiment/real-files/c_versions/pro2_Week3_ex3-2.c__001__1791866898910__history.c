#include <stdio.h>

int x,y,z;
//xは入力された数,yは桁数,zは1の位,10の位・・・
int main(void){
    printf("正の数を入力してください");
    scanf("%d",&x);
    y=0;
    z=1;
    while(x%z!=x){
    if(x%z!=0){
        printf("%dの位は%dです。",z,x%10);
        z=z*10;
        y=y+1;
    }}
    pritnf("%dは%d桁の数です。",x,y);

}
