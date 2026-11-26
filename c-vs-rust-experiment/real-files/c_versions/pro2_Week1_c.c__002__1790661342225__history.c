#include <stdio.h>

int main(void){
    int x;
    printf("整数を入力して下さい");
    sfcanf("%d,&x");
    if(x%5)
        printf("その数は5ではありません");
        return 0;
    
}
