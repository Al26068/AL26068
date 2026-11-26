#include <stdio.h>

int main(void){
    int x,max;
    x = 1;
    printf("数を入力");
    scanf("%d",&max);
    while (x<max){
        printf("%d",x);
        x=x*2
    }
}