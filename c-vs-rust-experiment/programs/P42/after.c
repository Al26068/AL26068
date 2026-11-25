#include <stdio.h>
int main(void)
{
    double pi = 0.0;
    int i;
    for (i = 0; i < 3; i++) {
        pi = pi + 1.0 / (2 * i + 1);
    }
    printf("%f\n", pi);
    return 0;
}
