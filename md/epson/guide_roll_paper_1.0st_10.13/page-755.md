## **C O N F I D E N T I A L** 

## **GS ( E** _**pL pH fn a d1 d2**_ <Function 7> 

[Name] Copy the user-defined page [Format] ASCII GS ( E pL 

ASCII GS ( E pL pH fn a d1 d2 Hex 1D 28 45 04 00 07 a d1 d2 Decimal 29 40 69 2 0 7 a d1 d2 (pL + pH × 256) = 4 (pL = 4, pH = 0) fn = 7 

[Range] 

d1 = 30, 31 

d2 = 30, 31 (d1 ≠ d2) 

## TM-J2000/J2100, TM-T90 **,** TM-L90 **:** 

a **= 10, 12 (Other than Japanese model)** a **= 12, 17, 18 (Japanese model)** 

TM-P60 **:** a **= 12, 17, 18** 

- [Description] Copies the data in the user-defined code page. 

   - Font number is specified by a. 

|a|**User defined code page**|**Number of**<br>**horizontal dots**|**Number of**<br>**vertical dots**|
|---|---|---|---|
|10|Font configuration 9×14 (page 255)|9|17|
|12|Font configuration 12×24 (page 255)|12|24|
|17|Font configuration 8×16 (page 255)|8|16|
|18|Font configuration 10×24 (page 255)|10|24|



- Copy operation is specified by d1, d2. 

|d1|d2|**Copy operation**|
|---|---|---|
|31|30|Copy the font number data (a) from the storage area into the work area|
|30|31|Copy the data from the work area into the storage area specified by font number<br>(a)|
