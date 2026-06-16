## C O N F I D E N T I A L

[Description]

Sets the paper layout (layout reference, vertical layout, horizontal layout).

- ■ Sets 'Layout reference (print reference/eject reference)' with sm .

| sm   | Layout reference                                                             | Relevant paper                      |
|------|------------------------------------------------------------------------------|-------------------------------------|
| '0'  | No reference (do not use layout)                                             | Receipt (no black mark)             |
| '1'  | Print reference: Label top edge Eject reference: Label bottom edge           | Die cut label paper (no black mark) |
| '2'  | Print reference: Black mark bottom edge Eject reference: Black mark top edge | Die cut label paper (black mark)    |
| '3'  | Print reference: Black mark top edge Eject reference: Black mark top edge    | Receipt (black mark)                |

## ■ Sets 'Vertical layout' with sa -se .

|    | Vertical layout                                                                                                                                                                 |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sa | ( sa = '0'): Does not specify the distance from the print reference to the next print reference ( sa ≠ '0'): Sets distance from the print reference to the next print reference |
| sb | The distance from the print reference to the print start position                                                                                                               |
| sc | The distance from the eject reference to the cutting position                                                                                                                   |
| sd | The distance from the eject reference to the label bottom edge position                                                                                                         |
| se | The distance from the eject reference to the bottom edge of the printing area                                                                                                   |

- The setting unit is 0.1 mm.
