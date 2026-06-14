## **3.3.9. Logo** 

|**ESC FS q n**|**ESC FS q n**|**ESC FS q n [x11 x12 y11 y12 d1...dk]1...[xn1 xn2 yn1 yn2 d1...dk]n**|||
|---|---|---|---|---|
|[Name]|Register logo|Register logo|||
|[Code]|ASCII|ESC<br>FS<br>q<br>n [x11 x12 y11 y12<br>d1<br>... dk]1<br>... [xn1 xn2 yn1 yn2|d1|... dk]n|
||Hex.|1B<br>1C<br>71<br>n [x11 x12 y11 y12<br>d1<br>... dk]1<br>... [xn1 xn2 yn1 yn2|d1|... dk]n|
||Decimal|Decimal<br>27<br>28 113<br>n [x11 x12 y11 y12<br>d1<br>... dk]1<br>... [xn1 xn2 yn1 yn2|d1|... dk]n|
|[Defined Area]||1≤<br>n≤<br>255|||
|||0≤<br>xn1≤<br>255,0≤<br>xn2≤<br>3|||
|||1≤<br>(xn1 + xn2 x 256)≤<br>1023|||
|||0≤<br>yn1≤<br>255,0≤<br>yn2≤<br>1|||
|||1≤<br>yn1 + yn2 x 256)≤<br>288|||
|||0≤<br>d≤<br>255|||
|||k = {(xn1 + xn2 x 256) x (yn1 + yn2 x 256) x 8}|||
|[Initial Value]||- - -|||
|[Function]|[Function]|Parameter details|||
|||• n:<br>Specifies registered logo count|||
|||• xn1, xn2: Horizontal size of registered logo {(xn1 + xn2 x 256) x 8} dots|||
|||• yn1, yn2: Vertical size of registered logo {(yn1 + yn2 x 256) x 8} dots|||
|||• d:<br>Registered logo data|||
|||• k:<br>Logo data count|||
|||This command should be specified at the top of the line.|||
|||When the first parameter is determined to be free of error, the printer starts processing this||When the first parameter is determined to be free of error, the printer starts processing this|
|||command.|||
|||When logo register processing starts, all previously defined data is deleted.|||
|||(It is not possible to reregister a portion of a plurality of defined logo data.)|||
|||Logo registration numbers are defined in rising order from 1.|||
|||If the defined area specified by the parameter is not empty, or if there is an error in the parameter||If the defined area specified by the parameter is not empty, or if there is an error in the parameter|
|||specification, register processing is aborted.  (The pre-registered and complete data is effective.)||specification, register processing is aborted.  (The pre-registered and complete data is effective.)|
|||The printer should be initialized if logo registration is completed or register processing is aborted.|||
|||If an error occurs while performing register processing (the time from when the first parameter is|||
|||OK until the printer initialization is completed after registering a logo), error processing, mechanical|||
|||operation and status processing cannot be performed.|||
|||The relationships between input data and the actual print are shown on the next page.||The relationships between input data and the actual print are shown on the next page.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-38 
