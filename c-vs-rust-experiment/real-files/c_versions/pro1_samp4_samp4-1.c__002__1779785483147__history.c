#include <stdio.h>

int main(void){
    int i;
    for(i=0;i<128;i++){
    printf("%d %c\n",i,i);
    }
    return 0;
    //%cの用法：int型の値を文字コードとみなして表示できる。
}
