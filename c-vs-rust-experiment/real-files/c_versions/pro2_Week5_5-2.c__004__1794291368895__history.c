#include <stdio.h>
#include <math.h>

double BMI(double height,double weight){
    height=height/100;
    return weight/pow(height,2);
}

int main(void){
    double height;
    double weight;
    printf("身長(cm): \n");
    scanf("%lf",&height);
    printf("体重(kg): ");
    scanf("%lf",&weight);
    printf("BMIは%.1fです。\n",BMI(height,weight));

    return 0;
}
