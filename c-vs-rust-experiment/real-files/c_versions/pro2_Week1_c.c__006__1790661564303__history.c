#include <stdio.h>

in6 main(void){
    int x;
    printf("整数を入力して下さい:");
    scanf("%d",&x);
    if(x%5)
        printf("その数は5でわりきれません\n");
    else
        printf("その数は5で割り切れます\n");
        return 0;
    
}
