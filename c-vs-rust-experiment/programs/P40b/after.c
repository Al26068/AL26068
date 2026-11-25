#include <stdio.h>
int main(void)
{
    double x1 = 1, y1 = 2, x2 = 3, y2 = 8;
    double a = (y2 - y1) / (x2 - x1);
    double b = y2 - a * x2;
    printf("%f %f\n", a, b);
    return 0;
}
