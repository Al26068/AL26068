#include <stdio.h>
#include <math.h>


int main(void){
    int i,j,k,l,m,n;
    int sum,score[10],standardvalue[10],avg,spread,standard;

    for(i=0;i<10;i++){
        sacnf("%d",&score[i]);
    }
    for(j=0;j<10;j++){
        //平均
        for(k=0;k<10;k++){
            sum = sum + score[k];
            avg = sum /10;
        }
        //分散
        for(l=0;l<10;l++){
            spread = pow((score[i]-avg),2)/10 ;
        }
        //標準偏差
        standard = pow(spread,1/2);

        // 偏差値
        for(m=0;m<10;m++){
            standardvalue[m]=50+10*((score[m]-avg)/standard);
        }
    }
}