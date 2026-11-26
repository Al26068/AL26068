#include <stdio.h>

int numOfGradeA (int *seiseki, int length){
    int count = 0,i;
    for(i=0;i<length;i++){
        if(seiseki[i]>=80){
            count = count +1;
        }
    }
    return count;
}
int main(void){
    int i;
    int score[117];
    for(i=0;i<117;i++){
    scanf("%d",&score[i]);
}
    
    printf("80点以上の人は%d人です\n",numOfGradeA(score,117));
    return 0;
}
