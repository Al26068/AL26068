#include <stdio.h>

int main(void){
    int x,y;
    printf("xの値を入力してください");
    printf("yの値を入力してください");
    scanf("%d\n",x);
    scanf("%d\n",y);
    if (x == y){
        printf("どちらも同じです");
    } else if ( x > y){
        printf("大きいほうの数は%dです",x);
    } else{
         printf("大きいほうの数は%dです",y);
    }
    return 0;
}

