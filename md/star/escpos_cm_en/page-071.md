Rev.2.52 

## **ESC c 3 n** 

Name 

Select paper out sensor to enable at paper out signal output 

Code ASCII ESC c 3 n Hex. 1B 63 33 n Decimal 27 99 51 n 0 ≤ n ≤ 15 Defined Region Initial Value Spec. A:  n = 15 Spec. B:  n = 0 Function Selects paper out detector that outputs a paper out signal when paper has run out. 

## Spec. B: 

|Spec.|B:|||
|---|---|---|---|
|Bit|Function<br>|“0”|“1”|
|7|Undefned<br>|--|--|
|6|<br>Undefned<br>|--|--|
|5|<br>Undefned<br>|--|--|
|4|<br>Undefned<br>|--|--|
|3|<br>Undefned<br>|--|--|
|2|<br>Undefned|--|--|
|1|<br>Paper roll near end detector|Invalid|Valid|
|0|Paper roll near end detector|Invalid|Valid|



## Details 

- It is possible to select a multiple of detectors for signal output at the same time.  If any of the detectors detects the end of the paper, the paper end signal is output. 

- This command is only effective when using a parallel interface.  It is ignored when using a serial interface. 

- The detector switches when this command is executed so there may be some delay from reception of this command until switching to the paper out signal, depending on the status of the reception buffer. 

- If either bit 0 or bit 1 is set to 1, select the paper roll near end detector as the paper out detector for paper out signal output. 

- If either bit 2 or bit 3 is set to 1, select the paper roll end detector as the paper out detector for paper out signal output. 

- If all detectors are invalid, the paper out signal is constantly output as having paper. 

ESC/POS Command Specifications 

71 
