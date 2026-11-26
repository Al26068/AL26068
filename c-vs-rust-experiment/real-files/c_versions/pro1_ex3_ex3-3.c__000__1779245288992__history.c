#include <stdio.h>

int main (void){
    int x,y;
    printf("2つの異なる数を入力してください\n");
    scanf("%d",&x);
    scanf("%d",&y);
    while (x!=y){
        printf("同じ数です、2つの異なる数を入力してください");
        scanf("%d",&x);
        scanf("%d",&y);
    }
    printf("%dと%dが入力されました",x,y);
}
