#include <stdio.h>

int money;

int main(void){
    printf("金額を入力してください:\n");
    scanf("%d",&money);
    printf("消費税を含めた金額は%d円です\n",money*1.1);

}
