#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void){
    int answer;
    srand((unsigned)time(NULL));
    answer=(int)(rand()/(RAND_MAX+1.0)*1000);
    int x,i;
    i=1;
    printf("いくつだと思いますか？");
    scanf("%d",&x);
    while(x!=answer){
        if(x>answer){
            if (x>=answer+100){
                printf("とても大きい\n");
                i=i+1;
            } else if(x>=answer+10){
                printf("大きい\n");
                i=i+1;
            } else {
                printf("少し大きい\n");
                i=i+1;
            }
        if(x<answer){
            if(x<=answer-100){
            printf("とても小きい\n");
            i=i+1;
            } else if(x<=answer-10){
                printf("小さい\n");
                i=i+1;
            } else {
                printf("少し小きい\n");
                i=i+1;
            }
    }printf("いくつだと思いますか？");
        scanf("%d",&x);}
    printf("あたりです%d回でできました！",i);
    return 0;
}
}
