#include <stdio.h>
double average(int a[], int n)
{
    int i, s = 0;
    for (i = 0; i < n; i++) {
        s = s + a[i];
    }
    return (double)s / n;
}
int main(void)
{
    int score[3] = {1, 2, 3};
    double ave;
    ave = average(score, 3);
    printf("%f\n", ave);
    return 0;
}
