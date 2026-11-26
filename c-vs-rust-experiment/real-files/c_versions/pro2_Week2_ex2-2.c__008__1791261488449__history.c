#include <stdio.h>
int p,i,x;
x=1;
int main(void){
    printf("正の整数を入力してください");
    scanf("%d",&p);
    if(p<2){
        x=0;
    }
    for(i=2;i<p;i++){
        if(p%i==0){
            x=0;
            break;
        }
    }
    if(x==1){
        printf("%dは素数です",p);
    } else {
        printf("%dは素数ではありません\n",p);
    }
    return 0;
}
