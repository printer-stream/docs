## C O N F I D E N T I A L

- The 12th byte data is processed as a modular check character when processing data is 12 byte. In this case, modular check character is not checked.
- ■ Left guard bar/center bar/right guard bar are added automatically.

[Notes for UPC-E ( m = 66) process]

- ■ Some models do not support settings of 6, 7, or 8 bytes for the amounts of data to process. For details, refer to [Model Information].
- ■ If the amount of data to process is 6 bytes, the number system character (NSC) 0 is added automatically.
- ■ If the amount of data to process is any of (7, 8, 11, 12 bytes), the first data ( d1 ) is processed as number system character (NSC) so 0 must be specified.
- ■ If n is out of the specified range or if n is an odd number when ITF bar code system ( m = 70) is selected, this command is canceled and the following data is processed as normal data.
- ■ Modular check character (1 character) is processed as follows:
- If the amount of data to process is any of (6, 7, 11 bytes), it is added automatically.
- The 12th byte data is processed as a modular check character when processing data is 12 byte. In this case, modular check character is not checked.
- If the amount of data to process is 8 bytes, the 8th byte data is processed as a modular check character. However, the modular check character is not checked.
- Modular check characters are data to decide the bar pattern; they are not printing data.
- ■ Prints a 6-column short code that except NSC and modular check characters.
- If the amount of data to process is 6 bytes, the shortened 6-digit code specified by ( d1...d6 ) is printed.
- If the amount of data to process is either of (7, 8 bytes), the shortened 6-digit code specified by ( d2...d7 ) is printed.
