#include <stdio.h>
#include <string.h>

int countSpaces(char *str){
    int count =0;
    int i=0;

    while (str[i]!= '\0'){
        i=i+1;
    }
    return count;
}

int main(void){
    char moji[100];
    printf("英語の文字列を入力してください:");
    fgets(moji,sizeof(moji),stdin);
    printf("文字列%cの中の空白の数は%dです",countSpaces(moji),i);
}
