#include <stdio.h>

int main(void){
    int a[16];
    int i,x;
    printf("1から65535までの正の整数を入力してください:");
    scanf("%d",&x);
    for(i=0;i<15;i++){
        a[16-i]=x%2;
        x=x/2;
    }
    printf("%dを2進数で表すと,",x);
    for(i=0;i<15;i++){
    printf("%d",a[16-i]);
    }
}
