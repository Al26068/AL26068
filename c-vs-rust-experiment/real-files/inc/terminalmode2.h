/********************************************************************
 * <ProNyu1 non-blocking I/O header file> * 
 * filename: "terminalmode2.h"
 *
 * Purpose:
 * This header file tries to isolate the students
 * from the details of non-blocking I/O and lets
 * the students create textbased animation easier.
 *
 * ------------------------------------------------------------------
 * History:
 * Date        by             Comment
 * 2022/02/15  k.imamura      Initial coding 
 *                            printf("\n") may/may not work well.
 *                            Use printf("%c",0xD) or
 *                            printf("%c%c",0xA,0xD) instead
 *                            Depends on interpretation of "\n" (2023/06/07)
 *
 * 2023/04/17  k.imamura      Added led_canvas_peek()
 *
 * 2023/04/17  k.imamura      led_canvas_set_pixel() and text_canvas_write_char()
 *                            are variadic.
 *
 * 2023/06/07  k.imamura      Initial version of "terminalmode2.h" 
 *                            led_canvas_setsize() added to define canvas size.
 *                            Two macros added to maintain backward compatibility: 
 *                             #define LED_ROW   (led_max_ROW())
 *                             #define LED_COL   (led_max_COL())
 *                            reset_terminal_mode() now does free(canvas)
 *
 * 2023/06/09  k.imamura      text_canvas_write_char() added fg and bg color 
 *
 *-------------------------------------------------------------------

 * Example of usage:
 *
 *   #include "terminalmode2.h"
 *   main()
 *   { char ch;
 *     led_canvas_setsize(0,0); //default size
 *     set_terminal_reset();
 *     text_canvas_write_char(5,3,'d',TMIDORI,KI,102);
       led_canvas_set_pixel(8,8, KI);
 *     led_canvas_display();
 *     ch = getkbchar();
 *   }
 *
 * Note0:
 * void set_conio_terminal_mode()
 * void reset_terminal_mode()
 * The above two functions are copied from (2022/06/13):
 * http://itecnote.com/tecnote/r-c-non-blocking-keyboard-input
 * 
 ****************************************************************/


#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include <string.h>
#include <time.h>

/*
 * This color definitions are copied from:
 *         https://gist.githubusercontent.com/
 *
 * This is free and unencumbered software released into the public domain.
 *
 * For more information, please refer to <https://unlicense.org>
 */

//#include "ansi_color.h"

//Regular text
#define BLK "\e[0;30m"
#define RED "\e[0;31m"
#define GRN "\e[0;32m"
#define YEL "\e[0;33m"
#define BLU "\e[0;34m"
#define MAG "\e[0;35m"
#define CYN "\e[0;36m"
#define WHT "\e[0;37m"

//Regular bold text
#define BBLK "\e[1;30m"
#define BRED "\e[1;31m"
#define BGRN "\e[1;32m"
#define BYEL "\e[1;33m"
#define BBLU "\e[1;34m"
#define BMAG "\e[1;35m"
#define BCYN "\e[1;36m"
#define BWHT "\e[1;37m"

//Regular underline text
#define UBLK "\e[4;30m"
#define URED "\e[4;31m"
#define UGRN "\e[4;32m"
#define UYEL "\e[4;33m"
#define UBLU "\e[4;34m"
#define UMAG "\e[4;35m"
#define UCYN "\e[4;36m"
#define UWHT "\e[4;37m"

//Regular background
#define BLKB "\e[40m"
#define REDB "\e[41m"
#define GRNB "\e[42m"
#define YELB "\e[43m"
#define BLUB "\e[44m"
#define MAGB "\e[45m"
#define CYNB "\e[46m"
#define WHTB "\e[47m"

//High intensty background 
#define BLKHB "\e[0;100m"
#define REDHB "\e[0;101m"
#define GRNHB "\e[0;102m"
#define YELHB "\e[0;103m"
#define BLUHB "\e[0;104m"
#define MAGHB "\e[0;105m"
#define CYNHB "\e[0;106m"
#define WHTHB "\e[0;107m"

