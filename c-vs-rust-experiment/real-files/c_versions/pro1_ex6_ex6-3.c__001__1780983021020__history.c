#include <stdio.h>

double power(double x,int n){
    int i;
    double K;
    for(i=1;i<=n;i++){
        K=x*x;
    }
    return K;
}

int main(void){
    double x;
    int n;

    printf("x?");
    scanf("%lf",&x);
    printf("n?");
    scanf("%d",&n);
    printf("%fの%d乗は%f",x,n,power(x,n));
    return 0;
}
