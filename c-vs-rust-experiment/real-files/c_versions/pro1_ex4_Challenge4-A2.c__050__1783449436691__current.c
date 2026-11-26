#include <stdio.h>
#include "terminalmode2.h"

int main(void){
    int row, col;

    led_canvas_setsize(24,24);
    led_canvas_clear();

    for(row=0; row<LED_ROW; row++){
        for(col=row*LED_COL/LED_ROW; col<LED_COL; col++){
            if((row+col)%2==0){
                led_canvas_set_pixel(row,col,MIDORI);
            }
        }
    }

    led_canvas_display();
    return 0;
}
