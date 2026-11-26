#include <stdio.h>

int main (void) {
    int x,y,i;
    //xは割られる数,yは割る数
    int amari;
    printf("正の整数(割られる数)を入力してください:");
    scanf("%d",&x);
    printf("正の数(割る数)を入力してください:");
    scanf("%d",&y);
    printf("%d",x/y);
    amari=x%y;
    printf(".");
    for(i=0;i<50;i++){
        if (amari==0){
            break;
        }
        
        amari = amari*10;
        x = amari;
        amari = x%y;
        prinft("%d",x/y);
    }
    return 0;
}
