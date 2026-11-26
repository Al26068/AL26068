#include <stdio.h>

int main(void){
    int answer = 578;
    int x;
    prinft("いくつだと思いますか？");
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
