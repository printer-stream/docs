Rev.2.52 

## **ESC GS / 6 n** 

Name Set partial cut before Auto Logo printing Code ASCII ESC GS / 6 n Hex. 1b 1d 2f 36 n Decimal 27 29 47 54 n 0 ≤ n ≤ 1 Defined Region Initial Value n = 0 Function Sets a partial cut before the Auto Logo printing. 

This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command. This command is ignored when Auto Logo is being executed. 

|Defned Region<br> <br>Initial Value<br> <br>Function<br> <br> <br>|0≤n≤1<br>n = 0<br>Sets a partial cut before the Auto Logo printing.<br>This command is registered to the non-volatile memory by the “<ESC> <GS> / W” c<br>This command is ignored when Auto Logo is being executed.|
|---|---|
|n|Setting|
|0|Does not execute apartial cut before the Auto Logoprinting.|
|1|Executes apartial cut before the Auto Logoprinting.|



When printing Logo2 and Logo3 as Auto Logo printing like the one in the drawing below, this command selects to execute a partial cut before printing Logo2 of the Auto Logo and Logo3. 

If a partial cut is executed using this function, it is possible to provide coupons, etc., that are printed using Auto Logo with a partial cut. 

Reference ESC GS / W, ESC GS / C, ESC GS / 1, ESC GS / 2, ESC GS / 3, ESC GS / 4, ESC GS / 5 

**==> picture [369 x 366] intentionally omitted <==**

**----- Start of picture text -----**<br>
     Header<br>***************<br>********************<br> MACDONALDS<br> MCDONALD’S<br>******************** ***************<br>1.CHEESBUGER       $2.00 1.CHEESEBURGER    $2.00<br>2.CO KE                    KE $1 .. 00<br>TOTAL                   $3.00 ----------------------------------- - -- -- -- --- -- -- --- -- -- -<br>TOTAL                    $3.00<br>1. AutoLogo triggered by cut<br>command  Partial Cut<br>2. User macro 1 is executed<br>Cheesebu     Heade r ger    Logo2 is printed<br>Partial Cut<br>3. AutoLogo is printed.<br>      COKE<br>Logo3 is printed<br>4. User macro 2 is executed.<br> Paper is cut.<br> Head logo is printed       Header<br>********************<br> MCDONALD’S<br>**----- End of picture text -----**<br>


ESC/POS Command Specifications 

215 
