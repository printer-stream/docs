<!-- image -->

## 6-5-2 Usage	Example	of	Page	Mode

This section provides a detailed description of how to use the page mode.

The following outlines the representative command transmission procedures when using the page mode.

1. Page mode is used by the printer receiving the ESC L (Select page mode) command.
2. The print region is specified by the ESC W (Select print region in page mode) command.
3. The print direction is specified by the ESC T (Select character print direction in page mode) command.
4. Send print data.
5. The printer prints the print data send, using the FF (Print and recover page mode) command.
6. After printing, the printer recovers to standard mode.

&lt;Example 1: Sample Program using Basic&gt;

- (It is already possible to send to the printer using file #1 with an OPEN statement.) 100 PRINT #1,   CHR$(&amp;H1B); 'L'; 110 PRINT #1, CHR$(&amp;H1B); 'W'; CHR$(0); CHR$(0); CHR$(0); CHR$(0); 120 PRINT #1, CHR$(200); CHR$(0); CHR$(144); CHR$(1); 130 PRINT #1, CHR$(&amp;H1B); 'T'; CHR$(0); 140 PRINT #1, 'Page mode lesson TEST 1'
- 150 PRINT #1, CHR$(&amp;HC);

With the program in example 1, the print region of the size of 200 x 400 pitch is ensured from the origin point (0,0). Printing is performed on that first line.

<!-- image -->

The reason for the line break between lesson and Test 1 in the figure above is because it was automatically in -serted due to the fact that a space could not be inserted after lesson in the horizontal direction in the print range of 200 x 400 pitch.  This line feed amount is a value specified by ESC 3 (Set line feed amount).  Also, several print regions can be set until FF is executed.  However, when print regions are overlapped, an OR operation is used for data that is newly written and data that was already written.

To delete only a portion of the buffered data, use the CAN (Cancel print data in page mode) command.  CAN de -letes all data in the print region currently specified.  Therefore, specify the print region that encloses the portion to delete using ESC W, then use the CAN command to delete that data.

However, be careful because the portion in the specified print region, even if a portion of the characters, will be deleted.
