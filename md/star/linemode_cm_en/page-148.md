|**ESC GS y D 1 m nL nH d1 d2 … dk**|**ESC GS y D 1 m nL nH d1 d2 … dk**|**ESC GS y D 1 m nL nH d1 d2 … dk**|||||
|---|---|---|---|---|---|---|
|[Name]|Set QR code cell size (Auto Setting)||||||
|[Code]|ASCII|ESC GS<br>y<br>D<br>1<br>m<br>nL<br>nH|d1|d2|…|dk|
||Hex.|1B<br>1D<br>79<br>44<br>31<br>m<br>nL<br>nH|d1|d2|…|dk|
||Decimal|Decimal<br>27<br>29 121<br>68<br>49<br>m<br>nL<br>nH|d1|d2|…|dk|
|[Defined Area]||m = 0|||||
|||0≤<br> nL≤<br> 255, 0≤<br> nH≤<br> 255|||||
|||1≤<br> nL + nH x 256≤<br> 7089 (k = nL + nH x 256)|||||
|||0≤<br> d≤<br> 255|||||
|[Initial Value]||---|||||
|[Function]|[Function]|Automatically expands the data type of the bar code and sets the data.|||Automatically expands the data type of the bar code and sets the data.||
|||• Parameter details|||||
|||• nL + nH x 256: Byte count of bar code data|||||
|||• dk: Bar code data (Max. 7089 bytes)|||||
|||• When using this command, the printer receives data for the number of bytes (k) specified by nL|||||
|||and nH.  The data automatically expands to be set as the bar code data.|||||
|||• Indicates the number bytes of data specified by the nL and nH.|• Indicates the number bytes of data specified by the nL and nH.|||• Indicates the number bytes of data specified by the nL and nH.|
|||Bar code data is cleared at this time.|||||
|||• The data storage region of this command is shared with the manual setting command so data is|||||
|||updated each time either command is executed.|||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-130 
