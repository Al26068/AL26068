#include <stdio.h>
int tuki;
int main(void){
    printf("月を入力してください");
    scanf("%d",&tuki);
    if(tuki>8 && tuki<12){
        printf("%d月は秋です。");
    } else {
        printf("%d月は秋ではありません。");
    }
    return 0;
}
