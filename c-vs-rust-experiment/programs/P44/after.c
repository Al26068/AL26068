#include <stdio.h>
int main(void)
{
    int a[10], i;
    for (i = 0; i <= 9; i++) {
        a[i] = i;
    }
    printf("%d\n", a[8]);
    return 0;
}
