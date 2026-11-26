#include <stdio.h>
int p,i;
int main(void){
    printf("正の整数を入力してください");
    scanf("%d",&p);
    for(i=2;i<p;i++){
        if(p%i==0){
            printf("%dは素数ではありません",p);
        } else {
            printf("%dは素数です",p);
        }
    }
    return 0;
}
