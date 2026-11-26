#include <stdio.h>

int main(void){
    int i,max;
    printf("max?\n");
    scanf("%d",&max);

    for(i=1;i<=max;i++){
        if(max%i==0){
            printf("%d",i);
        }
    }
    return 0;

}
