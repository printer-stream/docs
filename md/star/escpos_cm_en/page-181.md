Rev.2.52 

## **4-3-4 STAR Original Commands** 

STAR original commands are not regulated by the ESC/POS control codes, but are standard for improved functions and for independent STAR functions. 

## **ESC GS = nL nH da1 … dak db1 …dbk** 

Name Write data to a blank code page Code ASCII ESC GS = nL nH da1...dak db1...dbk Hex. 1B 1D 3D nL nH da1...dak db1...dbk Decimal 27 29 61 nL nH da1...dak db1...dbk nL = 0 Defined Region nH = 48 1 ≤ nL+ (nH x 256) 0 ≤ da ≤ 255 (Font-A Data) 0 ≤ db ≤ 255 (Font-B Data) k = nL+ (nH x 256) ÷ 2 

- Function • Stores blank code page data in non-volatile memory. Details • A blank code page is a character code table that is completely free of character codes 80H to FFH.  It is selected when the character code table selection command (ESC tn) sets n = 255, or (ESC GS t n) sets n = 255. 

   - The following are data that is written to the blank code page. Font-A: 1 Character = 48 bytes; 6144 bytes = 48 bytes x 128 characters Font-B: 1 Character = 48 bytes; 6144 bytes = 48 bytes x 128 characters • Font-A data and Font-B data is sent continuously. 

• The printer is reset after writing with to the non-volatile memory. Reference ESC t, ESC GS t, Appendix-3 

ESC/POS Command Specifications 

181 
