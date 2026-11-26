#include <stdio.h>

int main(void){
    int i,max;
    i=1;
    printf("数を入力してください\n");
    scanf("%d",&max);
    while(i==100){
        if(max%i==0){
            printf("%d\n",i);
        }
        i=i+1;
    }
}
