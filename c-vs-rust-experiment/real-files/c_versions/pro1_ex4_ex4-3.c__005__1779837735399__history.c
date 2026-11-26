#include <stdio.h>

int main(void){
    double pi;
    int i,n;
    pi = 0.0;
    printf("n?\n");
    scanf("%lf",&n);
    for(i = 0; i < n; i++){
        if(i % 2 == 0){
            pi = pi + 1.0 / (2.0 * i + 1.0);
        } else {
            pi = pi - 1.0 / (2.0 * i + 1.0);
        }
    }
    pi=pi*4;
    printf("第%d項までの近似値は%fです。",n,pi);
    return 0;
    }

