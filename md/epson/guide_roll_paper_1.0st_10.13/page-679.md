EXECUTING COMMAND 

## **C O N F I D E N T I A L** 

## **FS 2 g** 

[Name] Read from NV user memory 

[Format] ASCII FS g 2 m a1 a2 a3 a4 nL nH Hex 1C 67 32 m a1 a2 a3 a4 nL nH Decimal 28 103 50 m a1 a2 a3 a4 nL nH 

- [Printers not featuring this command] TM-J2000/J2100, TM-T90, TM-L90, TM-P60, TM-U230, TM-U220 

- [Range] TM-T20, TM-T88IV, TM-T88V: 

**m = 0** 

**0** ≤ **(a1 + a2** × **256 + a3** × **65536** + **a4** × **16777216)** ≤ **1023 (0** ≤ **a1** ≤ **255, 0** ≤ **a2** ≤ **3, a3 = 0, a4 = 0) 1** ≤ **(nL + nH** × **256)** ≤ **80  (1** ≤ **nL** ≤ **80, nH = 0)** TM-T70: **m = 0** 

**0** ≤ **(a1 + a2** × **256 + a3** × **65536** + **a4** × **16777216)** ≤ **1023 (0** ≤ **a1** ≤ **255, 0** ≤ **a2** ≤ **3, a3 = 0, a4 = 0) 1** ≤ **(nL + nH** × **256)** ≤ **80  (0** ≤ **nL** ≤ **80, nH = 0)** 

- [Description] Transmits the data in NV user memory. 

   - a1 _**,**_ a2 _**,**_ a3 **,** and a4 specify the starting address of transmission data as 

      - (a1 + a2 × 256 + a3 × 65536 + a4 × 16777216). 

   - nL and nH specify the amount of transmission data as (nL + nH × 256) bytes. 

## [Recommended Functions] 

- This is an unrecommended command. It is supported by some printer models but will not be supported by future models. 

- GS ( C is recommended to write to NV user memory. Operation of GS ( C offers the following improvements: 

   - Data can be controlled by record. 

   - Each record can be redefined, retrieved, or deleted by keycode. 

   - Memory can be used efficiently because the printer controls the data. 

   - Transmission data can be identified. 
