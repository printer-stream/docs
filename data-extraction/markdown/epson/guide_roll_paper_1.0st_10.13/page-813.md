## C O N F I D E N T I A L

- ■ When ( sm = '1') or ( sm = '2') is specified, note the following points when setting the printing area and cutting position.
- Specify that the printing area fits within with the label paper (do not specify any part of the printing area on the backing paper).
- Specify that the cutting position in on the backing paper (do not specify the cutting position on the label paper).
- ■ The setting values of ( sa -sf ) expressed as decimals are converted to text data and the high-order values are specified first. When specifying a negative number, add '-' at the beginning. Example:

When specifying 120, the data is the 3 bytes '120' [Hexadecimal = 31H, 32H, 30H / Decimal = 49, 50, 48]. When specifying -10, the data is the 3 bytes '-10'

[Hexadecimal = 2DH, 31H, 30H / Decimal = 45, 49, 48].

- ■ If the currently set 'Layout reference' and ( sm ) are the same value, ( sa -sf ) can be omitted. Omitted settings are not changed. However, when omitting parameters ';' cannot be omitted. Example:
- (When omitting sc and se ) FS ( L pL pH fn sm sa ; sb ; ; sd ; ; sf ;
- ■ Calculates the effective value used for actual print operation based on the setting values of this function, the setting value for paper width, and the limiting values for mechanical configuration (mechanical pitch, print head position, etc.) The setting value and effective value can be acquired with &lt;Function 34&gt; of this command.
- ■ When changing to paper with a different layout, reset the paper layout with this function.
- ■ The paper layout setting is enabled until the following operations are executed. It is not initialized by ESC @ . The setting value for this function is the saved data of GS ( M &lt;Function 1&gt;.
- Executing this function
- Turning off the power or resetting
