<!-- image -->

## 3. COMMAND	FUNCTION	LIST

- ○: Valid
- (L): Effective only at the top of the line
- (S): Only setting effective
- (D): Effective only when there is no data in print buffer

## Standard	Commands

| Commands   | Name                                                         | Command Class   | Command Class   | Std Mode   | Page Mode   | GS P Effect   |
|------------|--------------------------------------------------------------|-----------------|-----------------|------------|-------------|---------------|
| Commands   | Name                                                         | Exe.            | Set             | Std Mode   | Page Mode   | GS P Effect   |
| HT         | Horizontal tab                                               | ○               |                 | ○          | ○           |               |
| LF         | Line feed                                                    | ○               |                 | ○          | ○           |               |
| FF         | Print and recover to page mode                               | ○               |                 | Ignored    | ○           |               |
| CR         | Print and carriage return                                    | ○               |                 | ○          | ○           |               |
| CAN        | Cancel print data in page mode                               | ○               |                 | Ignored    | ○           |               |
| DLE EOT    | Real-time status transmission                                | ○               |                 | ○          | ○           |               |
| DLE ENQ    | Real-time request to printer                                 | ○               |                 | ○          | ○           |               |
| DLE DC4    | Real-time output of specified pulse                          | ○               |                 | ○          | ○           |               |
| ESC FF     | Print data in page mode                                      | ○               |                 | Ignored    | ○           |               |
| ESC SP     | Set character right space amount                             |                 | ○               | ○          | ○           | ○             |
| ESC !      | Batch specify print mode                                     |                 | ○               | ○          | ○           |               |
| ESC $      | Specify absolute position                                    | ○               |                 | ○          | ○           | ○             |
| ESC%       | Specify/cancel download character set                        |                 | ○               | ○          | ○           |               |
| ESC &      | Define download characters                                   |                 | ○               | ○          | ○           |               |
| ESC *      | Specify bit image mode                                       | ○               |                 | ○          | ○           |               |
| ESC -      | Specify/cancels underline mode                               |                 | ○               | ○          | ○           |               |
| ESC 2      | Set default line spacing                                     |                 | ○               | ○          | ○           |               |
| ESC 3      | Set line feed amount                                         |                 | ○               | ○          | ○           | ○             |
| ESC =      | Select peripheral device                                     |                 | ○               | ○          | ○           |               |
| ESC ?      | Delete download characters                                   |                 | ○               | ○          | ○           |               |
| ESC@       | Initialize printer                                           | ○               | ○               | ○          | ○           |               |
| ESC D      | Set horizontal tab position                                  |                 | ○               | ○          | ○           |               |
| ESC E      | Specify/cancel emphasized printing                           |                 | ○               | ○          | ○           |               |
| ESC G      | Specify/cancel double printing                               |                 | ○               | ○          | ○           |               |
| ESC J      | Print and Paper Feed                                         | ○               |                 | ○          | ○           | ○             |
| ESC L      | Select page mode                                             | ○               |                 | (L)        | Ignored     |               |
| ESC M      | Select character font                                        |                 |                 | ○          | ○           |               |
| ESC R      | Select international characters                              |                 | ○               | ○          | ○           |               |
| ESC S      | Select standard mode                                         | ○               |                 | Ignored    | ○           |               |
| ESC T      | Select character print direction in page mode                |                 | ○               | (S)        | ○           |               |
| ESC V      | Specify/cancel char. 90 deg. clockwise rotation              |                 | ○               | ○          | (S)         |               |
| ESCW       | Set print region in page mode                                |                 | ○               | (S)        | ○           | ○             |
| ESC \      | Specify relative position                                    | ○               |                 | ○          | ○           | ○             |
| ESC a      | Position alignment                                           |                 | ○               | (L)        | (S)         |               |
| ESC c 3    | Select paper out sensor to enable at paper out signal output |                 | ○               | ○          | ○           |               |
| ESC c 4    | Select paper out sensor to enable at printing stop           |                 | ○               | ○          | ○           |               |
| ESC c 5    | Enable/disable panel switches                                |                 | ○               | ○          | ○           |               |
| ESC d      | Print and feed paper n lines                                 | ○               |                 | ○          | ○           |               |
| ESC p      | Specify pulse                                                | ○               |                 | ○          | ○           |               |
| ESC t      | Select character code table                                  |                 | ○               | ○          | ○           |               |
| ESC {      | Specify/cancel upside-down characters                        |                 | ○               | (L)        | (S)         |               |
| FS g 1     | Write data to user NV memory                                 |                 | ○               | ○          | Invalid     |               |
| FS g 2     | Read user NV memory data                                     | ○               |                 | ○          | ○           |               |
