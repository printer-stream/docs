2. Decimal Format — a number between —128.0000 and 127.9999 with an optional decimal point and decimal fraction with up to four significant digits. If no sign is specified, the parameter is assumed to be positive. 

3. Label Fields — any combination of text, numeric expressions, or string variables. Refer to The Label Instruction, LB, Chapter 5, for a complete description. 

Some instructions such as PA, PR, PU, and PD may have multiple parameters. Separators are required between these parameters. These optional parameters are shown in parentheses in the syntax descriptions. 

The syntax shown under the description of each HP-GL instruction uses the following notations: 

MNemonic For readability, the mnemonic is shown uppercase and separated from the parameters and/or terminator. 

necessary parameter All typeset items are required parameters. ( ) All items in parentheses are optional. C....C Any number of labeling characters. (,..) Any number of XY coordinate pairs. terminator ; or any nonnumeric or nonalphabetic character such as $ or #, or the next mnemonic. LF is also valid for HP-IB and HP-IL plotters. 

(terminator) Terminator for an instruction which will execute after the last necessary parameter is received. The following table shows the 7470’s HP-GL instruction set. 

## Plotter Instruction Set 

|AA|X,Y, arc angle (, chord angle) | Arc absolute*|X,Y, arc angle (, chord angle) | Arc absolute*|
|---|---|---|
|AR|X,Y, arc angle (, chord angle) | Arc relative*||
|CA|n|Designate alternate set n|
|CI|radius (, chord angle)|Circle*|
|CP_|spaces, lines|Character plot|
|CS|m|Designate standard setm|
|DC||Digitize clear|
|DF||Setdefaultvalues|



1-8 GETTING STARTED 
