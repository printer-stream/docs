<!-- image -->

## 3.  COMMAND DETAILS

## 3.1.  Exp lanation  of  Terms

## · Reception buffer

The buffer for storing data (reception data) received from the host, as it is called the reception buffer. Reception data is temporarily stored in the reception buffer, then processed sequentially.

## · Line buffer

The buffer for storing image data for printing is called the line buffer.

## · Line buffer full

The state in which the buffer has no more space available is called line buffer full.  When the buffer is full in standard mode, data in the line buffer is printed and a line feed is performed when new print data is processed.  This is the same as a Line Feed.  When the line buffer is full in the page mode, the printer move the print position to the head of the next line then starts with the new print data.

## · Top of line

The top of line is a state that satisfies the following conditions.

- There is currently no print data in the line buffer.
- The position is not specified with the horizontal direction position command.
- Printable region

This is the maximum printable area with the printer's specifications.

· Print region This is the printing area specified by a command. (Print region ≤ printable region)

## · ANK character base line

<!-- image -->

- ASB Function

Sends the automatic status to the host each time the printer's status changes.

## · NSB Function

When the printer uses a parallel I/F or USB I/F, sends the automatic status each time the reverse transfer mode is entered. When the printer uses Ethernet I/F or wireless I/F, sends the automatic status when the printer is connected to the print port (TCP#9100). The ASB and NSB status formats are the same.

-----------------------------------------------------------------------------
