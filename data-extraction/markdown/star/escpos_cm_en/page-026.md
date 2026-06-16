<!-- image -->

## STAR	Original	Commands

| Commands   | Name                               | Command Class   | Command Class   | Std Mode   | Page Mode   | GS P Effect   |
|------------|------------------------------------|-----------------|-----------------|------------|-------------|---------------|
| Commands   | Name                               | Exe.            | Set.            | Std Mode   | Page Mode   | GS P Effect   |
| ESC GS =   | Write data to a blank code page    |                 | ○               | ○          | ○           |               |
| ESC GS t   | Select character code table        |                 | ○               | ○          | ○           |               |
| ESC GS +   | Macro registration                 | ○               | ○               | ○          | ○           |               |
| ESC GS #m  | Memory switch settings             | ○               | ○               | ○          | ○           |               |
| ESC RS F   | Select font                        |                 | ○               | ○          | ○           |               |
| ESC RS C   | Print mode selection               | ○               | ○               | ○          | ○           |               |
| ESC RS L   | Batch control logos                | ○               |                 | ○          |             |               |
| ESC GS ETX | Send print-end counter, initialize | ○               |                 | ○          | ○           |               |
| ESC GS ETX | Cancel print data feature          |                 | ○               | ○          |             |               |
| ESC GS ETX | Set data time out                  |                 | ○               | ○          |             |               |

## STAR	Original	Presenter	Control	Commands

| Commands       | Name                              | Command Class   | Command Class   | Std Mode   | Page Mode   | GS P Effect   |
|----------------|-----------------------------------|-----------------|-----------------|------------|-------------|---------------|
| Commands       | Name                              | Exe.            | Set.            | Std Mode   | Page Mode   | GS P Effect   |
| ESC SYN 0      | Execute presenter paper recovery  | ○               |                 | ○          | ○           |               |
| ESC SYN 1      | Set presenter paper recovery time |                 | ○               | ○          | ○           |               |
| ESC SYN 3      | Get presenter counter             |                 | ○               | ○          | ○           |               |
| ESC SYN 4      | Initialize presenter counter      |                 | ○               | ○          | ○           |               |
| ESC GS SUB DC1 | Specify snout opeation mode       |                 | ○               | ○          | ○           |               |
| ESC GS SUB DC2 | Set snout LED ON/OFF time         |                 | ○               | ○          | ○           |               |
| ESC GS SUB DC3 | Ouptut snout LED                  | ○               |                 | ○          | ○           |               |

## STAR	Original	Mark	Commands

| Commands   | Name                                              | Command Class   | Command Class   | Std Mode   | Page Mode   | GS P Effect   |
|------------|---------------------------------------------------|-----------------|-----------------|------------|-------------|---------------|
| Commands   | Name                                              | Exe.            | Set.            | Std Mode   | Page Mode   | GS P Effect   |
| ESC GS * 0 | Print mark                                        | ○               |                 | (D)        | Ignored     |               |
| ESC GS *1  | Set mark height and line feed                     |                 | ○               | ○          | ○           |               |
| ESC GS *2  | Set mark color and horizontal width               |                 | ○               | ○          | ○           |               |
| ESC GS *W  | Register mark format to non-volatile memory       | ○               | ○               | ○          | ○           |               |
| ESC GS *C  | Initialize mark format in the non-volatile memory | ○               | ○               | ○          | ○           |               |
