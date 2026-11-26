#include <stdio.h>

int fact(int n){
    int answer,i;
    answer=1;
    for(i=1;i<=n;i++){
        answer=answer*i;
    }
    return answer;

int main(void){
    int n,r;
    printf("n?"); scanf("%d",&n);
    printf("r?"); scanf("%d",&r);
    printf("nCr=%d\n",fact(n)/fact(r)/fact(n-r));
    return 0;
}
}