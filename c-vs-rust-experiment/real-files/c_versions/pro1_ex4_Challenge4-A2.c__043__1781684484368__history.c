#include <stdio.h>
#include "terminalmode2.h"

int main(void){
    led_canvas_setsize(15,45);
    led_canvas_clear();
    int x,y;
    for(x=0;x<=LED_COL-1;x=x+2){
        for(y=x;y<=LED_ROW-1;y=y+2)
        led_canvas_set_pixel(x,y,MIDORI);
    }
    led_canvas_display();
    return 0;
}

