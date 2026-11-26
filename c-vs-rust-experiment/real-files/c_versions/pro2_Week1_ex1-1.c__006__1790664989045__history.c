#include <stdio.h>

int year;
int wareki;

int main(void){
    printf("西暦(1896年以降)を入力してください:\n");
    scanf("%d",&year);
    if(year>2018){
        wareki = year -2018;
        if(year==2019){
            printf("2019年は令和元年です。");
        } else {
        printf("%d年は令和%d年です。",year,wareki);
        }
    } else if(year>1988){
        wareki = year -1988;
        if(year==1989){
            printf("1989年は平成元年です。");
        } else {
        printf("%d年は平成%d年です。",year,wareki);
        }
    } else if(year>1925){
        wareki = year -1925;
        if(year==1926){
            printf("1925年は昭和元年です。");
        } else {
        printf("%d年は昭和%d年です。",year,wareki);
        }
    } else if(year>1988){
        wareki = year -1911;
        if(year==1912){
            printf("1912年は大正元年です。");
        } else {
        printf("%d年は大正%d年です。",year,wareki);
        }
    } else if(year>1988){
        if(year==1868){
            printf("1868年は明治元年です。");
        } else {
        wareki = year -1867;
        printf("%d年は明治%d年です。",year,wareki);
        }
    }
}
