#include <stdio.h>

int i,j;

int main(void){
    printf("整数を入力");
    scanf("%d",&i);
    for(j=i;j>=0;j--){
        printf("%d\n",j);
    }
    return 0;
}
