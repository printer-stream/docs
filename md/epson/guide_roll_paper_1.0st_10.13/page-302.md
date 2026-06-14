EXECUTING + SETTING 

## **C O N F I D E N T I A L** 

## **FS q** 

[Name] Define NV bit image 

[Format] ASCII FS q n [xL xH yL yH d1...dk]1...[xL xH yL yH d1...dk]n Hex 1C 71 n [xL xH yL yH d1...dk]1...[xL xH yL yH d1...dk]n Decimal 28 113 n [xL xH yL yH d1...dk]1...[xL xH yL yH d1...dk]n 

[Printers not featuring this command] TM-L90, TM-P60, TM-U230 

[Range] TM-J2000/J2100: **1** ≤ n ≤ **255** 

**1** ≤ **(** xL **+** xH × **256)** ≤ **1023 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **3)** 

- **1** ≤ **(** yL **+** yH × **256)** ≤ **576 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **2)** 

- **0** ≤ d ≤ **255** k **= (** xL **+** xH × **256)** × **(** yL **+** yH × **256)** × **8 The definition area is maximum 384 KB** 

TM-T90: 

- **1** ≤ n ≤ **255** 

- **1** ≤ **(** xL **+** xH × **256)** ≤ **1023 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **3) 1** ≤ **(** yL **+** yH × **256)** ≤ **288 (0** ≤ yL ≤ **255,** yH **= 0, 1)** 

**0** ≤ d ≤ **255** k **= (** xL **+** xH × **256)** × **(** yL **+** yH × **256)** × **8 The definition area is maximum 384 KB** 

## TM-T70, TM-T20, TM-T88IV, TM-T88V: 

- **1** ≤ n ≤ **255** 

- **1** ≤ **(** xL **+** xH × **256)** ≤ **1023 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **3)** 

- **1** ≤ **(** yL **+** yH × **256)** ≤ **288 (0** ≤ yL ≤ **255,** yH **= 0, 1)** 

**0** ≤ d ≤ **255** k **= (** xL **+** xH × **256)** × **(** yL **+** yH × **256)** × **8 The definition area is 256 KB** TM-U220: **1** ≤ n ≤ **255 1** ≤ **(** xL **+** xH × **256)** ≤ **1023 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **3) 1** ≤ **(** yL **+** yH × **256)** ≤ **288 (0** ≤ yL ≤ **255,** yH **= 0, 1) 0** ≤ d ≤ **255** k **= (** xL **+** xH × **256)** × **(** yL **+** yH × **256)** × **8 The definition area is 128 KB** 
