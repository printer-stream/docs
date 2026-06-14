## **C O N F I D E N T I A L** 

|**(**nL**+**nH ×**256) **|**Print speed**|**Print speed**|
|---|---|---|
|**7**|**Print speed level 7**|**|**|
|**8**|**Print speed level 8**|**|**|
|**9**|**Print speed level 9**|**Fast**|



■ **Thai character print mode setting (a = 7)** 

|**(nL + nH**×**256)**|**Thai characterprint mode**|
|---|---|
|**0**|**Thai 3pass**|
|**1**|**Thai 1pass**|



- **Number of division of thermal head energizing (** a **= 97)** 

|**(**nL**+**nH ×**256) **|**Division number**|
|---|---|
|**1**|**Divide into one**|
|**2**|**Divide into two**|
|**4**|**Divide into four**|
|**128**|**Automatic control**|



   - **When "Automatic control (128)" is selected, normally printing is performed with one-part energizing, and when high duty data is printed, there is a possibility that printing is performed temporarily with two-part energizing.** 

   - **The Japanese specification (paper width 80 mm) does not support "Divide into four" and “Automatic control”.** 

   - **The Japanese specification (paper width 58 mm) does not support "Divide into four".** 

- **Setting the TM-T88IV command-compatible mode (a = 120)** 

|**(**nL**+**nH ×**256) **|**Mode**|**Japanese Model**|**Other model**|
|---|---|---|---|
|**0**|**Disables the TM-T88IV-compatible mode.**|**--**|**Y (Default)**|
|**1**|**Enables the TM-T88IV-compatible mode.**|**--**|**--**|



## TM-L90 

**We recommend that Number of division of thermal head energizing be set to Divide into two for best print quality in 2-color printing.** 
