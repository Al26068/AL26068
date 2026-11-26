#include <stdio.h>

int gcd(int n,int m){

    while(b!=0){
        int r=n%m;
        n = m;
        m = r;
    }
    return n;
}

int main(void){
    int n,m;
    printf("正の整数を入力してください:");
    scanf("%d",&n);
    printf("正の整数を入力してください:");
    scanf("%d",&m);
    printf("%dと%dの最小公倍数は%dです",n,m,gcd(n,m));
    return 0;

}
