#include <stdio.h>
#include <string.h>

int main(void){
    char moji[100],*p;
    int x;
    printf("英文を入力してください:");
    
    fgets(moji,sizeof(moji),stdin);
    p= strchr(moji,'\n');
    if(p!=NULL){
        *p='\0';
    }
    x=strlen(moji);

    printf("あなたが入力した文字数は%dです",x);
    return 0;
}
