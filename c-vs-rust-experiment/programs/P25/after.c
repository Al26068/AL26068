#include <stdio.h>
int main(void)
{
    int n = 0;
    scanf("%d", &n);
    if (n % 5 != 0) {
        printf("not 5\n");
        printf("not divisible\n");
    }
    return 0;
}
