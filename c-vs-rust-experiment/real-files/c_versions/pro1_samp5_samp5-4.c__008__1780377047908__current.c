#include <stdio.h>

int main(void){
    int a[10][10];
    int i,j;

    //9x9を計算

    for (i=0;i<9;++i){
    for (j=0;j<9;++j){
    
    a[i][j]=(i+1)*(j+1);}
    }

    //9x9の内容を表示
    for (i=0;i<9;++i){
        for(j=0;j<9;++j){
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
