## **Example  /api/param?network.access_control(stream_out).host(1)=%00** 

**Allowed user** admin 

## **23. JVC API for Time** 

The APIs below are related to time. These are equivalent to the features on the Time page of the WEB setting 

page. Refer to the instruction manual for details on the Time page. 

## **Getting On/Off of SNTP Client** 

## **Format  /api/param?network.ntp.status** 

## **Example of Response  network.ntp.status=off&200 OK** 

**Interpretation** Acquire the on/off status of SNTP client. Either on or off will be returned. 

**Allowed users** admin, operator, user 

## **Setting On/Off of SNTP Client, or Validate Changes** 

## **Format  /api/param?network.ntp.status=data** 

## **Example  /api/param?network.ntp.status=on** 

## **Example of Response  network.ntp.status&200 OK** 

**Interpretation** Change the on/off status of SNTP client, or validate changes to settings. Specify "on", "off" or 

"restart". as on or off. IP address of NTP server and access interval are validated by "restart". 

**Allowed users** admin, operator 

## **Getting NTP Server Address** 

## **Format  /api/param?network.ntp.host** 

## **Example of Response  network.ntp.host=10.0.0.100&200 OK** 

**Interpretation** Acquire IP address of NTP server. Either the IP address or FQDN will be returned. 

**Allowed users** admin, operator, user 

## **Setting NTP Server Address** 

## **Format  /api/param?network.ntp.host=data** 

## **Example  /api/param?network.ntp.host=10.0.0.100** 

## **Example of Response  network.ntp.host&202 Accepted(network.ntp.status=restart)** 

**Interpretation** Change IP address of NTP server. Specify IP address or FQDN. To validate the change, use "network.ntp.status=restart " API. 

**Allowed users** admin, operator 

82 

Downloaded from www.Manualslib.com manuals search engine 
