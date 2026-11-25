#include <stdio.h>
int main(void)
{
    int p = 7, i, c = 0;
    for (i = 2; i < p; i++) {
        if (p % i == 0) {
            c++;
        }
    }
    printf("%d\n", c);
    return 0;
}
