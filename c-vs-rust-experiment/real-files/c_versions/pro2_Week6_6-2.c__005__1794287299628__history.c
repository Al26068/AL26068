#include <stdio.h>

double Average(int *seiseki,int length){
    int average=0,i;
    for(i=0;i<length;i++){
        average=average+seiseki[i];
    }
    return average/117 ;
}

int main(void){
    
    int score[117],average;
    int i,n;
    n=0;

for(i=0;i<117;i++){
    scanf("%d",&score[i]);
}


printf("平均点は%.2f点です",Average(score,117));
}
