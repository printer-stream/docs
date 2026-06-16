## C O N F I D E N T I A L

- ■ Adds the guard bar automatically for encoding.

[Note for GS1 DataBar Omnidirectional, GS1 DataBar Truncated and GS1 DataBar Limited]

- ■ The data shown below is added automatically in encoding.
- Application identifier (AI): The AI is "01".
- Check digit (1 character)
- Guard pattern and separator pattern
- ■ Prints the 18 characters of ["(01)", (d1...d13), check digit] as HRI characters when HRI characters are designated to be added.

[Note for GS1 DataBar Stacked and GS1 DataBar Stacked Omnidirectional]

- ■ The data shown below is added automatically in encoding.
- Application identifier (AI): The AI is "01".
- Check digit (1 character)
- Guard pattern and separator pattern
- ■ Even when HRI characters are designated to be added, HRI characters are not added to this symbol.

[Note for GS1 DataBar Expanded]

- ■ The data shown below is added automatically in encoding.
- Guard pattern and finder pattern
- ■ The special characters ("(',')') are processed as shown in the table below.
- ■ Adds the guard pattern and finder pattern automatically.

| Special characters   | Special characters   | Special characters   | Special characters                                                           |
|----------------------|----------------------|----------------------|------------------------------------------------------------------------------|
| Character            | Hex                  | Decimal              | Processing                                                                   |
| (                    | 28                   | 40                   | "(" is inserted for the HRI character. "(" does not constitute encoded data. |
| )                    | 29                   | 41                   | ")" is inserted for the HRI character. ")" does not constitute encoded data. |
