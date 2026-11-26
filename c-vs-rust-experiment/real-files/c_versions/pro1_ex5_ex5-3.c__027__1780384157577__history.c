#include <stdio.h>
#include <math.h>


int main(void){
    int i,j,k,l,m,n;
    double sum,avg,spread,standard;
    double score[10],standardvalue[10];
    for(i=0;i<10;i++){
        scanf("%lf",&score[i]);
    }
    
    //平均
    sum = score[0]+score[1]+score[2]+score[3]+score[4]+score[5]+score[6]+score[7]+score[8]+score[9];
    avg = sum/10;
    //分散
    for(l=0;l<10;l++){
        spread = spread + pow(score[l]-avg,2);
        
    }
    spread = (spread/10) ;
    //標準偏差
    standard = pow(spread,0.5);

    // 偏差値
    for(m=0;m<10;m++){
        standardvalue[m]= ((score[m] - avg) / standard)*10 + 50;
    }
    for(n=0;n<10;n++){
        printf("平均%f 分散%f 標準偏差%f",avg,spread,standard);
        printf("得点%fの偏差値は%.2fです\n",score[n],standardvalue[n]);
    }
    return 0;
}
