<!-- image -->

## 2. Separator character 1 (1 Byte)

Sends ':'

## 3. Data Type (1byte)

Indicate printer status data; sends 'B' (binary type).

4. Status Length (2 bytes)

2 byte value indicating printer status byte count.

## 5. Printer Status (Variable length)

Status sent by printer.

Status differs according to the cause.

See the command causes and automatic status for details on the content of statuses.

## 6. Separator character 2 (1 Byte)

Sends ';'

## 3) Status Transmission Specification List

| Status Cause                               | STAR ASB   | Length   | Status Data              | Status Data                     | Status Data           | Status Data   | Status Data   | Status Data    | Status Data           |
|--------------------------------------------|------------|----------|--------------------------|---------------------------------|-----------------------|---------------|---------------|----------------|-----------------------|
| Status Cause                               | STAR ASB   | Length   | Status Type              | Status Type                     | Separated Character 1 | Data Type     | Status Length | Printer Status | Separated Character 2 |
| Status Cause                               | STAR ASB   | Length   | First/Second Bytes Cause | Third/Fourth Bytes n Parameter  | Separated Character 1 | Data Type     | Status Length | Printer Status | Separated Character 2 |
| ASB Automatic Status                       | ASB        | 0x0000   | --                       | --                              | --                    | --            | --            | --             | --                    |
| ESCACK SOH Printer Status Request          | ASB        | 0x0000   | --                       | --                              | --                    | --            | --            | --             | --                    |
| ENQ Printer Status Request                 | ASB        | 0x0008   | '01'                     | Omitted                         | ':'                   | 'B'           | 0x0001        | Status         | ';'                   |
| EOT Printer Status Request                 | ASB        | 0x0008   | '02'                     | Omitted                         | ':'                   | 'B'           | 0x0001        | Status         | ';'                   |
| ESC SYN 3 n Presenter Counter Request      | ASB        | 0x0011   | '13'                     | '00' ≤ n ≤ '01' '30' ≤ n ≤ '31' | ':'                   | 'B'           | 0x0008        | Status         | ';'                   |
| ESC GS x I PDF417 Information Request      | ASB        | 0x000C   | '16'                     | Omitted                         | ':'                   | 'B'           | 0x0005        | Status         | ';'                   |
| ESC GS y I QR Code Information Request     | ASB        | 0x000D   | '19'                     | Omitted                         | ':'                   | 'B'           | 0x0006        | Status         | ';'                   |
| ESC GS ETS n1 n2 Print End Counter Request | ASB        | 0x000F   | '20'                     | Omitted                         | ':'                   | 'B'           | 0x0008        | Status         | ';'                   |

-----------------------------------------------------------------------------
