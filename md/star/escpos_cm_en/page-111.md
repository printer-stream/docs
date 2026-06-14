Rev.2.52 

## **<Function 069> GS ( k pL pH cn fn m n  (cn=48, fn=69)** 

## Name 

Set the PDF417 error correction level 

Code 

ASCII GS ( k pL pH cn fn m n Hex. 1D   28  6B  pL  pH cn fn m n Decimal   29   40  107  pL  pH cn fn m n 

Defined Region pL = 4, pH = 0 cn = 48, fn = 69 48 ≤ n ≤ 56 (When m = 48) 1 ≤ n ≤ 40 (When m = 49) Initial Value m = 49, n = 1 

Initial Value m = 49, n = 1 Function Sets the PDF417 error correction level. Details 

The setting of this function affects processes of Functions 081 and 082. 

- When m = 48, the error correction level is set by level. 

The error correction level set by ratio is discarded. 

The number of error correction code words is fixed regardless of the number of code words of the data region. 

|n|Function|Error Correction Code Word Count|
|---|---|---|
|48|Selects error correction level 0.|2|
|49|Selects error correction level 1.|4|
|50|Selects error correction level 2.|8|
|51|Selects error correction level 3.|16|
|52|Selects error correction level 4.|32|
|53|Selects error correction level 5.|64|
|54|Selects error correction level 6.|128|
|55|Selects error correction level 7.|256|
|56|Selects error correction level 8.|512|



- When m = 49, the error correction level is set by ratio. The ratio is set to n × 10%. 

The error correction level set by ratio is discarded. 

The error level is determined as shown in the following table on the basis of the result (A) of calculating [(data code words × n × 0.1) to the first decimal place rounded to the nearest integer]. 

The number of error correction code words varies proportionally to the number of code words of the data region. 

|<br>of the data region.|||
|---|---|---|
|Calculated Result(A)|Function|Error Correction Code Word Count|
|0 to 3|Selects error correction level 1.|4|
|4 to 10|Selects error correction level 2.|8|
|11 to 20|Selects error correction level 3.|16|
|21 to 45|Selects error correction level 4.|32|
|46 to 100|Selects error correction level 5.|64|
|101 to 200|Selects error correction level 6.|128|
|201 to 400|Selects error correction level 7.|256|
|More than 401|Selects error correction level 8.|512|



Reference GS ( k Function 081, 082, ESC @ 

ESC/POS Command Specifications 

111 
