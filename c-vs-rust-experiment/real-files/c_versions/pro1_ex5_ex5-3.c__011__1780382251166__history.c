#include <stdio.h>
#include <math.h>


int main(void){
    int i,j,k,l,m,n;
    int sum,score[10],standardvalue[10],avg,spread,standard;

    for(i=0;i<10;i++){
        scanf("%d",&score[i]);
    }
    
    //平均
    for(k=0;k<10;k++){
        sum = sum + score[k];
        avg = (sum/10);
    }
    //分散
    for(l=0;l<10;l++){
        spread = pow(score[l]-avg,2);
        spread = (spread/10) ;
    }
    //標準偏差
    standard = pow(spread,1/2);

    // 偏差値
    for(m=0;m<10;m++){
        standardvalue[m]=50+10*((score[m]-avg)/standard);
    }
    for(n=0;n<10;n++){
        printf("平均%d 分散%d 標準偏差%d",avg,spread,standard);
        printf("得点%dの偏差値は%dです\n",score[n],standardvalue[m]);
    }
    return 0;
}
