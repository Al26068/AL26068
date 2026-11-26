#include <stdio.h>
#include <math.h>

int function(int n,int x){
    int i,y,b,a;
    a=0;
    b=1;
    for(i=0;i<=(n/abs(b-a));i++){
        x=pow((abs(b-a)/n),3);
    }
    return x;
}

int main(void){
    int a,b,n,x;
    printf("n?");
    scanf("%d",&n);
    printf("%d",function(n,x));
}
