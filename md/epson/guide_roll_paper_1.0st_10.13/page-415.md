## **C O N F I D E N T I A L** 

TM-U230 **: Function A** m **= 1, 49 Function B** m **= 66; 0** ≤ n ≤ **255 Function C** m **= 98; 0** ≤ n ≤ **255** 

[Default] None 

## [Printers not featuring this command] None 

## [Description] Executes paper cutting specified by m, as follows: 

|m||**Function**|
|---|---|---|
|<A>|0, 48|Executes a full cut (cuts the paper completely).|
||1, 49|Executes a partial cut (one point left uncut).|
|<B>|65|Feeds paper to (cutting position +n ×vertical motion unit) and executes a full cut (cuts<br>the paper completely).|
||66|Feeds paper to (cutting position +n ×vertical motion unit) and executes a partial cut<br>(one point left uncut).|
|<C>|97|Specifies a paper cutting range to (basic paper feed amount + [n ×vertical motion unit]<br>and executes a full cut.|
||98|Specifies a paper cutting range to (basic paper feed amount + [n ×vertical motion unit]<br>and executes a partial cut (one point left uncut).|
|<D>|103|Feeds paper to (cutting position +n ×vertical motion unit) and executes a full cut (cuts<br>the paper completely), then feeds paper to the print start position.|
||104|Feeds paper to (cutting position +n ×vertical motion unit) and executes a partial cut<br>(one point left uncut), then feeds paper to the print start position.|



- n of <B> and <D> specify paper feed amount executed immediately before a paper cut. 

- n of <C> specifies a range of paper cut. 

## [Notes for <A>, <B>,<C>, and <D>] 

- When standard mode is selected, these commands are enabled only when processed at the beginning of the line. 
