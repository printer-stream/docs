ESC ( U

set units

ESC ( C

set page length in defined unit-continuous paper only

ESC ( c

set page format-top and bottom margins

ESC U

turn unidirectional mode on/off

## Adjust Vertical Print Position (if necessary)

ESC ( V

absolute position in units

ESC ( v

relative position in units

LF

line feed

FF

form feed

## Step 4 Adjust Horizontal Print Position (if necessary)

ESC $

absolute position in units

ESC \

relative position in units

CR

carriage return

## Step 5 Output Raster Graphics

```
ESC \ relative horizontal position in units ESC r n select printing color where n = 0 Black 1 Magenta 2 Cyan 4 Yellow ESC .c print raster graphics data where c = 0 uncompressed raster graphics 1 compressed raster graphics (RLE)
```

## Note:

Use data compression whenever possible to reduce file size and printing time.

CR

carriage return

Repeat steps as necessary within a graphics block-start with yellow and then follow command sequence with magenta, cyan, and black. If necessary, signal the end of the graphics band with a CR, LF, or vertical positioning command.

## Step 6 Repeat Above as Necessary within Page

Send FF command

Prompt user for paper if in single-sheet mode

## Step 7 End Job

ESC @

reset printer to defaults (exit raster graphics mode)
