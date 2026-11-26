#include <stdio.h>
#include <string.h>

int countSpaces(char *str){
    int count =0;
    int i=0;

    while (str[i]!= '\0'){
        if(str[i]==''){
            count = count +1;
        }
        i=i+1;
    }
    return count;
}

int main(void){
    char moji[100],*p;
    
    printf("英語の文字列を入力してください:");
    fgets(moji,sizeof(moji),stdin);
    p= strchr(moji,'\n');
    if(p!=NULL){
        *p='\0';
    }
    printf("文字列%sの中の空白の数は%dです",moji,countSpaces(moji));

    return 0;
}
