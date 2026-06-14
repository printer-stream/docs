## **3.3.15. Kanji characters** 

**ESC p** [Name] Specify JIS Kanji character mode [Code] ASCII ESC p Hex. 1B 70 Decimal 27 112 [Defined Area] - - - [Initial Value] JIS Kanji character mode cancelled [Function] Specifies JIS Kanji character mode When in JIS Kanji character mode, character codes are all handled as 2 byte Kanji characters (First byte: upper code; second byte: lower code). This command is ignored for models not equipped with Japanese and Kanji characters and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch.  In such a case, this is handled as the ANK font 14 dot pitch specification command. 

## **ESC q** 

[Name] Cancel JIS Kanji character mode [Code] ASCII ESC q Hex. 1B 71 Decimal 27 113 [Defined Area] - - - [Initial Value] JIS Kanji character mode cancelled [Function] Cancel JIS Kanji character mode 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-59 
