#include <stdio.h>

double innerProd(double *a,double *b,int length){
    int i;
    double prod=0;
    for(i=0;i<length;i++){
        prod=prod+a[i]*b[i];
    }
    return prod;
}

int main(void){
    int i;
    double a[3],b[3];
    for(i=0;i<3;i++){
        printf("a[%d]=",i);
        scanf("%lf",&a[i]);
    }
    for(i=0;i<3;i++){
        printf("b[%d]=",i);
        scanf("%lf",&b[i]);
    }

    printf("aとbの内積は%.2fです",innerProd(a,b,3));
}

