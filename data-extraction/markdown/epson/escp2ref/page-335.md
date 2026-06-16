## Programming examples

This section provides several programming examples that take advantage of the new features of the Stylus COLOR and later printer models. The following examples are not inclusive. Therefore, the specific driver commands you use will depend on the application.

## Example 1: ESC/P 2 color multipoint font driver

## Step 1 Start Job

ESC @ initialize the printer, reset printer to defaults

## Step 2 Set Specific Configuration

ESC ( U set units ESC ( t assign character table ESC ( C set page length in defined unit-continuous paper only ESC ( c set page format-top and bottom margins ESC X set pitch before setting left and right margins (ESC P, ESC M, ESC g) ESC l &amp; ESC Q set left and right margins ESC = set line spacing n/360'

## Step 3 Adjust Vertical Print Position (if necessary)

ESC ( V absolute position in units ESC ( v relative position in units LF line feed FF form feed

## Step 4 Adjust Horizontal Print Position (if necessary)

ESC $ absolute position in units ESC \ relative position in units CR carriage return

## Step 5 Output Text

ESC r n select printing color where n = 0 Black 1 Magenta 2 Cyan 3 Violet 4 Yellow 5 Red 6 Green
