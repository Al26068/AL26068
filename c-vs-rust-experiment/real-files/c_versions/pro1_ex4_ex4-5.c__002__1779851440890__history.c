#include <stdio.h>

int main(void){
    int max,i,j;
    printf("max?\n");
    scanf("%d",&max);
    for (i=1;i<=max;i++){
      
        if(max%i==0){
            printf("%d\n",i);
        } else if (max%i!=0){
            j=j+1;
    }
}
}
