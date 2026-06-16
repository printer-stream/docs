## C O N F I D E N T I A L

|   cn |   fn | Function No.   | Function name                                                                                          |
|------|------|----------------|--------------------------------------------------------------------------------------------------------|
|   50 |   65 | Function 265   | MaxiCode: Select the mode                                                                              |
|   50 |   80 | Function 280   | MaxiCode: Store the data in the symbol storage area                                                    |
|   50 |   81 | Function 281   | MaxiCode: Print the symbol data in the symbol storage area                                             |
|   50 |   82 | Function 282   | MaxiCode: Transmit the size information of the symbol data in the symbol storage area                  |
|   51 |   67 | Function 367   | 2-dimensional GS1 DataBar: Set the width of the module                                                 |
|   51 |   71 | Function 371   | 2-dimensional GS1 DataBar: GS1 DataBar Expanded Stacked maximum width setting                          |
|   51 |   80 | Function 380   | 2-dimensional GS1 DataBar: Store data in the symbol storage area                                       |
|   51 |   81 | Function 381   | 2-dimensional GS1 DataBar: Print the symbol data in the symbol storage area                            |
|   51 |   82 | Function 382   | 2-dimensional GS1 DataBar: Transmit the size information of the symbol data in the symbol storage area |
|   52 |   67 | Function 467   | Composite Symbology: Set the width of the module                                                       |
|   52 |   71 | Function 471   | Composite Symbology: GS1 DataBar Expanded Stacked maximum width setting                                |
|   52 |   72 | Function 472   | Composite Symbology: Select HRI character font                                                         |
|   52 |   80 | Function 480   | Composite Symbology: Store the data in the symbol storage area                                         |
|   52 |   81 | Function 481   | Composite Symbology: Print the symbol data in the symbol storage area                                  |
|   52 |   82 | Function 482   | Composite Symbology: Transmit the size information of the symbol data in the symbol storage area       |

- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( cn , fn , and [parameters] ). The [parameters] are described in each function.
- ■ The function is specified with the function code ( fn ). Details of the performance differ according to the function.

[Notes]

[Notes for processing of PDF417 symbol (when cn = 48)]

- ■ The symbol data specified by Function 080 d1...dk is stored in the printer and is printed by Function 081.
