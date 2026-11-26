#include <stdio.h>
#include <math.h>


int main(void){
    int i,j,k,l,m,n;
    int sum,avg,spread,standard;
    int score[10],standardvalue[10];
    for(i=0;i<10;i++){
        scanf("%d",&score[i]);
    }
    
    //平均
    sum = score[0]+score[2]+score[3]+score[4]+score[5]+score[6]+score[7]+score[8]+score[9];
    avg = sum/10;
    //分散
    for(l=0;l<10;l++){
        spread = pow(score[l]-avg,2);
        spread = (spread/10) ;
    }
    //標準偏差
    standard = pow(spread,0.5);

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
