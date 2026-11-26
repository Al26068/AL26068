#include <stdio.h>
int a,b,x=1,n;
int main(void){
    while(x==1){
    printf("数値を入力");
    scanf("%d",a);
    printf("数値を入力");
    scanf("%d",b);
    if(a%b==0){
        printf("%dは%dの約数です",a,b);
    } else {
        printf("%dは%dの約数ではありません",a,b);
    }
    printf("[続ける:1,終了:0]");
    scanf("%d",&n);
    if(x!=n){
        break;
    }
    }
}
