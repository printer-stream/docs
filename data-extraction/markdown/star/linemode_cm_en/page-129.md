<!-- image -->

## 3.10. AUTO LOGO Function Command Details

This command functions to print logos, like the one below, by only changing the product name, when only product names can be changed in systems that are already in use.  Also, this function has two operating modes.

## 1) Standard Auto Logo Function

The Auto Logo function is preset and executes the following operations using the print cut command under the current system as a trigger.

1. Starts up the Auto Logo function using the current system cut command as a trigger
2. Prints if there is print data in the image buffer
3. Executes user macro 1
4. Prints the Auto Logo
5. Executes user macro 2

Logo 2 is printed by #4 Auto Logo printing according to the command character '/' that was preset in the current print data and embedding the logo number '2' to print. Specifically, if the product is registered with 'CHEESE BURGER/2' the logo 2 coupon ticket is automatically printed for the purchaser of a cheese burger. Also, Logo 1 for the header is used for company logos.  By registering to the user macro 2 of #5, cut command + Logo 1 print command, the company logo of logo1 will be printed. User macro 1 of #3 is used when it is necessary to position the Auto Logo in the center. When doing so, register the left alignment command using the user macro 2 of #5 and return to its original setting.

<!-- image -->

-----------------------------------------------------------------------------
