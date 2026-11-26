#include<stdio.h>

int fibonachi(int n){
    int i,fn[3];
    //fn[0]=fn 
    //fn[1]=f(n-1)
    //fn[2]=f(n-2)
    if(n==0){
        printf("F(0)=0");
    }

    if(n==1){
        printf("F(1)=1");
    }
    
    if(n>=2){
        for(i=1;i<n-2;i++){
            fn[1]=1;
            fn[2]=0;
            fn[0]=fn[1]+fn[2];
            fn[1]=fn[2];
            fn[0]=fn[1];
        }
    }
    return fn[0];
}

int main(void){
    int n;
    printf("0以上の整数を入力:");
    scanf("%d",&n);
    printf("F(%d)=%d",n,fibonachi(n));
    return 0;
}
