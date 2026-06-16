## C O N F I D E N T I A L

Overview of data processing

## OVERVIEW OF DATA PROCESSING

## Character Data and Normal Commands

The printer stores data sent from the host computer in the receive buffer temporarily, and then the printer interprets the data and classifies them into commands or character data sequentially. If the data from the receive buffer is a normal command, the printer processes the command corresponding to its function; for example, if the data interpreted is ESC 3 , the printer changes a setting value for the line spacing, and if it is LF , the printer prints the data in the print buffer and feeds the paper one line.

If the data from the receive buffer is character data, the printer reads the appropriate font data from the resident character generator and writes image data to the print buffer.

## Real-time Commands

The printer stores data sent from the host computer in the receive buffer, interprets the data, and processes the commands corresponding to their function one line at a time. The real-time commands are the commands that consist of a DLE extension, such as DLE EOT or DLE ENQ . They are processed immediately. The real-time commands are ignored as undefined codes in the main processing.
