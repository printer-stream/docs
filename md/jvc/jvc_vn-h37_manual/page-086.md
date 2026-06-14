## **Getting Access Interval to NTP Server** 

## **Format  /api/param?network.ntp.interval** 

## **Example of Response  network.ntp.interval=10&200 OK** 

**Interpretation** Acquire the interval for accessing the NTP server. Unit can be gotten by "network.ntp.unit" API. **Allowed users** admin, operator, user 

## **Setting Access Interval to NTP Server** 

## **Format  /api/param?network.ntp.interval=data** 

## **Example  /api/param?network.ntp.interval=60** 

## **Example of Response** 

## **network.ntp.interval&202 Accepted(network.ntp.status=restart)** 

**Interpretation** Change the interval for accessing the NTP server. Unit can be set by "network.ntp.unit" API. 

Specify 1-60 when the unit is min/hour, 1-31 when the unit is day. To validate the change, use 

"network.ntp.status=restart" API. 

**Allowed users** admin, operator 

## **Getting Access Interval Unit of NTP** 

## **Format  /api/param?network.ntp.unit** 

## **Example of Response  network.ntp.unit=hour&200 OK** 

**Interpretation** Acquire the unit of interval for accessing the NTP server. "min", "hour" or "day" is returned. 

**Allowed users** admin, operator, user 

## **Setting Access Interval Unit of SNTP** 

## **Format  /api/param?network.ntp.unit=data** 

## **Example  /api/param?network.ntp.unit=day** 

## **Example of Response** 

## **network.ntp.unit&202 Accepted(network.ntp.status=restart)** 

**Interpretation** Change the unit of interval for accessing the NTP server. Specify "min", "hour" or "day". To 

validate the change, use "network.ntp.status=restart" API. 

**Allowed users** admin, operator 

## **Getting Time** 

## **Format  /api/param?system.date** 

## **Example of Response  system.date=20050614171537&200 OK** 

**Interpretation** Acquire the time from the built-in clock of the camera. Time is arranged in the order of year, month, day, hour, minute and second. Year is denoted in a 4-digit decimal number, and month, day, hour, minute and 

83 

Downloaded from www.Manualslib.com manuals search engine 
