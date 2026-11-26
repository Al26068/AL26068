#include <stdio.h>

int main(void){
    int dest,in, cost, ret,a,b,c,d,e,f,g,h,i,j,k;
    printf("行先\n土呂-->1\n大宮-->2\n新都心-->3\n浦和-->4\n赤羽-->5\n尾久-->6\n上野-->7\n");
    scanf("%d",&dest);
    if(dest == 1){
        cost = 150;
    } else if (dest == 2){
        cost = 190;
    } else if (dest == 3){
        cost = 200;
    } else if (dest == 4){
        cost = 240;
    } else if (dest == 5){
        cost = 420;
    } else if (dest == 6){
        cost = 510;
    } else if (dest == 7){
        cost = 590;
    }
    printf("投入金額を入力\n1000-->\n500-->\n100-->\n50-->\n10-->7");
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    scanf("%d",&d);
    scanf("%d",&e);

    in=1000*a+500*b+100*c+50*d+10+e;
    ret=cost - in;
    if (ret/1000>0){
        f=ret/1000;
        ret=ret-f;
    }
    if(ret/500>0){
        g=ret/500;
        ret=ret-g*500;
    }
    if(ret/100>0){
        h=ret/100;
        ret=ret-h*500;
    }
    if(ret/50>0){
        i=ret/50;
        ret=ret-i*50;
    }
    if(ret/10>0){
        j=ret/10;
        ret=ret-i*10;
    }
    
    printf("釣銭\n1000-->%d\n500-->%d\n100-->%d\n50-->%d\n10-->%d",f,g,h,i,j);
    return 0;
}
