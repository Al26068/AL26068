#include <stdio.h>
int main(void)
{
    int a[3] = {1, 2, 3};
    int sum, i;
    for (i = 0; i < 3; i++) {
        sum = sum + a[i];
    }
    printf("%d\n", sum);
    return 0;
}
