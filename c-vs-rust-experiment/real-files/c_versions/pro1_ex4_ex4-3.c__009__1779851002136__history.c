#include <stdio.h>
#include <math.h>

int main(void){
    double pi;
    int i,n;
    pi = 0.0;
    printf("n?\n");
    scanf("%d",&n);
    for(i = 0; i < n; i++){
        pi=pi+pow(-1,i)/(2*i+1);
    }
    pi=pi*4;
    printf("第%d項までの近似値は%15fです。",n,pi);
    return 0;
    }

//if(i % 2 == 0){
            //pi = pi + 1.0 / (2.0 * i + 1.0);
        //} else {
          //  pi = pi - 1.0 / (2.0 * i + 1.0);
        //}
