| Paris     | Same timezone as GMT+1.                                                      |
|-----------|------------------------------------------------------------------------------|
| CET       | Same timezone as GMT+1.                                                      |
| GMT+2     | Timezone that is 2 hours later than the Greenwich Mean Time.                 |
| EET       | Same timezone as GMT+2                                                       |
| GMT+3     | Timezone that is 3 hours later than the Greenwich Mean Time.                 |
| GMT+3:30  | Timezone that is 3 hours and 30 minutes later than the Greenwich Mean Time.  |
| GMT+4     | Timezone that is 4 hours later than the Greenwich Mean Time.                 |
| GMT+4:30  | Timezone that is 4 hours and 30 minutes later than the Greenwich Mean Time.  |
| GMT+5     | Timezone that is 5 hours later than the Greenwich Mean Time.                 |
| GMT+5:30  | Timezone that is 5 hours and 30 minutes later than the Greenwich Mean Time.  |
| Calcutta  | Same timezone as GMT+5:30                                                    |
| GMT+5:45  | Timezone that is 5 hours and 45 minutes later than the Greenwich Mean Time.  |
| GMT+6     | Timezone that is 6 hours later than the Greenwich Mean Time.                 |
| GMT+6:30  | Timezone that is 6 hours and 30 minutes later than the Greenwich Mean Time.  |
| GMT+7     | Timezone that is 7 hours later than the Greenwich Mean Time.                 |
| GMT+8     | Timezone that is 8 hours later than the Greenwich Mean Time.                 |
| GMT+8:45  | Timezone that is 8 hours and 45 minutes later than the Greenwich Mean Time.  |
| GMT+9     | Timezone that is 9 hours later than the Greenwich Mean Time.                 |
| GMT+9:30  | Timezone that is 9 hours and 30 minutes later than the Greenwich Mean Time.  |
| Japan     | Same timezone as GMT+9.                                                      |
| GMT+10    | Timezone that is 10 hours later than the Greenwich Mean Time.                |
| GMT+10:30 | Timezone that is 10 hours and 30 minutes later than the Greenwich Mean Time. |
| GMT+11    | Timezone that is 11 hours later than the Greenwich Mean Time.                |
| GMT+11:30 | Timezone that is 11 hours and 30 minutes later than the Greenwich Mean Time. |
| GMT+12    | Timezone that is 12 hours later than the Greenwich Mean Time.                |
| GMT+12:45 | Timezone that is 12 hours and 45 minutes later than the Greenwich Mean Time. |

Allowed users admin, operator, user

## Setting Timezone

Format  /api/param?system.timezone=data

Example  /api/param?system.timezone=Pacific

Example of Response  system.timezone&amp;202 Accepted(system.status=restart)

Interpretation Change the timezone of the camera. Refer to "Getting Timezone" on the character string to specify. To validate the change, use "system.status=restart" API.

Allowed user admin

## 24.  JVC API for Password

The APIs below are related to passwords. These are equivalent to the features on the Password page of the WEB setting page. Refer to the instruction manual for details on the Password page.

## Setting Password of admin

Format  /api/param?system.password.admin(num)=data2

Example

/api/param?system.password.admin(0)=someword

Example of Response system.password.admin(0)&amp;200 OK
