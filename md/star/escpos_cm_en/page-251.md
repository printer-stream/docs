Rev.2.52 

## **<Function 48> ESC GS ) I pL pH fn d1 d2** 

Name Send the all kind of multibyte fonts Code ASCII ESC GS ) I pL pH fn d1 d2 Hex. 1B 1D 29 49 pL pH fn d1 d2 Decimal 27 29 41 73 pL pH fn d1 d2 

Defined Region pL = 3,  pH = 0 fn = 48 d1 = 0, d2 = 0 

Function Sends the all kind of multibyte font in the printer. 

Details Sends in the following format. 

ESC GS ) I pL pH fn k1 k2 [multibyte font kind1, multibyte font kind2, ..... ] LF NUL 

k1 and k2 indicate the number of transmission data bytes (k1 + k2 * 256) after the multibyte font types. 

When there are multiple multibyte font types in the printer, they are delimited by commas (2Ch). 

The kind of multibyte font is sent as character string data. 

|<br>(2Ch).<br>The kind of multibyte font is sent as|<br>character string data.|
|---|---|
|Kind of multibyte fonts|Transmittingstring|
|Japanese<br>|KANJI JAPANESE|
|Simplifed  Chinese GB2312<br>|CHINA GB2312|
|<br>Simplifed Chinese GB18030|CHINA GB18030|
|<br>Traditional Chinese BIG5|TAIWAN BIG-5|
|Korean|KOREA C-5601C|



Exemple:  When “Simplified Chinese GB18030" and "Traditional Chinese BIG5 " are installed in the printer: 

ESC GS ) I pL pH fn k1 k2 CHINA GB18030 , TAIWAN BIG-5 , LF NUL 

(k1 = 29, k2 =0) 

When the multibyte font is not installed in the printer, the following data is sent: 

ESC GS ) I pL pH fn k1 k2 LF NUL 

(k1 = 2, k2 =0) 

ESC/POS Command Specifications 

251 
