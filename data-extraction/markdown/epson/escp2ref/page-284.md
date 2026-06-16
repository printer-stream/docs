<!-- image -->

Several types of scoring are available on 24/48-pin printers, as shown below:

| ABCDEFGHi jklmno   | ABCDEFGhi jklmno   |
|--------------------|--------------------|
| ABEBEFGH+Fkimno    | ABEDEFGh+3ktmnoe   |
| ABCDEFGHi jkImno   | ABCDEFGhi jkImno   |
| TR AR RRADTT       |                    |

## Note:

You can use the ESC- command to select single, continuous underlining on 9-pin printers. This is the only type of scoring available on 9-pin printers.

The command for selecting scoring is ESC ( -, and its format and combinations are as follows:

ESC ( - 3 0 1 n 1 n2

n1  = 1 Underline 2 Strikethrough 3 Overscore

n2  = 0 Turn off scoring 1 Single continuous line 2 Double continuous line 5 Single broken line 6 Double broken line

## Note:

- Each type of scoring is independent of other types; any combination of scoring can be set simultaneously.
- The score is printed in the currently selected print quality and is affected by the bold and double-strike commands.
- You cannot score graphics characters.
