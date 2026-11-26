#include <stdio.h>

int main(void){
    int a[10];
    int i,j;

    for(i=0;i<9;i++){
        scanf("%d",&a[i]);
    }
    for(j=0;j<9;j++){
        if(a[j]>0){
            printf("%dは正の数です",a[j]);
        } else {
            prinft("%dは負の数です",a[j]);
        }
    }
    return 0;
}
