#include <stdio.h>

int main(void){
    int tutu[5],zaiko[5],uketori[5],oturi[5];
    int azukari,bangou,okaeshi,hituyou;
    int i;
    int turiari=0;
    for(i=0;i<5;i++){
    zaiko[i]=4;
    tutu[i]=5;
    oturi[i]=0;
    };
    int okane[5]={
        1000,500,100,50,10
    };

    char syouhin[5][128]={
        "1 麦茶:120円",
        "2 緑茶:130円",
        "3 珈琲:140円",
        "4 紅茶;150円",
        "5 牛乳:160円"
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
    if(turiari==1){
        printf("すでに筒がいっぱいです,お返しします.\n1000円-->%d\n500円-->%d\n100円-->%d\n50円-->%d\n10円-->%d\n",oturi[0],oturi[1],oturi[2],oturi[3],oturi[4]);
        for(i=0;i<5;i++){
            uketori[i]=uketori[i]-oturi[i];
        }
        for(i=0;i<5;i++){
            oturi[i]=0;
        }
    } 
    azukari=1000*uketori[0]+500*uketori[1]+100*uketori[2]+50*uketori[3]+10*uketori[4];
    printf("お預かりは%d円です\n買える商品は以下です",azukari);
    for(i=0;i<5;i++){
        if(nedan[i]<azukari){
            printf("%s\n",syouhin[i]);
        }
    }
    printf("購入番号を入力してください");
    scanf("%d",&bangou);
    bangou=bangou-1;
    if(bangou>=6){
        printf("番号がエラーです");
    }
    for(i=0;i<5;i++){
        if(bangou==i){
            okaeshi=azukari-nedan[i];
        }
    }
    if(okaeshi==0){
        printf("商品はこちらです(ガタッ)");
        zaiko[bangou]=zaiko[bangou]-1;
    }

    for(i=0;i<5;i++){
        hituyou = okaeshi/okane[i];
        if(hituyou>tutu[i]){
            oturi[i]=tutu[i];
        } else {
            oturi[i]=hituyou;
        }
        okaeshi=okaeshi-oturi[i]*okane[i];
    };
    if(okaeshi==0){
        printf("商品とおつりです\nおつりは%d円です\n",1000*oturi[0]+500*oturi[1]+100*oturi[2]+50*oturi[3]+10*oturi[4]);
        printf("1000円-->%d\n500円-->%d\n100円-->%d\n50円-->%d\n10円-->%d\n",oturi[0],oturi[1],oturi[2],oturi[3],oturi[4]);
        zaiko[bangou]=zaiko[bangou]-1;
    } else{
        printf("おつりにトラブルが発生しました。残念に思います。");
        printf("お金をお返しします(チャリン)\n");
    }
}
    
//for(i=0;i<5;i++){
            //if(okaeshi/okane[i]>0&&(okaeshi/okane[i])<tutu[i]){
                //oturi[i]=okaeshi/okane[i];
                //okaeshi=okaeshi-okane[i]*oturi[i];
            //}

        //}


//tutu[5],zaiko[5],uketori[5],oturi[5];
    //int azukari,turiari,bangou,okaeshi,hituyou;

// TODO
// 商品番号のずれ修正（bangou++周辺）
// 売り切れ判定を追加
// おつりを出した後に筒の残数を減らす
// 買える商品の判定を < から <= に変更
// 「つり銭切れ」の表示を追加
// 在庫が0になった商品の表示改善

