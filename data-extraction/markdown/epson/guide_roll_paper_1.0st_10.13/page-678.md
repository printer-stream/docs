## C O N F I D E N T I A L

- Memory can be used efficiently because the printer controls the data.
- The amount of definition area remaining can be confirmed.
- ■ NV user memory is the memory area used for storing character font data in non-volatile memory. The data stored is effective until it is redefined by this command.
- ■ In standard mode, this command is effective only when processed at the beginning of a line.
- ■ If this command is encountered while a macro is being defined, the printer cancels macro definition and starts processing this command. At that time, the macro becomes undefined.
- ■ All the previously stored data in the specified area is replaced with new data.
- ■ The NV user memory data can be read by FS g 2 .
- ■ Data is written to non-volatile memory by this function. Note the following when using these functions:
- Do not turn off the power or reset the printer from the interface when this command is being executed.
- The printer may be BUSY when storing data and will not receive any data. In this case, be sure not to transmit data from the host.
- Excessive use of this function may destroy the non-volatile memory. As a guideline, do not use any combination of the following commands more than 10 times per day for writing data to the nonvolatile memory: GS ( A (part of functions), GS ( C (part of functions), GS ( E (part of functions), GS ( L / GS 8 L (part of functions), GS ( M (part of functions), GS g 0 , FS g 1 , FS q .
- ■ Note the rules below for the operating NV memory (store data / cancel data):
- Even if the paper feed button is pressed, the printer does not feed paper.
- The printer does not process real-time commands.
- Even if 'ASB is enabled' is specified, the printer does not send ASB status.

[Model-dependent variations]

None

```
Program Example PRINT #1, CHR$(&H1C); Ó g1 Ó ;CHR$(0); PRINT #1, CHR$(0);CHR$(0);CHR$(0);CHR$(0);CHR$(14);CHR$(0); PRINT #1, Ò NVimage1=Stamp Ó ;
```

[Notes]
