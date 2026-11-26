#include <stdio.h>

int i,j;

int mian(void){
    printf("整数を入力");
    scanf("%d",&i);
    for(j=i;j>0;j--){
        printf("%d\n",j);
    }
}
