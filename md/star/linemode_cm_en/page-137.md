## **ESC GS / 6  n** 

[Name] Set partial cut before Auto Logo printing [Code] ASCII ESC GS / 6 n Hex. 1b 1d 2f 36 n Decimal 27 29 47 54 n 

**==> picture [471 x 528] intentionally omitted <==**

**----- Start of picture text -----**<br>
[Defined Area]  0 ≤ n ≤ 1<br>[Initial Value]  n = 0<br>[Function]  Sets a partial cut before the Auto Logo printing.<br>This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.<br>This command is ignored when Auto Logo is being executed.<br>n  Setting<br>0  Does not execute a partial cut before the Auto Logo printing.<br>1  Executes a partial cut before the Auto Logo printing.<br>a<br>When printing Logo2 and Logo3 as Auto Logo printing like the one in the drawing below, this<br>command selects to execute a partial cut before printing Logo2 of the Auto Logo and Logo3.<br>If a partial cut is executed using this function, it is possible to provide coupons, etc., that are printed<br>using Auto Logo with a partial cut.<br>Header<br>oT<br>***************<br>********************<br> MACDONALDS<br> MACDONALDS<br>******************** ***************<br>1.CHEESEBURGER  $2.00 1.CHEESBUGER       $2.00<br>2.COKE                      $1.00 2.COKE                    $1.00<br>--------------------------------------<br>TOTAL                       $3.00----------------------<br>TOTAL                   $3.00<br>1. Starts Auto Logo with trigger<br>    of cutting command. Partial Cut<br>2. Executes user macro 1.<br>     Header Cheeseburger  Prints Logo 2<br>Partial Cut<br>3. Prints Auto Logo<br>COKE Prints Logo 3<br>|<br>4. Executes user macro 2.- Executes cut. __<br>- Executes Header logo  Header<br>       printing.<br>********************<br> MACDONALDS<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-119 
