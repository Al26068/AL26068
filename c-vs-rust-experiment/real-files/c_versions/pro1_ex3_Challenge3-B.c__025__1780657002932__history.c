#include <stdio.h>

int main(void){
    int tutu[5],zaiko[5],uketori[5],oturi[5];
    int azukari,turiari,bangou,okaeshi,hituyou;
    int i,j,k,l,m;
    
    for(i=0;i<5;i++){
    zaiko[i]=4;
    tutu[i]=5;
    };

    int okane[5]={
        1000,500,100,50,10
    };

    char syouhin[5][128]={
        "麦茶:120円",
        "緑茶:130円",
        "珈琲:140円",
        "紅茶;150円",
        "牛乳:160円"
    };
    int nedan[5]={
        120,130,140,150,160
    };

    for(i=0;i<5;i++){
        printf("%s %d \n",syouhin[i],zaiko[i]);
    };

    printf("お金を入れてください\n 1000円-->\n500円-->\n100円-->\n50円-->\n10円-->\n");
    for(i=0;i<5;i++){
        scanf("%d",&uketori[i]);
        tutu[i]=uketori[i]+tutu[i];
        if(tutu[i]>10){
            oturi[i]=tutu[i]-10;
        }
    }
    int turi = 0;
    for(i=0;i<5;i++){
        if(oturi[i]>0){
            turiari=1;
        }
    }
    if(turiari=1){
        printf("おつりです\n1000円-->%d\n500円-->%d\n100円-->%d\n50円-->%d\n10円-->%d\n",oturi[0],oturi[1],oturi[2],oturi[3],oturi[4]);
    } 
    azukari=1000*uketori[0]+500*uketori[1]+100*uketori[2]+50*uketori[3]+10*uketori[4];
    printf("お預かりは%d円です\n買える商品は以下です",azukari);
    for(i=0;i<5;i++){
        if(nedan[i]>azukari){
            printf("%s",syouhin[i]);
        }
    }
    printf("購入番号を入力してください");
    scanf("%d",&bangou);
    for(i=0;i<5;i++){
        if(bangou==i){
            okaeshi=azukari-nedan[i];
        }
    }
    if(okaeshi==0){
        printf("商品はこちらです(ガタッ)");
    }

    for(i=0;i<5;i++){
        hituyou=okaeshi/okane[i];
        if(hituyou>tutu[i]){
            oturi[i]=tutu[i];
        } else {
            oturi[i]=hituyou;
        }
        okaeshi=okaeshi-oturi[i]*okane[i];
    };
    if(okaeshi==0){
        printf("商品とおつりです");
        printf("1000円-->%d\n500円-->%d\n100円-->%d\n50円-->%d\n10円-->%d\n",oturi[0],oturi[1],oturi[2],oturi[3],oturi[4]);
    } else{
        printf("おつりにトラブルが発生しました。残念に思います。");
        printf("お金をお返しします(チャリン)\n");
    }
    
    for(i=0;i<5;i++){
        printf("%d\n",zaiko[i]);
    }
    return 0;
}
//for(i=0;i<5;i++){
            //if(okaeshi/okane[i]>0&&(okaeshi/okane[i])<tutu[i]){
                //oturi[i]=okaeshi/okane[i];
                //okaeshi=okaeshi-okane[i]*oturi[i];
            //}

        //}


//tutu[5],zaiko[5],uketori[5],oturi[5];
    //int azukari,turiari,bangou,okaeshi,hituyou;

