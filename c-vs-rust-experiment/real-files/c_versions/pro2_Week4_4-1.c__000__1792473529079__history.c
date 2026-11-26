#include <stdio.h>

int main(void){
    int score[100];
    int i,n;
    n=0;

for(i=0;i<117;i++){
    scanf("%d",&score[i])
    if(score[i]>80){
        n=n+1;
    }
}
printf("80点以上の人は%d人です",n);
}
