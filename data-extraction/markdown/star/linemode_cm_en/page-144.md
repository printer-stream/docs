<!-- image -->

## 3.13. Two-Dimensional Bar Code QR Code Command Details

* Note that QR code is a registered trademark of DENSO WEB.

This command is for printing 2-dimensional bar code QR codes.  There are four functions of the commands relating to the 2-dimensional bar code QR codes, shown below.

- (1) Set bar code type

(&lt;ESC&gt; &lt;GS&gt; 'y' 'S')

- (2) Set bar code data

(&lt;ESC&gt; &lt;GS&gt; 'y' 'D')

- (3) Set page mode

(Reserved)

- (4) Print Bar code

(&lt;ESC&gt; &lt;GS&gt; 'y' 'P')

- (5) Set bar code type

(&lt;ESC&gt; &lt;GS&gt; 'y' 'I')

The details of each function are described below.

## (1) Set bar code type

These commands set the bar code type.  Because all initial values are set, use these only to make changes.  (See the details for each setting below.)

<!-- image -->

## &lt;ESC&gt; &lt;GS&gt; 'y' 'S' '0' Sets the model

Currently supported models are model 1 and model 2.  Model 2 has a configuration including an alignment bar to improve its support of weight to handle skewing when codes are large.

## &lt;ESC&gt; &lt;GS&gt; 'y' 'S' '1'  Sets the error correction level

QR codes can be read even if a part of the data is corrupted, by using error correction.  Raising this level increases the size of the bar code because there is an increase in preparatory information.

## &lt;ESC&gt; &lt;GS&gt; 'y' 'S' '2'  Specifies the size of the cell (One four squared region configuring the QR code)

The QR code is formed into a square of an equivalent size in the vertical and horizontal directions, but the size of the bar code image that is generated depends on the cell size setting.  See Appendix 7 for details on the actual printed size of the QR code.

These settings are individual settings.  Therefore, even though there may not be any particular problem in each of them, there is the potential for an error to be generated.  (See the descriptions below.)  In such cases, the bar code will not be generated  and  the  (4)  Print  command  (&lt;ESC&gt;  &lt;GS&gt;  'y'  'P')  is  ignored.    With  the  (5)  Get  bar  code  expansion information command, an error code is returned.

- Error is generated when generating a bar code by the combination of each setting command.
- Print data exceeds the currently set print region

Therefore, it is recommended to use (5) Get bar code expansion information command (&lt;ESC&gt; &lt;GS&gt; 'y' 'I') as a means for checking for these errors prior to printing.

-----------------------------------------------------------------------------
