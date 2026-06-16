<!-- image -->

## Kanji	Control	Commands	(For	Japanese,	Chinese	and	Taiwanese	language	specifications	only)

| Commands   | Name                                                       | Command Class   | Command Class   | Std Mode   | Page Mode   | GS P Effect   |
|------------|------------------------------------------------------------|-----------------|-----------------|------------|-------------|---------------|
| Commands   | Name                                                       | Exe.            | Set.            | Std Mode   | Page Mode   | GS P Effect   |
| FS !       | Batch specify Chinese character print mode                 |                 | ○               | ○          | ○           |               |
| FS &       | Specify Chinese character mode                             |                 | ○               | ○          | ○           |               |
| FS -       | Specify/cancel Chinese character underline                 |                 | ○               | ○          | ○           |               |
| FS .       | Cancel Chinese character mode                              |                 | ○               | ○          | ○           |               |
| FS 2       | Define external character                                  |                 | ○               | ○          | ○           |               |
| FS C       | Select Chinese character code type                         |                 | ○               | ○          | ○           |               |
| FS S       | Set Chinese character space amount                         |                 | ○               | ○          | ○           | ○             |
| FSW        | Specify/cancel double-tall, double wide Chinese characters |                 | ○               | ○          | ○           |               |

## ESC/POS	Black	Mark	Related	Commands

| Commands   | Name                                          | Command Class   | Command Class   | Std Mode   | Page Mode   | GS P Effect   |
|------------|-----------------------------------------------|-----------------|-----------------|------------|-------------|---------------|
| Commands   | Name                                          | Exe.            | Set.            | Std Mode   | Page Mode   | GS P Effect   |
| FF         | Print and recover to page mode + TOF and Cut  | ○               |                 | ○          | ○           |               |
| DLE ENQ    | Real-time request to printer                  | ○               |                 | ○          | ○           |               |
| GS FF      | Move to BM detection position                 | ○               |                 | ○          | ○           |               |
| GS ( F     | Adjust BM detection position                  |                 | ○               | ○          | ○           | ○             |
| GS ( M n=1 | Save black mark adjustment amount             | ○               |                 | ○          | ○           |               |
| GS ( M n=2 | Load black mark adjustment amount             | ○               |                 | ○          | ○           |               |
| GS ( M n=3 | Set auto-load of black mark adjustment amount |                 | ○               | ○          | ○           |               |
| GS <       | Mechanically initialize printer               | ○               |                 | ○          | ○           |               |
| GS V       | Cut paper                                     | ○               |                 | (L)        | ○           | ○             |
