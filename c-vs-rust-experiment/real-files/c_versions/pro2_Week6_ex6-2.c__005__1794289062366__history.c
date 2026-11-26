#include <stdio.h>

int min (int *p,int size){
    int x=p[0];
    int i;
    
    for(i=0;i<5;i++){
        if(x>p[i]){
            x=p[i];
        }
}
    return x;
}

int main(void){
    int a[5];
    int i;

    for(i=0;i<5;i++){
        printf("a[%d]=",i);
        scanf("%d",&a[i]);
    }
    printf("最小値は&dです",min(a,5));
}
