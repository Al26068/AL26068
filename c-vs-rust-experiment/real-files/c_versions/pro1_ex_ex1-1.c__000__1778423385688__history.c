#include <stdio.h>

int main(void){
    int x,y,z,avg;
    printf("3つの整数x,y,zを入力してください\n");
    scanf("%d",&x);
    scanf("%d",&y);
    scanf("%d",&z);
    int avg = (x+y+z)/3;
    printf("平均は%dです\n",avg);

}
