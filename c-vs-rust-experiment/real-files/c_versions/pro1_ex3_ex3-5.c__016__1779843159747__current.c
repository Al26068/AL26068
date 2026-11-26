#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main( void )
//main 関数名
//int-intenger、関数が出す値
//void　関数が読み込む値
//Cのルール　main名の関数が1番最初に読み込まれる　voidを読み込んでも良き。何かファイルを読み込みたい（ポインタ：絶対座標と座標の長さがわかってその間に）
//intは打っておこう

{
    int x,y,z,you,com,moji,hiku,crand,p0,c0;
    x=5;
    y=7;
    z=9;
    p0=0;
    c0=0;

    while( x!=0 || y!=0 || z!=0 ){
        printf("現在のx,y,zの値はx=%d,y=%d,z=%dです。引きたい文字を選んでください.\n",x,y,z);
        scanf("%d",&moji);
        if(moji==1&&x>0){
            printf("引く数を選んでください\n");
            scanf("%d",&hiku);
            x=x-hiku;

            if(x<=0){
                printf("xが0になりました\n");
                if(x==0&&y==0&&z==0){
    printf("ユーザーの勝利です！");
    break;
}
            }
            if(x>0){srand(time(NULL));
            int crand = rand() % x + 1;
            x=x-crand;
            if(x<=0){
                printf("x=0になりました。\n");
                if(x==0&&y==0&&z==0){
    printf("comの勝利です");
    break;
}
            }}

            
            printf("COMは%dを引きました現在のxは%dです\n",crand,x);

        } else if(moji==1&&x<=0){
            printf("すでにxは０です。別の文字を入力してください。");
        } else if(moji==2&&y>0){
            printf("引く数を選んでください\n");
            scanf("%d",&hiku);
            y=y-hiku;

            if(y<=0){
                printf("yが0になりました！\n");
                if(x==0&&y==0&&z==0){
    printf("ユーザーの勝利です！");
    break;
}
            }
            if (y>0){srand(time(NULL));
            int crand = rand() % y + 1;
            y=y-crand;
            if(y<=0){
                printf("COMは%dを引きました現在のy=%dです\n",crand,y);
                if(x==0&&y==0&&z==0){
    printf("comの勝利です");
    break;
}
            }}
           

        } else if (moji==2&&y<=0){
            printf("すでにxは０です。別の文字を入力してください。\n");
        } else if (moji==3&&z>0){
            printf("引く数を選んでください\n");
            scanf("%d",&hiku);
            z=z-hiku;

            if(z<=0){
                printf("zが0になりました！\n");
                p0=p0+1;
                if(x==0&&y==0&&z==0){
    printf("ユーザーの勝利です！");
    break;
}
            }
            if(z>0){srand(time(NULL));
            int crand = rand() % z + 1;
            z=z-crand;
            printf("COMは%dを引きました現在のz=%dです\n",crand,z);
            if(z<=0){ 
                printf("z=0になりました。\n");
                c0=c0+1;
                if(x==0&&y==0&&z==0){
                printf("comの勝利です");
                break;
                }
            }};
            

        } else if (moji==3&&z<=0){
            printf("すでにzは０です。別の文字を入力してください。\n");
        }
    }
    
    return 0;
//returnでミス発覚   
}








