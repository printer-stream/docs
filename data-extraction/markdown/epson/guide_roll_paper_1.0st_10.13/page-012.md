Definitions

## DEFINITIONS

## Normal commands

Normal commands are all the commands except real-time commands. The normal commands are stored in the receive buffer temporarily and then processed sequentially.

## Real-time commands

Real-time commands are the commands that consist of a DLE extension (such as DLE EOT or DLE ENQ ). The realtime commands execute processing when received. After executing, they are stored in the receive buffer and then discarded as undefined codes when the normal commands are processed.

## Receive buffer

The receive buffer is used to store data from the host computer. All received data is stored in this buffer and processed in the order received. Buffer capacity depends on the printer model used.

## Obsolete commands

These are commands that will not be supported by future printer models. The command descriptions give a better command to use for the same function.

## Print buffer

The print buffer is used to store image data for printing.

## Print buffer-full

This state occurs when the print buffer becomes full.

## Print buffer-full printing

If new print data (such as characters or bit images) or horizontal tabs are processed in standard mode when the print buffer is full, the image data already stored in the print buffer is printed, and a line feed is executed. This is the same operation as LF . The data (print data or horizontal tab) that causes the print buffer-full is processed from the beginning of the next line.

If new print data (such as characters or bit images) or horizontal tabs are processed in page mode when the print buffer is full, the printer moves the print position to the beginning of the next line (the same operation as LF ) and processes the data (print data or horizontal tabs) that causes the print buffer-full.
