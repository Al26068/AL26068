#include <stdio.h>

int i,n;

int main(void){
    printf("正の整数を入力してください");
    scanf("%d",&n);
    printf("20の約数を小さい順に列挙すると、");
    for(i=1;i<=n;i++){
        if(n%i==0){
            printf("%d,",i);
            if(n==i){
                printf("%d",i);
            }
            
        }
        
    }
    printf("である。");
    return 0;
}
