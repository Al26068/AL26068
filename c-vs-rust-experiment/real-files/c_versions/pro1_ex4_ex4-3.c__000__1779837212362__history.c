#include <stdio.h>

int main(void){
    double pi;
    int i,n;
    pi = 0.0;
    printf("n?\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        pi=pi+((-1)^i)/(2*i+1)
    }
}