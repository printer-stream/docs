<!-- image -->

## GS	(	k	pL	pH	cn	fn	[parameter]

Name

Set and print symbol

Code

ASCII GS ( k pL pH cn fn    [ p a r ame t e r ]

Hex. 1D 28 6B pL pH cn fn    [ p a r ame t e r ]

Decimal 29 40 107 pL pH cn fn    [ p a r ame t e r ]

Function

Runs processes related to symbol.

- pL and pH specify the parameter count (pL + pH x 256) in bytes after cn.

- Specifies the type of symbol with cn.

- Specifies the function with fn.

- See the function specifications for details on [parameter].

|   cn | Type of Symbol                                                                                          |
|------|---------------------------------------------------------------------------------------------------------|
|   48 | PDF417 (2-dimensional code)                                                                             |
|   49 | QR Code (2-dimensional code)                                                                            |
|   51 | 2D GS1 DataBar (GS1 DataBar Stacked, GS1 DataBar Stacked Omnidirectional, GS1 DataBar Expanded Stacked) |
|   52 | GS1 compound symbol                                                                                     |

|   cn |   fn | Function No.   | Function Name                                                               |
|------|------|----------------|-----------------------------------------------------------------------------|
|   48 |   65 | Function 065   | PDF417: Set number of positions                                             |
|   48 |   66 | Function 066   | PDF417: Set number of levels                                                |
|   48 |   67 | Function 067   | PDF417: Set module width                                                    |
|   48 |   68 | Function 068   | PDF417: Set level height                                                    |
|   48 |   69 | Function 069   | PDF417: Set error correction level                                          |
|   48 |   70 | Function 070   | PDF417: Select options                                                      |
|   48 |   80 | Function 080   | PDF417: Store data in symbol saving region                                  |
|   48 |   81 | Function 081   | PDF417: Print symbol data of symbol saving region                           |
|   48 |   82 | Function 082   | PDF417: Send size information of symbol data in symbol saving region        |
|   49 |   65 | Function 165   | QR Code: Set model                                                          |
|   49 |   67 | Function 167   | QR Code: Set module siz                                                     |
|   49 |   69 | Function 169   | QR Code: Select error correction level                                      |
|   49 |   80 | Function 180   | QR Code: Store data in symbol saving region                                 |
|   49 |   81 | Function 181   | QR Code: Print symbol data of symbol saving region                          |
|   49 |   82 | Function 182   | QR Code: Send size information of symbol data in symbol saving region       |
|   51 |   67 | Function 367   | 2D GS1 DataBar: Set module siz                                              |
|   51 |   71 | Function 371   | 2D GS1 DataBar: Set The maximum width of the 2D GS1DataBar Expanded Stacked |
|   51 |   80 | Function 380   | 2D GS1 DataBar: Store data in symbol saving region                          |
|   51 |   81 | Function 381   | 2D GS1 DataBar: Print symbol data of symbol saving region                   |
|   52 |   67 | Function 467   | Compound symbol: Set module siz                                             |
|   52 |   71 | Function 471   | Compound symbol:Set The maximum width of the 2D GS1DataBar Expanded Stacked |
|   52 |   72 | Function 472   | Compound symbol: Set HRI Font                                               |
|   52 |   80 | Function 480   | Compound symbol: Store data in symbol saving region                         |
|   52 |   81 | Function 481   | Compound symbol: Print symbol data of symbol saving region                  |
