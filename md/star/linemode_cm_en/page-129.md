## **3.10. AUTO LOGO Function Command Details** 

This command functions to print logos, like the one below, by only changing the product name, when only product names can be changed in systems that are already in use.  Also, this function has two operating modes. 

## 1) Standard Auto Logo Function 

The Auto Logo function is preset and executes the following operations using the print cut command under the current system as a trigger. 

1. Starts up the Auto Logo function using the current system cut command as a trigger 

2. Prints if there is print data in the image buffer 

3. Executes user macro 1 

4. Prints the Auto Logo 

5. Executes user macro 2 

**==> picture [471 x 419] intentionally omitted <==**

**----- Start of picture text -----**<br>
Logo 2 is printed by #4 Auto Logo printing according to the command character “/” that was preset in the current print<br>data and embedding the logo number “2” to print. Specifically, if the product is registered with “CHEESE BURGER/2”<br>the logo 2 coupon ticket is automatically printed for the purchaser of a cheese burger. Also, Logo 1 for the header is<br>used for company logos.  By registering to the user macro 2 of #5, cut command + Logo 1 print command, the company<br>logo of logo1 will be printed. User macro 1 of #3 is used when it is necessary to position the Auto Logo in the center.<br>When doing so, register the left alignment command using the user macro 2 of #5 and return to its original setting.<br>Header Logo 1<br>********************<br> MACDONALDS<br>********************  *************** ********************<br>1.CHEESEBURGER  $2.00 2.COKE                      $1.00   MACDONALDS  MACDONALDS<br>*************** ********************<br>--------------------------------------  1.CHEESEBURGER  $2.00 1.CHEESBUGER       $2.00<br>TOTAL                       $3.00 2.COKE                      $1.00 2.COKE                    $1.00<br>--------------------------------------  Current<br>---------------------- TOTAL                       $3.00 System<br>TOTAL                     $3.00  Print Data<br>1. Starts Auto Logo with trigger<br>    of cutting command. Partial Cut<br>2. Executes user macro 1.<br>Current System Print Data Logo 2<br>     Header Cheeseburger<br>Partial Cut<br>3. Prints Auto Logo.<br>COKE Logo 3<br>‘o<br>4. Executes user macro 2.<br>     - Executes cut.<br>     - Executes Header logo  Header<br>       printing.<br>********************<br> MACDONALDS<br>Si an<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-111 
