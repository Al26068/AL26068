#include <stdio.h>

int i;
long long x=10000000;
int main(void){
    for(i=1;i<51;i++){
        x=x+x/10000;
        printf("%d年後:%lld円\n",i,x);
    }
    return 0;

}
