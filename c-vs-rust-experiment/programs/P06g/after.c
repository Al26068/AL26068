#include <stdio.h>
int main(void)
{
    int p[2][2] = {{0, 0}, {0, 0}};
    p[0][0] = 1;
    printf("%d\n", p[0][0]);
    return 0;
}
