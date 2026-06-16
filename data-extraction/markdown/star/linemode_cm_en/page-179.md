<!-- image -->

## 5.2.3. A utomatic

Status

Automatic status is a group of states that are automatically returned from the printer to the host when the printer's status has changed.  Automatic status is composed of 'Header - 1,' 'Header - 2' and 'plurality of bytes of the printer status and is continuously returned to the host.  The host always uses an identifying method to identify the data for every byte received.

(It is possible that Xon/Xoff codes are exceptionally mixed in the automatic status in the Xon/Xoff mode (when using a serial I/F), so it is necessary to consider that on the receiving side.)

The valid/invalid conditions of the automatic status abide by the DIPSW settings for the initial values.

It is possible to change the conditions using the ESC RS a n command after turning ON the power.

Also, it is possible to get the automatic status using the ESC ACK SOH command, regardless of the valid/invalid conditions.

## 1. Header - 1

Header - 1 is the 1 byte length information transmitted at the head of the automatic status.

The table below shows the composition of the Header - 1.  Header - 1 represents the entire status transmission byte count, including Header - 1, using bit 1 to bit 3 and bit 5.  The host gets the transmission byte information and always receives the status data for that amount transmission bytes.  For reference, the table below shows the relationship of actual transmission bytes and the Header - 1.  Because the bit 0 that indicates that this is the Header - 1 is normally 1 (the second byte and beyond is 0), to detect the Header - 1, it is acceptable to verify that bit 0 is 1 and bit 4 = 0 for this data.  Note that bit 6 is for future expansion and is ignored in host-side processes.

## &lt;Header - 1 (First Byte)&gt;

| Bit   | Contents                  | Status   | Status   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   |
|-------|---------------------------|----------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Bit   | Contents                  | '0'      | '1'      | TSP800                | TSP700                | TSP600                | TUP900                | TSP1000               | TSP828L               | TSP700II              | TSP650                | TUP500                | TSP800II              | FVP10                 |
| 7     | Fixed at '0'              |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 6     | Reserved (Fixed at '0')   |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 5     | Printer Status Byte Count |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 4     | Fixed at '0'              |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 3     | Printer Status Byte Count |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 2     | Printer Status Byte Count |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 1     | Printer Status Byte Count |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 0     | Fixed at '1'              | -        |          | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |

## Actual transmission byte count and header - 1 table

|   Transmission Byte Count n (7 ≤ n ≤ 15) | Header - 1         |
|------------------------------------------|--------------------|
|                                        7 | 00001111B (0F Hex) |
|                                        8 | 00100001B (21 Hex) |
|                                        9 | 00100011B (23 Hex) |
|                                       10 | 00100101B (25 Hex) |
|                                       11 | 00100111B (27 Hex) |
|                                       12 | 00101001B (29 Hex) |
|                                       13 | 00101011B (2B Hex) |
|                                       14 | 00101101B (2D Hex) |
|                                       15 | 00101111B (2F Hex) |

-----------------------------------------------------------------------------
