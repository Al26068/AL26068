#include <stdio.h>

int main(void){
    double shincho,taijyu,risou;
    printf("身長は？");
    printf("体重は？");
    scanf("%lf",&shincho);
    scanf("%lf",&taijyu);
    risou = shincho*shincho*22/10000;
    if(taijyu> (risou+5)){
        printf("甘いものを減らしましょう");
    } else if (taijyu<(risou-5)){
        printf("もっと食べましょう");
    } else {
        printf("その調子！");
    }
    return 0;

}
