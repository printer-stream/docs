Rev.2.52 

## **4-3-7 STAR Original Auto Logo Commands** 

This command functions to print logos, like the one below, by only changing the product name, when only product names can be changed in systems that are already in use.  Also, this function has two operating modes. 

## **1) Standard Auto Logo Function** 

The Auto Logo function is preset and executes the following operations using the print cut command under the current system as a trigger. 

1. Starts up the Auto Logo function using the current system cut command as a trigger 

2. Prints if there is print data in the image buffer 

3. Executes user macro 1 

4. Prints Auto Logo 

5. Executes user macro 2 

Logo 2 is printed by #4 Auto Logo printing according to the command character “/” that was preset in the current print data and embedding the Logo number “2” to print.  Specifically, if the product is registered with “CHEESEBURGER/2” the logo 2 coupon ticket is automatically printed for the purchaser of a cheese burger. Also, Logo 1 for the header is used for company logos.  By registering to the user macro 2 of #5, cut command + Logo 1 print command, the company logo of logo1 will be printed.  User macro 1 of #3 is used when it is necessary to position the Auto Logo in the center.  When doing so, register the left alignment command using the user macro 2 of #5 and return to its original setting. 

**==> picture [511 x 366] intentionally omitted <==**

**----- Start of picture text -----**<br>
********************      Header Logo1<br> MCDONALD’S<br>******************** ********************����������������<br>1 CHEESEBURGER.     $2.00  ������������<br> MCDONALD’S<br>2 .COKE                  $1.00<br>********************����������������<br>----------------------- -- --------  1.��������������������������CHEESEBURGER    $2.00<br>TOTAL                   $3.00 2���������������������.COKE                   $1.00 ����������<br>-----------------------TOTAL                    $3.00����������������������� -- --------  Print DataCurrent System<br>������ ���������������������<br>1. AutoLogo triggered by cut<br>Partial Cut<br>command<br>Current System Print Data 3. User macro 1 executed<br>������������ Cheeseburger   ������<br>Partial Cut<br>4. AutoLogo printed<br>      COKE<br>Logo3<br>5. User macro 2 executed<br> Paper is cut<br> Header logo is printed      Header<br>********************<br> MCDONALD’S<br>**----- End of picture text -----**<br>


ESC/POS Command Specifications 

205 
