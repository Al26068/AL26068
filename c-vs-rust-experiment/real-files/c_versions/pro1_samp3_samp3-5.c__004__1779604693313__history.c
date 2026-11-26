#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main( void )
{
    int x,y,z,you,com,moji,hiku,crand,pwin,cwin;
    x=5;
    y=7;
    z=9;
    pwin=0;
    cwin=0;

    while( x!=0 || y!=0 || z!=0 ){
        printf("現在のx,y,zの値はx=%d,y=%d,z=%dです。引きたい文字を選んでください.",x,y,z);
        scanf("%d",moji);
        if(moji==1&&x>0){
            printf("引く数を選んでください");
            scanf("%d",&hiku);
            x=x-hiku;

            if(x<=0){
                printf("おめでとうございますxが0になりました！");
                pwin=pwin+1;
            }
            srand(time(NULL));
            int crand = rand() % x + 1;
            x=x-crand;
            if(x<=0){
                printf("残念ですx=0になりました。コンピューターの勝ちです。");
                cwin=cwin+1;
            }
            printf("COMは%dを引きました現在のxは%dです",crand,x);

        } else {
            printf("すでにxは０です。別の文字を入力してください。");
        }
        
        if(moji==2&&y>0){
            printf("引く数を選んでください");
            scanf("%d",&hiku);
            x=x-hiku;

            if(y<=0){
                printf("おめでとうございますyが0になりました！");
                pwin=pwin+1;
            }
            srand(time(NULL));
            int crand = rand() % y + 1;
            x=x-crand;
            if(x<=0){
                printf("COMは%dを引きました現在のy=%dです\n",crand,y);
                printf("残念ですy=0になりました。コンピューターの勝ちです。");
                cwin=cwin+1;
            }
            printf("COMは%dを引きました現在のy=%dです",crand,y);

        } else {
            printf("すでにxは０です。別の文字を入力してください。");
        }

        if(moji==3&&z>0){
            printf("引く数を選んでください");
            scanf("%d",&hiku);
            z=z-hiku;

            if(y<=0){
                printf("おめでとうございますzが0になりました！");
                pwin=pwin+1;
            }
            srand(time(NULL));
            int crand = rand() % z + 1;
            z=z-crand;
            if(x<=0){
                printf("COMは%dを引きました現在のz=%dです\n",crand,z);
                printf("残念ですz=0になりました。コンピューターの勝ちです。");
                cwin=cwin+1;
            }
            printf("COMは%dを引きました現在のz=%dです",crand,z);

        } else {
            printf("すでにzは０です。別の文字を入力してください。");
        }
    }
}
