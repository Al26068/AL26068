#include <stdio.h>

int main(void){
    //ガチャガチャの関数
    int atari,x;
    atari = 3;
    printf("1から10までの数字を入力してください");
    scanf("%d",&x);
    //else分を消すこともOK
    if(x == atari){
        printf("当たりです\n");
    }else{
        printf("はずれです\n");
    }
}

