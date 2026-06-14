Rev.2.52 

## **6-6-3 GS1 Databar Omnidirectional** 

Sends 13 digits of data except for AI (application identifiers) and check digits. AI (“01”) is added automatically. 

One check digit is added automatically. 

When HRI printing is enabled, 18 digits of [“(01)”, (d1...d13), check digit] are printed by the HRI. 

When the setting for the bar code height is smaller than [module width x33], the bar code height is printed at the [module width x33]. (Except for HRI heights) 

## **6-6-4 GS1 Databar Truncated** 

Sends 13 digits of data except for AI (application identifiers) and check digits. AI (“01”) is added automatically. 

One check digit is added automatically. 

When HRI printing is enabled, 18 digits of [“(01)”, (d1...d13), check digit] are printed by the HRI. 

When the setting for the bar code height is smaller than [module width x13], the bar code height is printed at the [module width x13]. (Except for HRI heights) 

## **6-6-5 GS1 Databar Limited** 

Sends 13 digits of data except for AI (application identifiers) and check digits. When HRI printing is enabled, 18 digits of [“(01)”, (d1...d13), check digit] are printed by the HRI. When the setting for the bar code height is smaller than [module width x10], the bar code height is printed at the [module width x10]. (Except for HRI heights) 

## **6-6-6 GS1 Databar Expanded** 

When sending special characters (FNC1) or “(“,”)”, the following double-byte data is sent. 

||Send data|Send data|Send data|
|---|---|---|---|
|Data|ASCII|Hex.|Decimal|
|FNC1|{+ 1|7B + 31|123 + 49|
|(|{+(|7B + 28|123 + 40|
|)|{+)|7B + 29|123 + 41|



The special character (“(“,”)”) is processed as shown in the following table. 

|pecial character(“(“,”)”)isprocessed as shown in the followingtable.|pecial character(“(“,”)”)isprocessed as shown in the followingtable.|pecial character(“(“,”)”)isprocessed as shown in the followingtable.|pecial character(“(“,”)”)isprocessed as shown in the followingtable.|
|---|---|---|---|
|||||
|Special characters||||
|character|Hex.|Decimal||
|(|28|40|“(“ is entered in the HRI character. AI can be highlighted by using in com-<br>bination with “)”. “)“ is not encoded.|
|)|29|41|The frst “)” after d1 is handled as an AI and the data divider.<br>“)” is entered in the HRI character. “)“ is not encoded.|



When HRI character printing is enabled, special characters are handled in the HRI as shown below. 

Control characters (FNC1) are not printed. 

Special characters (“(“,”)”) are printed. 

Bar code data [“{“ + (“(“, “)”)] is printed as (“(“, “)”). 

When the setting for the bar code height is smaller than [module width x34], the bar code height is printed at the [module width x34]. (Except for HRI heights) 

ESC/POS Command Specifications 

299 
