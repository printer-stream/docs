ESC t

select character table

ESC X

select font by pitch and point-multipoint mode

ESC k

select typeface (see ESC k command description for latest font

parameters)

ESC 4 &amp; ESC 5

italic on/off

ESC E &amp; ESC F

bold on/off

ESC ( -

select line/score

ESC q

character style-outline/shadow

Send data to be printed

Repeat as necessary within line Signal end of line-use CR, LF, or vertical positioning

## Step 6 Repeat Above as Necessary within Page

## Step 7 End Page

Send FF command

Prompt user for paper if in single-sheet mode

## Step 8 End Job

ESC @ reset printer to defaults

Example 2: MicroWeave ESC/P 2 standard color raster graphics and RLE compressed raster graphics driver

## Step 1 Start Job

ESC @

initialize the printer, reset printer to defaults

## Step 2 Enter Raster Graphics Mode

ESC ( G

## Note:

- The appropriate driver commands depend on the application.
- New or expanded ESC/P 2 commands are shown in bold.

## Step 3 Set Specific Configuration

ESC ( i 01 00 n turn MicroWeave on/off where n = 0 MicroWeave off 1 MicroWeave on

## Note:

- If the EPSON ESC/P 2 printer does not support MicroWeave, it will ignore the ESC ( i command. High-resolution color printers, including the Stylus COLOR, support MicroWeave.
- Execute the ESC ( i command prior to paper feed.

select graphics mode
