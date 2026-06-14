## **C O N F I D E N T I A L** 

- **1** ≤ **(** xL **+** xH × **256)** ≤ **8192 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **32)** 

## TM-T20 **:** 

   - **1** ≤ **(** yL **+** yH × **256)** ≤ **2304 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **9)** c **= 49 (when the recommended monochrome paper is used)** c **= 49, 50 (when the recommended two-color paper is used)** b **= 1** 

   - **1** ≤ **(** xL **+** xH × **256)** ≤ **8192 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **32) 1** ≤ **(** yL **+** yH × **256)** ≤ **2304 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **9)** c **= 49** 

- TM-T88IV **:** b **= 1 (when single-color printing control is selected)** 

   - b **= 1, 2 (when two-color printing control is selected)** 

   - **1** ≤ **(** xL **+** xH × **256)** ≤ **8192 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **32)** 

- **1** ≤ **(** yL **+** yH × **256)** ≤ **2304 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **9)** c **= 49 (when single-color printing control is selected)** c **= 49, 50 (when two-color printing control is selected)** 

- TM-T88V **:** b **= 1 (when** a **= 48)** 

   - **1** ≤ b ≤ **4 (when** a **= 52)** 

   - **1** ≤ **(** xL **+** xH × **256)** ≤ **8192 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **32)** 

   - **1** ≤ **(** yL **+** yH × **256)** ≤ **2304 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **9)** c **= 49 (when** a **= 48)** 

   - **49** ≤ c ≤ **52 (when** a **= 52)** 

- TM-T70 **:** b **= 1** 

   - **1** ≤ **(** xL **+** xH × **256)** ≤ **8192 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **32)** 

   - **1** ≤ **(** yL **+** yH × **256)** ≤ **2304 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **9)** c **= 49** 

TM-P60 **:** 

      - b **= 1** 

      - **1** ≤ **(** xL **+** xH × **256)** ≤ **1024 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **4) 1** ≤ **(** yL **+** yH × **256)** ≤ **1200 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **4)** c **= 49** 

- [Description] Defines the NV graphics data (raster format) as a record specified by the key codes (kc1 and kc2) in the NV graphics area. 

   - b specifies the number of colors for the defined data. 

   - xL and xH specify the number of dots in the horizontal direction as (xL + xH × 256). 
