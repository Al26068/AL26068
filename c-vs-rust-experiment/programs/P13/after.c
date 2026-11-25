#include <stdio.h>
double circ(double r)
{
    return 2 * 3.14159 * r;
}
int main(void)
{
    double r = 1.0;
    printf("%.2f\n", circ(r));
    printf("%f\n", r);
    return 0;
}
