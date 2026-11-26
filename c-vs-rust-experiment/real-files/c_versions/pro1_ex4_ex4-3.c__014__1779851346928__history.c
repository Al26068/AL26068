#include <stdio.h>
#include <math.h>

int main(void){
    double pi,i,n;
    pi = 0;
    printf("n?\n");
    scanf("%lf",&n);
    for(i = 0; i <= n; i++){
        //pi=pi+pow(-1,i)/(2*i+1);
        if(pi % 2 == 0){
            pi = pi + 1.0 / (2.0 * i + 1.0);
        } else {
            pi = pi - 1.0 / (2.0 * i + 1.0);
        }

    }
    pi=pi*4;
    printf("第%f項までの近似値は%fです。",n,pi);
    return 0;
    }

