#include <stdio.h>

int main(void){
    int atari,x;
    atari = 3;
    printf("1から10までの数字を入力してください");
    scanf("%d",&x);
    if(x == atari){
        printf("当たりです\n");
    }else{
        printf("はずれです\n");
    }
}

