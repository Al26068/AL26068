#include <stdio.h>

int main(void){
    double a[365],sum;
    int i;
    for(i=0;i<365;i++){
        scanf("%lf",&a[i]);
    }
    sum=0.0;
    for(i=0;i<365;i++){
        sum = sum +a[i];
    }
    printf("%f\n",sum/365);
    return 0;
}
