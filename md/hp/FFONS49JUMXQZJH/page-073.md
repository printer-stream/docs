**==> picture [320 x 259] intentionally omitted <==**

**----- Start of picture text -----**<br>
Decimal | Set 0 Set | Set 2 Set 3 Sot 4<br>Value Standard 9825 French/German| Scandinavian |Spanish/Latin<br>ASCIT Set American<br>35 i f |4 £ | ¢<br>g2 \ f ¢ E |<br>93 ] J ] Q ]<br>Q5 [ees 4 co.<br>Q6 a. eee<br>126] * :<br>**----- End of picture text -----**<br>


## The Designate Standard Character Set Instruction, CS 

DESCRIPTION Bitewirs designate standard character set instruction, CS, provides the means of designating one of the five character sets (0 through 4) as the standard character set. 

| USES | The instruction can be used to change the standard character set to one with characters appropriate for your application. It is espe cially useful when labels are in a language other than English. 

SQUERS =CS character set number (terminator) 

eC §=The character set number can be 0 through 4. The set designated by the CS instruction is used for all labeling operations when the standard set is selected by the SS instruction or by the control character shift-in (decimal equivalent 15) in a label string. Character set 0 is automatically designated as the standard character set whenever the plotter is initialized or set to default values. 

A CS command executed while the standard set is selected will immediately change the character set used for labeling. CS commands 

LABELING 5-3 
