#include <stdio.h>

int isPrime(int n){
    int i,n,x,t;
    for(i=1;i<n;i++){
        if(x%i==0){
            t=0;
            break;
        } else {
            t=1;
            break;
        }
    }
    return t;
}

int main(void){
    int i,x;
    printf("正の整数を入力してください");
    scanf("%d",&x);

    if(isPrime(x)==0){
        printf("%dは素数ではありません",x);
    } else {
        printf("%dは素数です。",x);
    }
    }

