#include <stdio.h>

void print_binary(int n){
    int a[8],i;
    for(i=0;i<8;i++){
        a[i]=n%2;
        n=n/2;
    }
    for(i=7;i>=0;i--){
        printf("%d",a[i]);
    }
}

int main(void){
    int x,y;
    printf("x?"); scanf("%d",&x);
    printf("y?"); scanf("%d",&y);
    printf(" x="); print_binary(x); printf(" %d\n",x);
    printf(" y="); print_binary(y); printf(" %d\n",y);
    printf(" x+y="); print_binary(x+y); printf("%d\n",x+y);
    return 0;
}
