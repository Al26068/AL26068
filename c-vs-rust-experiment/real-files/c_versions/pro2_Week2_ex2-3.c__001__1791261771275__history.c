#include <stdio.h>

int i;
double x;
int y;
x=10000000;
int main(void){
    for(i=1;i<51;i++){
        printf("%d年後:%d円",i,1.0001*x);
    }
    return 0;

}
