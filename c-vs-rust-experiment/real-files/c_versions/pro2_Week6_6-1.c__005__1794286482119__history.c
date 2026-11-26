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
    printf("80点以上の人は%d人です",numOfGradeA(score[i],117))
}
