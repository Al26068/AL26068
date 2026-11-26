#include <stdio.h>

void sort(int *p,int size){
    int i;
    int x;
    int change=1;
    while(change==1){
        change=0;
    for(i=0;i<size-1;i++){
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
    printf("ソート後:\n");
    sort(a,5);
    for(i=0;i<5;i++){
        printf("a[%d]=%d\n",i,a[i]);
    }
    return 0;
}
