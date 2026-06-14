Rev.2.52 

When s=3, s=4 (Document start command + document end command) , operates as though in data cancel mode. 

If there is an error after receiveing the document start command, reception data is received and discarded until the document end command is received when the printer is recovered from the error. If the document end command cannot be recognized, all reception data is destroyed. Timeouts are 10 seconds. Automatically cancels the data intake mode. 

## Restrictions 

- 1) Sleep mode decrease 

- 2) Invalid when in Page mode 

- 3) Disabled in Page mode. 

When s = 3, initialize the following settings using the initializing process. 

- Set slash zero 

- Set specify/cancel external character (external register character data is retained) 

- Page length 

- Current position (move to top of page, top of line) 

- Horizontal tab/Vertical tab 

- Set upside-down, position alignment 

- Left/right margins 

## <T: TOP Command/E: END Command> 

**==> picture [281 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
T T<br>Doc 1 Doc 1<br>PE PE<br>Receive  Receive<br>and discard E and discard<br>T<br>Doc 2 Doc 2<br>E<br>T<br>Doc 3 Doc 3<br>E E<br>**----- End of picture text -----**<br>


ESC/POS Command Specifications 

191 
