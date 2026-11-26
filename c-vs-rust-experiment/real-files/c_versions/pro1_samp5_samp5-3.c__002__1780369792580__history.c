#include <stdio.h>

int main(void){
    double a[10],sum;
    int i;
    for(i=0;i<10;i++){
        scanf("%lf",&a[i]);
    }
    sum=0.0;
    for(i=0;i<10;i++){
        sum = sum +a[i];
    }
    printf("%f\n",sum/10);
    return 0;
}
