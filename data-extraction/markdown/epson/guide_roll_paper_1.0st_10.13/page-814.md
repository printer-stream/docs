## C O N F I D E N T I A L

- ■ The setting values of this function affect the following operations and values.
- Even if the setting value for paper width ( sf ) is changed with this function, the ESC W and GS W setting values do not change. After changing ( sf ) of this function, set ESC W and GS W , or initialize the setting values of ESC W and GS W with ESC @ . However, if you use ESC @ , the setting values of the various commands are also initialized.
- ■ When settings other than "No reference" are specified for layout reference ( sm ≠ "0"), a paper layout error may occur with a vertical layout ( sa ). For details of the paper layout error, refer to the model information. The special margin (the setting value of &lt;Function 80&gt; of this command) is taken into account in detection of the print reference when the paper is changed or the first sheet is printed after turning on the power. Refer to &lt;Function 80&gt; of this command for details of the special margin.

| Setting value   | Affected operation or value                                   |
|-----------------|---------------------------------------------------------------|
| sa              | Paper layout error detection                                  |
| sb              | Label paper/black mark paper feed to the print start position |
| sc              | Label paper/black mark paper feed to the cutting starting     |
| sd              | Label paper/black mark paper feed to the peeling position     |
| se              | Skipping backing paper when printing die cut label paper      |
| sf              | Standard mode/page mode printable area                        |
