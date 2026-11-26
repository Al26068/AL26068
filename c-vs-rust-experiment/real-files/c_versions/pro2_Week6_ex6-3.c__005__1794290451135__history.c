#include <stdio.h>

void sort(int *p,int size){
    int i;
    int x;
    int change=1;
    while(change==1){
    for(i=0;i<size;i++){
    change=0;
    if(p[i]>p[i+1]){
        x=p[i];
        p[i]=p[i+1];
        p[i+1]=x;
        change=1;
    }
}
}
}

int main (void){
    int a[5];
    int i;
    for(i=0;i<5;i++){
        printf("a[%d]=",i);
        scanf("%d",&a[i]);
    }
    printf("ソート後");
    for(i=0;i<5;i++){
        printf("a[%d]=%d",i,sort(a,5));
    }
    return 0;
}