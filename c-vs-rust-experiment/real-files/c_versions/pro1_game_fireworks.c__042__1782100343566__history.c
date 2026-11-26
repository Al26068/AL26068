#include <stdio.h>
#include "terminalmode2.h"
#include <time.h>
//void群
void draw_ground(void){
    int i;
    for(i=0;i<=39;i++){
        led_canvas_set_pixel(18,i,MIDORI);
        led_canvas_set_pixel(19,i,MIDORI);
    }
}

void draw_trail(int y,int z){
    int i;
    for(i=10;i>y;i--){
        led_canvas_set_pixel(i,z,SHIRO);
    }
}

//爆発の形
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
}
//１発の爆発
void launch_explode(int z,int shape,char color){
    int r;
    for(r=1;r<=8;r++){
        led_canvas_clear();
        draw_ground();
        led_canvas_set_pixel(5,z,AKA);
        explode_shape(5,z,r,shape,color);
        led_canvas_display();
        usleep(50000);
        }
}
void launch_finale_simple(char fireworks_color[4]){
    int z1=10,z2=20,z3=30;
    int y,r;
    int c = rand()%4;

    for(y=19;y>5;y--){
        led_canvas_clear();
        draw_ground();
        draw_trail(y,z1);
        draw_trail(y,z2);
        draw_trail(y,z3);
        led_canvas_set_pixel(y,z1,AKA);
        led_canvas_set_pixel(y,z2,AKA);
        led_canvas_set_pixel(y,z3,AKA);
        led_canvas_display();
        usleep(100000);
    }

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
    printf("夏が来たようだ。。。。。");
    
    usleep(2000000);

    srand(time(NULL));
    //int宣言コーナー
    int y=5;
    int k,r,i,x,m,c;
    

    led_canvas_setsize(20,40);
    set_terminal_reset();
    
    
    int star_col[20];
    int star_low[40];
    //星空生成
    for(m=0;m<19;m++){
        star_col[m]=rand()%LED_COL;
        star_low[m]=rand()%5;
    }
    //星空表示
    //for(m=0;m<19;m++){
        //led_canvas_set_pixel(star_low[m],star_col[m],SHIRO);
    //}
    led_canvas_display();

    char fireworks_color[4] = {SHIRO, AO, KI, MIDORI};
    
    //(行、列)
    //(COL,ROW)
    //おそらくこの配置 6/18 19:00
    led_canvas_clear();
    for(i=0;i<=39;i++){
    led_canvas_set_pixel(18,i,MIDORI);
    led_canvas_set_pixel(19,i,MIDORI);    
    }

    led_canvas_display();

    usleep(10000);

    for(k=1;k<=5;k++){
        if(k<5){
        //毎回ランダムにするためのコード
        int shape=rand()%3;
        int z=rand()%30+5;
        int c=rand()%4;

            for(y=19;y>=0;y--){
                //led_canvas_clear();
                if(y>5){
                    led_canvas_clear();
                    /*for(m=0;m<19;m++){
                        led_canvas_set_pixel(star_low[m],star_col[m],SHIRO);
                    }*/
                    //地面生成
                    for(i=0;i<=39;i++){
                        led_canvas_set_pixel(18,i,MIDORI);
                        led_canvas_set_pixel(19,i,MIDORI);    
                    }
                    //残像生成
                    for(i=10;i>y;i--){
                        led_canvas_set_pixel(i,z,SHIRO);
                    }

                    led_canvas_set_pixel(y,z,AKA);
                    led_canvas_display();
                    usleep(100000);

                } else if(y==5){
                    led_canvas_set_pixel(y,z,AKA);

                    if(y>0){
                        led_canvas_set_pixel(y-1,z,KI);
                    }
                    if(y<19){
                        led_canvas_set_pixel(y+1,z,KI);
                    }

                    for(r=1;r<=8;r++){
                        if(shape==0){
                            led_canvas_clear();
                            /*for(m=0;m<19;m++){
                                led_canvas_set_pixel(star_low[m],star_col[m],SHIRO);
                            }*/
                            //center
                            led_canvas_set_pixel(y,z,AKA);
                            for(i=0;i<=39;i++){
                                led_canvas_set_pixel(18,i,MIDORI);
                                led_canvas_set_pixel(19,i,MIDORI);    
                            }
                                
                            //斜め方向
                            if(y-r>=0&&z-r>=0){
                                led_canvas_set_pixel(y-r,z-r,fireworks_color[c]);
                            }
                            if(y-r>=0&&z+r<LED_COL){
                                led_canvas_set_pixel(y-r,z+r,fireworks_color[c]);
                            }
                            if(y+r<LED_ROW&&z-r>=0){
                                led_canvas_set_pixel(y+r,z-r,fireworks_color[c]);
                            }
                            if(y+r<LED_ROW&&z+r<LED_COL){
                                led_canvas_set_pixel(y+r,z+r,fireworks_color[c]);
                            }
                            if(y-r>=0){
                                led_canvas_set_pixel(y-r,z,fireworks_color[c]);
                            }
                            if(y+r<LED_ROW){
                                led_canvas_set_pixel(y+r,z,fireworks_color[c]);
                            }
                            if(z-r>=0){
                                led_canvas_set_pixel(y,z-r,fireworks_color[c]);
                            }
                            if(z+r<LED_COL){
                                led_canvas_set_pixel(y,z+r,fireworks_color[c]);
                            }
                            led_canvas_display();
                            usleep(50000);

                        } else if(shape==1){

                            led_canvas_clear();
                            /*for(m=0;m<19;m++){
                                led_canvas_set_pixel(star_low[m],star_col[m],SHIRO);
                            }*/
                            for(i=0;i<LED_COL;i++){
                                led_canvas_set_pixel(18,i,MIDORI);
                                led_canvas_set_pixel(19,i,MIDORI);
                            }
                                
                            if(y-r>=0) {
                                    led_canvas_set_pixel(y-r,z,fireworks_color[c]);
                                }
                            if(y+r<LED_ROW) {
                                    led_canvas_set_pixel(y+r,z,fireworks_color[c]);
                                }
                            if(z-r>=0) {
                                    led_canvas_set_pixel(y,z-r,fireworks_color[c]);
                                }
                            if(z+r<LED_COL) {
                                    led_canvas_set_pixel(y,z+r,fireworks_color[c]);
                                }

                            led_canvas_display();
                            usleep(50000);

                        } else if (shape==2){
                            led_canvas_clear();
                            /*for(m=0;m<19;m++){
                                led_canvas_set_pixel(star_low[m],star_col[m],SHIRO);
                            }
                            */
                            for(i=0;i<LED_COL;i++){
                                led_canvas_set_pixel(18,i,MIDORI);
                                led_canvas_set_pixel(19,i,MIDORI);
                            }

                            if(y-r>=0&&z-r>=0){
                                led_canvas_set_pixel(y-r,z-r,fireworks_color[c]);
                            }
                            if(y-r>=0&&z+r<LED_COL){
                                led_canvas_set_pixel(y-r,z+r,fireworks_color[c]);
                            }
                            if(y+r<LED_ROW&&z-r>=0){
                                led_canvas_set_pixel(y+r,z-r,fireworks_color[c]);
                            }
                            if(y+r<LED_ROW&&z+r<LED_COL){
                                led_canvas_set_pixel(y+r,z+r,fireworks_color[c]);
                            }

                            led_canvas_display();
                            usleep(50000);
                        }
                    }
                }
            }
        } else if(k==5){
            int c=rand()%4;
            led_canvas_clear();
            for(i=0;i<LED_COL;i++){
                led_canvas_set_pixel(18,i,MIDORI);
                led_canvas_set_pixel(19,i,MIDORI);
            }
            int z1=10;
            int z2=20;
            int z3=30;
            for(y=19;y>=5;y--){
                led_canvas_clear();
                for(i=0;i<LED_COL;i++){
                led_canvas_set_pixel(18,i,MIDORI);
                led_canvas_set_pixel(19,i,MIDORI);
                }
                led_canvas_set_pixel(y,z1,AKA);
                led_canvas_set_pixel(y,z2,AKA);
                led_canvas_set_pixel(y,z3,AKA);
                for(i=10;i>y;i--){
                    led_canvas_set_pixel(i,z1,SHIRO);
                    led_canvas_set_pixel(i,z2,SHIRO);
                    led_canvas_set_pixel(i,z3,SHIRO);
                }
                
                }
               
                led_canvas_display();
        }

        }
    led_canvas_display();
return 0;    
}


                