//High intensty text
#define HBLK "\e[0;90m"
#define HRED "\e[0;91m"
#define HGRN "\e[0;92m"
#define HYEL "\e[0;93m"
#define HBLU "\e[0;94m"
#define HMAG "\e[0;95m"
#define HCYN "\e[0;96m"
#define HWHT "\e[0;97m"

//Bold high intensity text
#define BHBLK "\e[1;90m"
#define BHRED "\e[1;91m"
#define BHGRN "\e[1;92m"
#define BHYEL "\e[1;93m"
#define BHBLU "\e[1;94m"
#define BHMAG "\e[1;95m"
#define BHCYN "\e[1;96m"
#define BHWHT "\e[1;97m"

//Reset
#define reset "\e[0m"
#define CRESET "\e[0m"
#define LED_COLOR_RESET "\e[0m"


// useful macros below
#define clrscr()   printf("\e[1;1H\e[2J")
#define nonblock() fcntl(0, F_SETFL, fcntl(0, F_GETFL) | O_NONBLOCK);
#define block()    fcntl(0, F_SETFL, fcntl(0, F_GETFL) & ~O_NONBLOCK);

// LED_COLOR DEFINITION
enum  bg_color_index 
    {  NONE, AKA, AO,  KI,  MIDORI,SHIRO,KURO, maxColorIndex};
char *bg_color_attrib[]=
    {CRESET,REDB,BLUB,YELB, GRNB,   WHTB,BLKB}; 

enum  tx_color_index 
    {  TNONE,TAKA,TAO,TKI,TMIDORI,TSHIRO,TKURO, TmaxColorIndex};
char *tx_color_attrib[]=
    {CRESET, RED, BLU,YEL, GRN,    WHT,  BLK}; 

/////////////////////////////////////
// Change canvas size here LED_ROW, LED_COL//
//  Now, it is macro and user definable.
/////////////////////////////////////
#define LED_ROW   (led_max_ROW())    //24    //20  //16
#define LED_COL   (led_max_COL())    //16

#define defaultROW     45    //24    //20  //16
#define defaultCOL     15  //16

typedef struct CANVAS
{ char data;
  int  attrib;    //  attrib>>8 is text color, 
                  //  attrib & 0xFF is background color
} CANVAS;

// CANVAS canvas[LED_ROW][LED_COL];

CANVAS **canvas;
static int maxROW, maxCOL;

/***  Set the size of canvas ***/
 

int led_canvas_setsize(int R, int C)
{int j;
 static int flag;

 if( flag ) 
 {  printf("ERROR: led_canvas_setsize may be called only once.%c%c", 0xA, 0xD);
    exit(0);
 }
 if(flag == 0)
 { flag = 1;
  if((R==0) && (C==0))
  {
  maxROW=defaultROW;
  maxCOL=defaultCOL;
  }
  else
  { 
  maxROW=R;
  maxCOL=C;
  }

  canvas = (CANVAS **)(malloc(maxROW * sizeof(CANVAS *)));
  // canvas is freed in reset_terminal_mode()
  // This assumes the user did 

  if( canvas == NULL )
   {  printf("led_canvas_setsize() : Memory allocationn faied\n");
      exit(0);
   }
  for(j=0; j<maxROW; j++)
    canvas[j] = (CANVAS *)malloc(maxCOL * sizeof(CANVAS ));
 }
}

int led_max_ROW()
{ return(maxROW);
}
int led_max_COL()
{ return(maxCOL);
}


/***************************************************
   The following two functions:
   reset_terminal_mode() and 
   set_terminal_mode() are meant 
   to be used together.
***************************************************/
struct termios orig_termios;


////////////////////////////////////////////////////////////////////
//  reset_terminal_mode() assumes:                                //
//     The user called set_terminal_reset(), which does malloc()  //
//     and does callback atexit(reset_terminal_mode);             //
////////////////////////////////////////////////////////////////////
void led_canvas_free()
{
  if( canvas )
  { //  printf("FREEing\n");
     free(canvas);
  }
  else
     printf("Error on freeing canvas %c%c", 0xA, 0xD);
}

