#include <stdio.h>

int main (void) {
    int x,y;
    //xは割られる数,yは割る数
    printf("正の整数(割られる数)を入力してください:");
    scanf("%d",&x);
    printf("正の数(割る数)を入力してください:");
    scanf("%d",&y);
    printf("%f",x/y);
    
}
