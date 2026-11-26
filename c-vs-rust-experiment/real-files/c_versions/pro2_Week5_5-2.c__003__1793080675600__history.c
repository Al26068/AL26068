#include <stdio.h>
#include <math.h>

double BMI(double hight,double weight){
    hight=hight/100;
    return weight/pow(hight,2);
}

int main(void){
    double hight;
    double weight;
    printf("身長(cm): \n");
    scanf("%lf",hight);
    printf("体重(kg): ");
    scanf("%lf",weight);
    printf("BMIは%.1fです。\n",BMI(hight,weight));

    return 0;
}
