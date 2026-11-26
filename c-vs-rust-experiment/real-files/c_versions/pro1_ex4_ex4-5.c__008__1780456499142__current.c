#include <stdio.h>

int main(void){
    int max,i,j,x;
    j=1;
    
    printf("max?\n");
    scanf("%d",&max);
    for(i=2;i<=max;i++){
        x=1;
        for(j=2;j<i;j++){
        if(i%j==0){
            x=0;
            break;
        } }
        if(x==1){
            printf("%d\n",i);
        }
    }
    }

