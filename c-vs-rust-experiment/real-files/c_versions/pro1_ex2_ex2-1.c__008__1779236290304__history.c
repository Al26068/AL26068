#include <stdio.h>

int main(void){
    int x,y;
    printf("xの値を入力\n");
    printf("yの値を入力\n");
    scanf("%d",&x);
    scanf("%d",&y);
    if( x > y ){
        printf("大きい値は%dです",x);
    } else{
        printf("大きい値は%dです",y);
    }
    return 0;
}

