#include <stdio.h>

double money;


int main(void){
    printf("金額を入力してください:\n");
    scanf("%lf",&money);
    printf("消費税を含めた金額は%f円です\n",money*1.1);

}
