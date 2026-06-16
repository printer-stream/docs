<!-- image -->

Rev. 2.31

## ESC GS ) I pL pH fn

[Name]

Send printer information

[Code]

ASCII

ESC GS ) I pL pH fn

Hex

1B 1D 29 49 pL pH fn

Decimal

27 29 41 73 pL pH fn

[Defined Area]

pL = 1, pH = 0 fn = 49

[Function]

Send information of the printer that has been set by 'Command ESC GS ( S".

However, when the printer information is not registered by ESC GS (S, or printer information is cleared, the printer information that was set at the factory is sent.

[More information]    Send in the following format.

ESC GS) I    pL    pH    fn    [Tag name=Parameter, Tag name=Parameter, ... ]    LF    NUL

There is a tag name associated to the beginning of each parameter, and a parameter corresponding to each tag name is sent.

The tag name is up to the equal sign ("="), and after that is the parameter.

Each set of tags and parameters are separated with a delimiter "," and (2CH).

Printer information that is sent by this command is different depending on the model.

Information is transmitted from the top of the list shown below.

Only  the  information  supported  by  the  printer  of  the  transmission  source  (a  set  of  tags  and parameters) is transmitted.

&lt;LF&gt; &lt;NUL&gt; represents the terminal, the tag and its parameters after that are not transmitted.

Parameters are sent as a string.

If the information can not be obtained, transmits the following data.

<!-- formula-not-decoded -->

---Specification(1) ---

## transmission

↓

↓

↓

↓

↓

↓

|       | Parameter information              | Parameter information                                     |
|-------|------------------------------------|-----------------------------------------------------------|
| PrHwV | Printer main body HWversion        |                                                           |
| PrSrN | Product serial number              | up to 16 digits (Information less than 16 digits is NUL.) |
| BtDvN | Bluetooth device name              | Fixed 16 digits (Information less than 16 digits is NUL.) |
| BtAtC | Bluetooth auto connection          | Auto connection Invalid: BtAtC=00 Valid:BtAtC=01          |
| BtIpN | Bluetooth iOS port name            | Fixed 16 digits (Information less than 16 digits is NUL.) |
| BtDsC | Bluetooth Search Permitted Setting | Search Prohibited: BtDsC=00 Search Permitted: BtDsC=01    |

--------------------------------------------------------------------------------------
