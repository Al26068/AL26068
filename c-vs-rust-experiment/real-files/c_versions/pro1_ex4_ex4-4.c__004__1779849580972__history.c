#include <stdio.h>

int main(void){
    int x,y,i,j,n;
    printf("n?\n");
    scanf("%d",&n);
    for (i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            printf("(%d,%d)\n",i,j);
    }
}
