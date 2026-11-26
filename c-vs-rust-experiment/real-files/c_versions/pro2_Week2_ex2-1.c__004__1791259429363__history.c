#include <stdio.h>

int a,b,i,j,g;
int n=0;
int x[1000];
int y[1000];
int main(void){
    printf("正の整数を入力してください\n");
    printf("正の整数を入力してください\n");
    scanf("%d",&a);
    scanf("%d",&b);

    for(i=1;i<a;i++){
        if(a%i==0){
            x[n]=i;
            n++;
        }
    }
    int na=n;
    n=0;
    for(i=1;i<b;i++){
        if(b%i==0){
            y[n]=i;
            n++;
        }
    }
    int nb=n;

    for(i=0;i<=na;i++){
        for(j=0;j<=nb;j++){
            if(x[i]==y[j]){
                g=x[i];
            }
    }
    }
    printf("最大公約数は%d/n",g);


}

