#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int r;
    srand(1);
    r = rand() % 10;
    printf("%d %d\n", r, RAND_MAX);
    return 0;
}