void reset_terminal_mode()
{ tcsetattr(0, TCSANOW, &orig_termios);
  led_canvas_free();
}


void set_terminal_reset()
{ 
/* This function and reset_terminal_mode() above are 
 * originally copied from (2022/06/13):
 * itecnote.com/tecnote/r-c-non-blocking-keyboard-input
 * Comments rewritten by me for students.
 */

  struct termios new_termios;  // storage for terminal mode 

  // copy current terminal mode into orig_termios
  // orig_termios is to be used by reset_terminal_mode() to 
  // restore the terminal mode.

    tcgetattr(0, &orig_termios);  // copy current mode
    memcpy(&new_termios, &orig_termios, sizeof(new_termios));

    /* atexit() register cleanup handler at exit of this program, 
       by running reset_terminal_mode() defined above. 
       If the user dies before exit is executed,
       the result is unknown,
       If you want to reset by yourself, then
       call set_terminal_no_reset() below and 
       call reset_terminal_mode() above whereve you want to exit.
    */
    atexit(reset_terminal_mode); // run reset_terminal_mocde() at exit

   // make raw mode data into new_termios  
    cfmakeraw(&new_termios);
   // set terminal with new_termios
    tcsetattr(0, TCSANOW, &new_termios);
}
/***************************************************/



/**** set terminal RAW mode with NO restoring ****/
void set_terminal_no_reset()
{
/* This function does not reset the terminal
 */

  struct termios new_termios;

    tcgetattr(0, &orig_termios);
    memcpy(&new_termios, &orig_termios, sizeof(new_termios));
    cfmakeraw(&new_termios);
    tcsetattr(0, TCSANOW, &new_termios);
}


void set_nonblock_terminal()
{
  struct termios new_termios;

    tcgetattr(0, &orig_termios);
    memcpy(&new_termios, &orig_termios, sizeof(new_termios));
    cfmakeraw(&new_termios);
    tcsetattr(0, TCSANOW, &new_termios);
}

//void set_conio_terminal_mode()
//{
//  struct termios new_termios;
//
//    /* take two copies - one for now, one for later */
//    tcgetattr(0, &orig_termios);
//    memcpy(&new_termios, &orig_termios, sizeof(new_termios));
//
//    /* register cleanup handler, and set the new terminal mode */
//    atexit(reset_terminal_mode);
//    cfmakeraw(&new_termios);
//    tcsetattr(0, TCSANOW, &new_termios);
//}



/***********************************
 * read one byte from the keyboard * 
 ***********************************/

char getkbchar()
{char ch;

     ch= 0;
     if( read (0, &ch, 1)<0 ) 
     { //nonblocking ends up with an error, -1
       // so, do not process any at this moment
       //printf("error read()\n");
     }
     return( ch );
}

/***********************************
*    Drawing functions             *
***********************************/

int led_canvas_clear()
{ int i,j;

	for(i=0; i<LED_ROW; i++)
	{  for(j=0; j<LED_COL; j++)
           {	canvas[i][j].data = NONE;
                canvas[i][j].attrib = 0;
	   }
        }
}


char led_canvas_peek(int i, int j, char *attrib, char *data)
{
   *attrib = canvas[i][j].attrib;
   *data   = canvas[i][j].data;
}


int led_canvas_display()
{
 int i, j, color;

       //printf("%c%c", 0x0A, 0x0D);
       //printf("%c", 0x0D);

       clrscr(); // clear scrn, print starts at upper-left
       printf(" ");
       for(i=0; i<LED_COL; i++)
       //for(i=0; i<LED_COL+2; i++)
       printf("-");
       printf("%c%c", 0x0A, 0x0D);

       for(i=0; i<LED_ROW; i++)
       {
         printf("%c", 0x0D);
         printf("|");
	 for(j=0; j<LED_COL; j++)
         {// printf("%d %d\n", i,j);
             if( canvas[i][j].attrib == 0)
             { color = canvas[i][j].data;
	       if ( (color<0) || ( color>maxColorIndex))
	       {  printf("\nError in color Index (led_canvas_displa)%c%c",0xD, 0xA);
                  printf("color= %d\n", color);
	          exit(0);
	       }

	       printf(bg_color_attrib[color]);
	       printf(" ");
	       //printf(CRESET);
             }
             //else if( canvas[i][j].attrib == 1)
             else
	     { //printf(CRESET);
               int fg, bg;
               fg = (canvas[i][j].attrib)>>8; 
               bg = (canvas[i][j].attrib) & 0xFF; 
               printf(tx_color_attrib[fg]);
               printf(bg_color_attrib[bg]);
               printf("%c", canvas[i][j].data);
             }
         }
         printf(CRESET);
         printf("|%c%c", 0x0A, 0x0D);
       }
       printf(CRESET);
       printf(" ");
       for(i=0; i<LED_COL; i++) //for(i=0; i<LED_COL+2; i++)
          printf("-");
       printf("%c%c", 0x0A, 0x0D);

}

