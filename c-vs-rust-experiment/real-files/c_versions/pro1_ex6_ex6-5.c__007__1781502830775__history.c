#include <stdio.h>
#include <math.h>

int function(int n){
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
    int n,x;
    printf("n?");
    scanf("%d",&n);
    printf("%d",function(n));
}
