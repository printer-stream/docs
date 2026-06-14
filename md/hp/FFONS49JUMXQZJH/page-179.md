output terminator = carriage return (decimal equivalent 13), 

intercharacter delay = 5, 

no immediate response string, 

block size = 80, 

enquiry character = DC2 (decimal equivalent 18), and 

acknowledgment string = 1 (decimal equivalent 49). 

The subroutine in line 100 contains the handshake. It causes the following chronological action. The enquiry character, DC2, is sent asking if the plotter has room for an 80-byte block. The plotter does not send an immediate response because that has been specified as null by itsuntilomissionafter it receivesin the ESCthe output.N command.trigger character,The plotter?. Theholdsquestionits responsemark — is sent by the computer when it interprets the BASIC statement INPUT to prompt for the input, Z. Z is the variable into which the acknowledgment string, 1, is read. If the acknowledgment string had been specified to contain nonnumeric characters, a string variable such as Z$ would have been used instead of Z. 

The plotter waits approximately five milliseconds, the intercharacter delay, before sending the 1 and between the 1 and the output terminator, carriage return. Note the carriage return parameter could have been omitted, but carriage return still would have been sent as the output terminator because that is the default value for output terminator. If ESC . I had been used instead of ESC . H, the output terminator would not have been sent after the acknowledgment string (but it would follow responses to HP-GL output commands). The carriage return character is a logical choice, because it is expected by the computer to delineate the end of data read by the INPUT statement. 

The computer is now free to send the string OUT$, which contains HPGL commands, to the plotter. Note the enquiry character must be sent each time data is sent to the plotter. 

Another handshake which would work using ESC. Tis 

40 PRINT CHR$(27);".180;7;33;13:" SO PRINT CHR$(27);".MS00:" 5; CHR$(27)5;".N5:" 

100 PRINT CHR$(7):INPUT Z$: PRINT OUT$: RETURN 

RS-232-C/CCITT V.24INTERFACING 10-37 
