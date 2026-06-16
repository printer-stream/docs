<!-- image -->

## &lt;Printer status 7  Position for Presenter Paper (Ninth Byte)&gt;

|   Bit | Contents                 | Status            | Status   | By model                 | By model                 | By model                 | By model                 | By model   | By model   | By model   | By model   | By model   | By model   | By model   |
|-------|--------------------------|-------------------|----------|--------------------------|--------------------------|--------------------------|--------------------------|------------|------------|------------|------------|------------|------------|------------|
|       |                          | '0'               | '1'      | TSP800 Ver. 4.3 or later | TSP700 Ver. 3.2 or later | TSP600 Ver. 3.2 or later | TUP900 Ver. 1.2 or later | TSP1000    | TSP828L    | TSP700II   | TSP650     | TUP500     | TSP800II   | FVP10      |
|     7 | Fixed at '0'             |                   | -        | -                        | -                        | -                        | -                        | -          | -          | -          | -          | -          | -          | -          |
|     6 | Not Used (Fixed at '0')  |                   | -        | NO                       | NO                       | NO                       | OK                       | NO         | NO         | NO         | NO         | NO         | NO         | NO         |
|     5 | Not Used (Fixed at '0')  |                   | -        | NO                       | NO                       | NO                       | OK                       | NO         | NO         | NO         | NO         | NO         | NO         | NO         |
|     4 | Fixed at '0'             |                   | -        | -                        | -                        | -                        | -                        | -          | -          | -          | -          | -          | -          | -          |
|     3 | Presenter Paper Position | (See table below) |          | NO                       | NO                       | NO                       | OK                       | NO         | NO         | NO         | NO         | OK         | NO         | NO         |
|     2 | Presenter Paper Position | (See table below) |          | NO                       | NO                       | NO                       | OK                       | NO         | NO         | NO         | NO         | OK         | NO         | NO         |
|     1 | Presenter Paper Position | (See table below) |          | NO                       | NO                       | NO                       | OK                       | NO         | NO         | NO         | NO         | OK         | NO         | NO         |
|     0 | Fixed at '0'             |                   | -        | -                        | -                        | -                        | -                        | -          | -          | -          | -          | -          | -          | -          |

- This status is valid only on models provided with a presenter. Models not provided with a presenter should send this status fixed at '0.'
- This status is made valid and invalid using the memory switch only on models provided with a presenter.

When valid, the presenter paper position status is updated, but when invalid, the presenter paper position status is fixed at '0' and there is no change in status.

- Details of the Presenter Paper Position
- Presenter operation mode: Paper position status transition

|   bit 3 |   bit 2 |   bit 1 | Presenter Paper Position                                          |
|---------|---------|---------|-------------------------------------------------------------------|
|       0 |       0 |       0 | Paper position0 State where there is nopaper in presenter         |
|       0 |       0 |       1 | Paper position1 State where paper is supplied (loop state)        |
|       0 |       1 |       0 | Paper position2 (Reserved)                                        |
|       0 |       1 |       1 | Paper position3 State where paper is discharged(Can bepulled out) |
|       1 |       0 |       0 | Paper position4 (Reserved)                                        |
|       1 |       0 |       1 | Paper position5 (Reserved)                                        |
|       1 |       1 |       0 | Paper position6 State where paper is recovered                    |
|       1 |       1 |       1 | Paper position7 State where paper is pulled out.                  |

| Operating Mode                 | Paper    | Presenter paper position state transition                                                     |
|--------------------------------|----------|-----------------------------------------------------------------------------------------------|
| Loop Take-up Internal recovery | Recovery | Position 0toPosition 1to(Paper cut) to Position3to (Paper recovery) to Position 6to Position0 |
| Loop Take-up Internal recovery | Pull out | Position 0toPosition 1to(Paper cut) to Position3to (Paper pull out) to Position 7toPosition0  |
| Loop Take-up Front Discharge   | Recovery | Position 0toPosition 1to(Paper cut) to Position3to (Paper pull out) to Position 6toPosition0  |
| Loop Take-up Front Discharge   | Pull out | Position 0toPosition 1to(Paper cut) to Position3to (Paper pull out) to Position 7toPosition0  |
| NoLoop Internal recovery       | Recovery | Position 0toPosition 1to (Paper cut) to Position3to (Paper pull out) to Position 6toPosition0 |
| NoLoop Internal recovery       | Pull out | Position 0toPosition 1to(Paper cut) to Position3to (Paper pull out) to Position 7toPosition0  |
| NoLoop Front Discharge         | Recovery | Position 0toPosition 1to (Paper cut) to Position3to (Paper pull out) to Position 6toPosition0 |
| NoLoop Front Discharge         | Pull out | Position 0toPosition 1to(Paper cut) to Position3to (Paper pull out) to Position 7toPosition0  |
| Recovery Invalid               | Recovery | Position 0toPosition 1to(Paper cut) to Position6 to Position0                                 |
| Recovery Invalid               | Pull out | Position 0toPosition 1to(Paper cut) to Position6 to Position0                                 |

## 4. Note

Do not use ENQ, EOT, and ESC ACK SOH when automatic status is valid.  Invalidate the automatic status in advance using the DIPSW (memory switch) or the ESC RS a n command to query these.

-----------------------------------------------------------------------------
