Rev.2.52 

## **FS q n [xL xH yL yH d1...dk] 1... [xL xH yL yH d1...dk] n** 

Name Define NV bit image Code ASCII FS q n [xL xH yL yH d1...dk]1 ... [xL xH yL yH d1...dk] n Hex. 1C 71 n [xL xH yL yH d1...dk]1 ... [xL xH yL yH d1...dk] n Decimal 28 113 n [xL xH yL yH d1...dk]1 ... [xL xH yL yH d1...dk] n 1 ≤ n ≤ 255 Defined Region 0 ≤ xL ≤ 255 0 ≤ xH ≤ 3 However, 1 ≤  (xL+xH×256) ≤ 1023 0 ≤ yL ≤ 255 0 ≤ yH ≤ 1 However, 1 ≤  (yL+yH×256)  ≤ 288 0 ≤ d ≤ 255 k =  (xL+xH×256) × (yL+yH×256) ×8 Total defined data area = 2 M bytes (256 K bytes) Function Defines the specified NV bit image. • n specifies the number of NV bit images to define. 

   - xL and xH specify the horizontal direction for one NV bit image (xL + xH x 256) x 8 dots. 

   - yL and yH specify the vertical direction for one NV bit image (yL + yH x 256) x 8 dots. 

- Details • This command erases all previously defined NV bit images.  The printer cannot redefine only one of several data definitions that had been defined before. Therefore, all data must be resent. 

   - Mechanical operations (such as initializing the position of the print head when the cover is open, feeding paper using a switch) cannot be executed from the time this command commences its process until a hardware reset is completed. 

   - NV bit image is a bit image defined by this command in non-volatile memory and is printed by the FS p (Print NV bit image) command. 

   - This command is effective only when processed at the top of the line when standard mode is being used. 

   - When in page mode, this command is disabled. 

   - This command is effective when 7 bytes of FS to yH of the command are processed normally. 

   - When the amount of data exceeds the capacity left in the range defined by xL, xH, yL, yH, the printer processes an argument that is out of the defined range. 

   - This command is invalid when processing an argument that is out of the defined range with the initial NV bit image data. 

   - The printer terminates processing of this command and starts writing data to the non-volatile memory if an argument out of the defined range is processed on the second and subsequent NV bit image data.  This invalidates the NV bit image being defined (making it undefined), but the NV bit images prior to that are valid. 

   - d specifies defined data. Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0. 

   - An n number of NV bit images are defined in ascending order from 01H.  Therefore, The first data of [xLxHyLyHd1…dk] is an NV bit image of the number 01H.  The final data of [xLxHyLyHd1…dk] is the NV bit image of the number n. 

   - This matches with the NV bit image number that is specified for NV bit image printing (by FS p). 

ESC/POS Command Specifications 

83 
