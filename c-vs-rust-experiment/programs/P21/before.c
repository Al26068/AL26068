#include <stdio.h>
int first(int a[])
{
    return a[0];
}
int main(void)
{
    int s[3] = {1, 2, 3};
    printf("%d\n", first(s[2]));
    return 0;
}
