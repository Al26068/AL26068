#include <stdio.h>

double power(double x,int n){
    int i;
    double ans=1;
    for(i=0;i<n;i++){
        ans= ans*x;
    }
    return ans;
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
