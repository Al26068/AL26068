#include <stdio.h>
#include "terminalmode2.h"
#include <time.h>

//関数プロトタイプ宣言
void draw_ground(void);
void draw_trail(int start, int y, int z);
int  my_isqrt(int n);
void explode_circle(int y, int z, int r, char color);
void explode_shape(int y, int z, int r, int shape, char color);
void launch_ascend(int z);
void launch_explode(int z, int shape, char color);
void launch_finale_simple(char fireworks_color[4]);

//地面描画
void draw_ground(void){
    int i;
    for(i=0; i<=39; i++){
        led_canvas_set_pixel(18,i,MIDORI);
        led_canvas_set_pixel(19,i,MIDORI);
    }
}

//残像
void draw_trail(int start, int y, int z){
    int i;
    for(i=start; i>y; i--){
        led_canvas_set_pixel(i,z,SHIRO);
    }
}

//近似式
int my_isqrt(int n){
    int x = 0;
    while((x+1)*(x+1) <= n){
        x++;
    }
    return x;
}

//大玉用（円形爆発）
void explode_circle(int y, int z, int r, char color){
    int dy;
    for(dy=-r; dy<=r; dy++){   
        int dz = my_isqrt(r*r - dy*dy) * 2;  
        int py  = y + dy;
        int pz1 = z - dz;
        int pz2 = z + dz;
        if(py>=0 && py<LED_ROW){
            if(pz1>=0 && pz1<LED_COL){
                led_canvas_set_pixel(py,pz1,color);
            }
            if(pz2>=0 && pz2<LED_COL){
                led_canvas_set_pixel(py,pz2,color);
            }
        }
    }
}

//爆発の形状
void explode_shape(int y, int z, int r, int shape, char color){
    if(shape==0 || shape==2){
        if(y-r>=0 && z-r>=0){
            led_canvas_set_pixel(y-r,z-r,color);
        }
        if(y-r>=0 && z+r<LED_COL){
            led_canvas_set_pixel(y-r,z+r,color);
        }
        if(y+r<LED_ROW && z-r>=0){
            led_canvas_set_pixel(y+r,z-r,color);
        }
        if(y+r<LED_ROW && z+r<LED_COL){
            led_canvas_set_pixel(y+r,z+r,color);
        }
    }
    if(shape==0 || shape==1){
        if(y-r>=0){
            led_canvas_set_pixel(y-r,z,color);
        }
        if(y+r<LED_ROW){
            led_canvas_set_pixel(y+r,z,color);
        }
        if(z-r>=0){
            led_canvas_set_pixel(y,z-r,color);
        }
        if(z+r<LED_COL){
            led_canvas_set_pixel(y,z+r,color);
        }
    }
    if(shape==3){
        explode_circle(y,z,r,color);
    }
}

//打ち上げ要因
void launch_ascend(int z){
    int y;
    for(y=19; y>5; y--){
        led_canvas_clear();
        draw_ground();
        draw_trail(19,y,z); 
        led_canvas_set_pixel(y,z,AKA);
        led_canvas_display();
        usleep(100000);
    }
}

//爆発要因
void launch_explode(int z, int shape, char color){
    int r;
    for(r=1; r<=8; r++){
        led_canvas_clear();
        draw_ground();
        led_canvas_set_pixel(5,z,AKA);
        explode_shape(5,z,r,shape,color);
        led_canvas_display();
        usleep(50000);
    }
}

//フィナーレ用
void launch_finale_simple(char fireworks_color[4]){
    int z1=10, z2=20, z3=30;
    int y, r;
    int c = rand()%4;

    /* 3本同時上昇 */
    for(y=19; y>5; y--){
        led_canvas_clear();
        draw_ground();
        draw_trail(19,y,z1);
        draw_trail(19,y,z2);
        draw_trail(19,y,z3);
        led_canvas_set_pixel(y,z1,AKA);
        led_canvas_set_pixel(y,z2,AKA);
        led_canvas_set_pixel(y,z3,AKA);
        led_canvas_display();
        usleep(100000);
    }

    /* 3本同時爆発 */
    for(r=1; r<=8; r++){
        led_canvas_clear();
        draw_ground();
        explode_shape(5,z1,r,0,fireworks_color[c]);
        explode_shape(5,z2,r,0,fireworks_color[c]);
        explode_shape(5,z3,r,0,fireworks_color[c]);
        led_canvas_display();
        usleep(50000);
    }
}

int main(void){
    printf("****************************************\n");
    printf("*                                      *\n");
    printf("*                                      *\n");
    printf("*              FireWorks               *\n");
    printf("*                                      *\n");
    printf("*                                      *\n");
    printf("****************************************\n");
    printf("\n");
    printf("夏が来たようだ。。。。。\n");

    usleep(2000000);

    srand(time(NULL));

    int k, m;

    led_canvas_setsize(20,40);
    set_terminal_reset();

    /* 星空生成(コメントアウト中だが座標だけ用意) */
    int star_col[20];
    int star_low[40];
    for(m=0; m<19; m++){
        star_col[m] = rand()%LED_COL;
        star_low[m] = rand()%5;
    }

    char fireworks_color[4] = {SHIRO, AO, KI, MIDORI};

    /* 最初の地面表示 */
    led_canvas_clear();
    draw_ground();
    led_canvas_display();
    usleep(10000);

    //5発分の打ち上げ
    for(k=1; k<=5; k++){
        if(k<5){
            int shape = rand()%4;        
            int z     = rand()%30+5;
            int c     = rand()%4;
            launch_ascend(z);
            launch_explode(z, shape, fireworks_color[c]);
        } else {
            launch_finale_simple(fireworks_color);  
        }
    }

    led_canvas_display();
    return 0;
}
