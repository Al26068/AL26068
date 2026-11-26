#include <stdio.h>
#include <math.h>

double function(int n){
    double a=0;
    double b=1;
    double S=0;
    double dx=(b-a)/n;
    int i;
    for(i=0;i<n;i++){
        double x=a+i*dx;
        S += x*x*dx;
    }
    return S;
}

int main(void){
    double n;
    printf("n?");
    scanf("%lf",&n);
    printf("%f",function(n));
}
