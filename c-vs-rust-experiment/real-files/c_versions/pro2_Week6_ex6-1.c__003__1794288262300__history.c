#include <stdio.h>

double innnerProd(int *a,int *b,int length){
    int i,prod=0;
    for(i=0;i<length;i++){
        prod=prod+a[i]*b[i];
    }
    return prod;
}

int main(void){
    int i;
    double a[3],b[3];
    for(i=0,i<2;i++;){
        printf("a[%d]=",i);
        scanf("%lf",&a[i]);
    }
    for(i=0,i<2;i++;){
        printf("b[%d]=",i);
        scanf("%lf",&b[i]);
    }

    printf("aとbの内積は%.2fです",innnerProd(a,b,3));
}

