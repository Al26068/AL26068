#include <stdio.h>

int main(void){
    int max,min,i,j,a[10];

    for(i=0;i<10;i++){
        scanf("%d",&a[i]);
    }
    for(j=0;j<10;j++){
        if(a[j]>max){
            max = a[j];
        } else if (a[j]<min){
            min = a[j];
        } 
    }
    printf("最大値は%d\n最小値は%d\n",max,min);
}
