#include <stdio.h>

int main(void){
    int a[16];
    int i,x,n,b=0;
    printf("1から65535までの正の整数を入力してください:");
    scanf("%d",&x);
    n=x;                       
    for(i=0;i<16;i++){
        a[i]=x%2;
        x=x/2;
    }
    for(i=0;i<16;i++){
        if(a[i]==1){           
            b=i;
        }
    }
    printf("%dを2進数で表記すると、",n);
    for(i=b;i>=0;i--){         
        printf("%d",a[i]);
    }
    printf("です。\n");
    return 0;
}
