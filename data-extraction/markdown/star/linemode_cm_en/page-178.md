<!-- image -->

## 5.2.  Appendix 2: Status Specifications

## 5.2.1. ENQ Command Status

This status is the one the printer transmits using the ENQ command.

| Bit   | Contents               | Status   | Status   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   |
|-------|------------------------|----------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Bit   | Contents               | '0'      | '1'      | TSP800                | TSP700                | TSP600                | TUP900                | TSP1000               | TSP828L               | TSP700II              | TSP650                | TUP500                | TSP800                | FVP10                 |
| 7     | Conversion SW          | OPEN     | CLOSE    | OK                    | OK                    | OK                    | No                    | NO                    | NO                    | OK                    | OK                    | NO                    | OK                    | OK                    |
| 6     | Overrun Error          | No       | Yes      | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 5     | Reception Buffer Empty | Has Data | Empty    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 4     | Fixed at '0'           |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 3     | Paper end              | Paper    | No Paper | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 2     | Other Errors           | No       | Yes      | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 1     | Framing Error          | No       | Yes      | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 0     | Parity Error           | No       | Yes      | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |

Indicates non-recoverable errors and cover open errors.

## 5.2.2. EOT Command Status

This status is the one the printer transmits using the EOT command.

| Bit   | Contents                    | Status   | Status   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   |
|-------|-----------------------------|----------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Bit   | Contents                    | '0'      | '1'      | TSP800                | TSP700                | TSP600                | TUP900                | TSP1000               | TSP828L               | TSP700II              | TSP650                | TSP800                | FVP10                 |
| 7     | Compulsion SW               | OPEN     | CLOSE -  | OK                    | OK                    | OK                    | -                     | -                     | -                     | OK                    | OK                    | NO                    | NO                    |
| 6     | Presenter Paper Jam Error   | No       | Yes      | No                    | No                    | No                    | OK                    | No                    | NO                    | NO                    | NO                    | NO                    | NO                    |
| 5     | Paper Near-end (Outer Side) | Paper    | No Paper | No                    | No                    | No                    | No                    | No                    | NO                    | NO                    | NO                    | -                     | -                     |
| 4     | Fixed at '1'                |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 3     | Paper end                   | Paper    | No Paper | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 2     | Paper Near-end (Inner Side) | Paper    | No Paper | OK                    | OK                    | OK                    | OK                    | OK                    | NO                    | OK                    | OK                    | OK                    | OK                    |
| 1     | BINDING MEDIA Error         | No       | Yes      | No                    | No                    | No                    | OK                    | OK                    | OK                    | OK                    | NO                    | OK                    | OK                    |
| 0     | Fixed at '0'                |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |

On models that use a common PE and BM sensor, if a continuous error is detected beyond a determined amount, it indicates not a black mark error, but a paper out error.

-----------------------------------------------------------------------------
