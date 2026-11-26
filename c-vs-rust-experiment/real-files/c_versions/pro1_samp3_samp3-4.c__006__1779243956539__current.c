#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void){
    int answer;
    srand((unsigned)time(NULL));
    answer=(int)(rand()/(RAND_MAX+1.0)*1000);
    int x;
    printf("いくつだと思いますか？");
    scanf("%d",&x);
    while(x!=answer){
        if(x>answer){
            printf("大きすぎます\n");
        } else {
            printf("小さすぎます\n");
        }
        printf("いくつだと思いますか？");
        scanf("%d",&x);
    }
    printf("あたりですよくできましたさすがです");
    return 0;
}
