#include <stdio.h>
void sort(int a[], int n)
{
    int i, j, t;
    for (i = 0; i < n; i++) {
        for (j = 0; j + 1 < n - i; j++) {
            if (a[j] > a[j + 1]) {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
}
int main(void)
{
    int a[3] = {3, 1, 2};
    int i = 0;
    printf("a[%d]=%d\n", i, sort(a, 3));
    return 0;
}
