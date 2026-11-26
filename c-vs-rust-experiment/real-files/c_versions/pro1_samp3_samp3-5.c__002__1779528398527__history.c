#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main( void )
{
    int x,y,z,you,com,moji,hiku,crand;
    x=5;
    y=7;
    z=9;
    printf("x,y,zの初期値はx=5,Y=7,Z=9です。\nひきたい文字をxなら1,yなら2,zなら3を入力してください");
    scanf("%d",&moji);
    while( x!=0 || y!=0 || z!=0 ){
        if(moji==1){
            printf("引く数を選んでください");
            scanf("%d",&hiku);
            x=x-hiku;
            srand(time(NULL));
            int crand = rand() % x + 1;
            x=x-crand;
            printf("COMは%dを引きました現在のxは%dです",crand,x);

        } else if(moji==2){
             printf("引く数を選んでください");
            scanf("%d",&hiku);
            y=y-hiku;
        } else if(moji=3){
            printf("引く数を選んでください");
            scanf("%d",&hiku);
            z=z-hiku;
        }
    }
}
