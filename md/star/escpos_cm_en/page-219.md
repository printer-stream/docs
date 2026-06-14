Rev.2.52 

## **4-3-9 Two-dimensional Bar Code 2D Code PDF417 Command Details** 

This command prints two-dimensional bar code 2D code PDF417. 

There are four types of commands, according to functions, for two-dimensional bar code PDF417. 

- (1) Bar code type setting 

- (2) Bar code data setting 

- (3) Bar code printing 

(<ESC> <GS> “x” “S”) (<ESC> <GS> “x” “D”) (<ESC> <GS> “x” “P”) 

The following describes the functions in detail. 

## **(1) Bar code type setting** 

These commands set the bar code type. Because these are all set with default values, they should be used only when it is necessary to change.  (Refer to section below for details on each setting.) 

**==> picture [314 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
p1<br>START p2  STOP<br>**----- End of picture text -----**<br>


PDF417 is configured by a fixed bar pattern for starting and stopping, and a bar pattern called a code word. Code words are configured by 17 modules. 

**==> picture [116 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
4  1 1 1 1 1  3   5<br><Code Word><br>**----- End of picture text -----**<br>


<ESC> <GS> “x” “S” “0” specifies values of p1 and p2. 

USE_LIMITS mode specify the ratio of p1 and p2.  USE_FIXED mode specifies p1 (line count) and p2 (code word count per line). 

<ESC> <GS> “x” “S” “1” specifies values of error correction levels. 

PDF417 can read information even if a portion of the data is corrupted by using the error correction. By increasing this level, the bar code size increases because there is more preparatory information. 

<ESC> <GS> “x” “S” “2” and <ESC> <GS> “x” “S” “3” specify the size of the module that configures the code word. 

The X direction size (in dot increments) is determined by <ESC> <GS> “x” “S” “2” for the module, and <ESC> <GS> “x” “S” “3” specifies the Y direction size from the aspect. 

Module size setting is the basis for the bar code image that is generated, so the resulting print will vary according to that setting. 

**Printable size of bar code** 

Vertical Size [dots] Horizontal Size [dots] 640 640 ~~ee ee~~ 

ESC/POS Command Specifications 

219 
