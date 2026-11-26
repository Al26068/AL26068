#include <stdio.h>
int main(void){
    int a[2][2];
    int b[2][2];
    int p[2][2];
    printf("行列aを入力してください\n");
    printf("a[0][0]=");
    scanf("%d",&a[0][0]);
    printf("a[0][1]=");
    scanf("%d",&a[0][1]);
    printf("a[1][0]=");
    scanf("%d",&a[1][0]);
    printf("a[1][1]=");
    scanf("%d",&a[1][1]);
    printf("行列bを入力してください\n");
    printf("b[0][0]=");
    scanf("%d",&b[0][0]);
    printf("a[0][1]=");
    scanf("%d",&b[0][1]);
    printf("a[1][0]=");
    scanf("%d",&b[1][0]);
    printf("a[1][1]=");
    scanf("%d",&b[1][1]);
    p[0][0]=a[0][0]*b[0][0]+a[0][1]*b[1][0];
    p[0][1]=a[0][0]*b[0][1]+a[0][1]*b[1][1];
    p[1][0]=a[1][0]*b[0][0]+a[1][1]*b[1][0];
    p[1][1]=a[1][0]*b[0][1]+a[1][1]*b[1][1];
    printf("行列a,bの積は");
    printf("p[0][0]=",p[0][0]);
    printf("p[0][1]=",p[0][1]);
    printf("p[1][0]=",p[1][0]);
    printf("p[1][1]=",p[1][1]);
    return 0;
}
