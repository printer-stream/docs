• n4 bar code height (dot count) 

Specification A 

When the height of the bar code is more than the form feed amount, the form feed amount is automatically doubled. 

Specification B 

Form feed at (Bar code height + underbar characters) 

• k (Bar code data count), d (Bar code data) 

|Barcode type<br>~~a~~|Defined area of k|Defined area ofd|
|---|---|---|
|UPC-E<br>~~a~~|11≤<br>k≤<br>12|48≤<br>d≤<br>57 (”0”≤<br>d≤<br>”9”)|
|UPC-A<br>~~a~~<br>~~a~~|11≤<br>k≤<br>12<br>~~a~~|57 (<br>)<br>48≤<br>d≤<br>57(”0”≤<br>d≤<br>”9”)|
|JAN/EAN8<br>~~a ~~<br>~~a~~|7≤<br>k≤<br>8<br> ~~a~~<br>~~a~~|(<br>)<br>48≤<br>d≤<br>57(”0”≤<br>d≤<br>”9”)|
|JAN/EAN13<br>~~a~~|12≤<br>k≤<br>13<br>~~a~~|(<br>)<br>48≤<br>d≤<br>57(”0”≤<br>d≤<br>”9”)|
|Code39<br>~~ee~~|1≤<br>k<br>~~ee~~|(<br>)<br>48≤<br>d≤<br>57 (”0”≤<br>d≤<br>”9”)<br>65≤<br>d≤<br>90 (”A”≤<br>d≤<br>”Z”)<br>32, 36, 37,43,45,46,47(SP,”$”,”%”,”+”,”-“,”.”,”/”)<br>~~eee~~|
|ITF<br>~~ee ~~|1≤<br>k<br>When an odd number: 0 is<br>automatically applied to the<br>top.<br> ~~ee~~|48≤<br>d≤<br>57 (“0”≤<br>d≤<br>”9”)<br>~~eee~~|
|Code128<br>~~a~~|1≤<br>k|0≤<br>d≤<br>127|
|Code93<br>~~a~~|1≤<br>k|0≤<br>d≤<br>127|
|NW-7|1≤<br>k|48≤<br>d≤<br>57 (”0”≤<br>d≤<br>”9”)<br>65≤<br>d≤<br>68 (”A”≤<br>d≤<br>”D”)<br>36, 43, 45, 46, 47, 58 (”$”, ”+”, ”-“, ”.”, ”/”, ”:”)<br>97, 98, 99,100 (”a”,”b”,”c”,”d”)|



- UPC – E: k = 11 (or 12) 

The 12[th] check digit is automatically applied, so it is specified and ignored. The command is ignored for data that cannot be shortened. Automatically converts data to shortened form. 

• UPC – A: k = 11 (or 12) 

The 12[th] check digit is automatically applied, so it is specified and ignored. 

• JAN/EAN – 8: k = 7 (or 8) 

The 8[th] check digit is automatically applied, so it is specified and ignored. 

• JAN/EAN -13: k = 12 (or 13) 

The 13[th] check digit cannot be automatically applied, so it is specified and ignored. 

• CODE 39: k is freely set, and maximum value differs according to the mode. Start/stop code (“*”) is automatically applied. 

• ITF: k is freely set, and maximum value differs according to the mode. If data is oddly numbered, a 0 is applied to the top. 

• CODE 128: k is freely set, and maximum value differs according to the mode and the print character type. 

The check character is automatically applied. 

• CODE 93: k is freely set, and maximum value differs according to the mode and the print character type. 

The check character (“□”) is automatically applied. 

• NW7: k is freely set, and maximum value differs according to the mode and the print character type. 

Start/stop codes included in the data (not automatically applied). 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-43 
