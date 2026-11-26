#include <stdio.h>
double circumeference(double radius){
    return 2*3.14*radius;
}
int main(void){
    printf("円の半径を入力");
    scanf("%lf",&circumeference);
    printf("演習の大きさは%.2fです",circumeference);
}