/*************** * set canvas pixel color * ***************/ 
int led_canvas_set_pixel(int row, int col, char color, ...)
{ int j;
  va_list args;
  va_start(args, color);

	if( (color<0) || (color>=maxColorIndex))
	{   printf("\nError in colorIndex (led_canvas_set_pixel)\n");
	    printf("color must be 0 ~ %d\n", maxColorIndex);
	    printf("color=%d\n", color);
            j = va_arg(args, int);
            printf("location at = %d\n", j);
	    exit(0);
	}
	if((row >= LED_ROW) || (col >= LED_COL))
	{   printf("Error led_canvas_set_pixel  %c%c",0xD, 0xA);
	    printf("maxROW=%d maxCOL=%d  %c%c", LED_ROW-1, LED_COL-1, 0xD, 0xA);
	    printf("got row=%d and col=%d %c%c",0xD, 0xA);
            j = va_arg(args, int);
            printf("location at = %d% c%c",j, 0xD, 0xA);
	    exit(0);
	}
	else
        {   canvas[row][col].data = color;
            canvas[row][col].attrib = 0;
	}
	return(0);
}




/**************  TEXT CANVAS  *************/

/**************** clear text field *******************/
int text_canvas_clear()
{ int i,j;
	for(i=0; i<LED_ROW; i++)
	   for(j=0; j<LED_COL; j++)
           {	canvas[i][j].data= ' ';
            	canvas[i][j].attrib= (TKURO<<8)|KURO;
	   }
}


/************** text canvas display ****************/
int text_canvas_display()
{
 int i, j;

       //printf("%c%c", 0x0A, 0x0D);
       //printf("%c", 0x0D);

       clrscr(); // clear scrn, print starts at upper-left
       printf(" ");
       for(i=0; i<LED_COL; i++)
       //for(i=0; i<LED_COL+2; i++)
       printf("-");
       printf("%c%c", 0x0A, 0x0D);

       for(i=0; i<LED_ROW; i++)
       {
         printf("%c", 0x0D);
         printf("|");
	 for(j=0; j<LED_COL; j++)
         {// printf("%d %d\n", i,j);

	     printf("%c", canvas[i][j].data);
	     //printf(CRESET);
         }
         printf(CRESET);
         printf("|%c%c", 0x0A, 0x0D);
       }
       printf(CRESET);
       printf(" ");
       for(i=0; i<LED_COL; i++) //for(i=0; i<LED_COL+2; i++)
          printf("-");
       printf("%c%c", 0x0A, 0x0D);

}



/*************************** set text canvas **************************/ 
int text_canvas_write_char(int row, int col, char ch, char fg, char bg, ...)
{ int j;

  va_list args;
  va_start(args, bg);

	if((row >= LED_ROW) || (col >= LED_COL))
	{   printf("Error text_canvas_write_char%c%c", 0xA, 0xD);
	    printf("maxROW=%d maxCOL=%d%c%c", LED_ROW-1, LED_COL-1, 0xA, 0xD);
            j = va_arg(args, int);
	    printf("got row=%d and col=%d at loc=%d\n", row, col, j);
	    exit(0);
	}
	else
        {   canvas[row][col].data = ch;
            canvas[row][col].attrib =  (fg<<8) | bg; 
	}
	return(0);
}
