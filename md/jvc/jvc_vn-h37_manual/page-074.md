**Interpretation** Acquire the current default gateway. Specify ipv4 or ipv6. 

**Allowed users** admin, operator, user 

## **Setting Default Gateway** 

## **Format  /api/param?network.gateway(ipv4)=data** 

## **Example  /api/param?network.gateway(ipv4)=192.168.0.254** 

## **Example of Response  network.gateway&200 OK** 

**Interpretation** Change the default gateway. To set static default gateway, disable DHCP. Default gateway can 

not be changed when DHCP is enabled. Specify IP address in same segment with the camera. Specify 0.0.0.0 to delete default gateway setting. Default gateway of IPv6 can not be set. 

**Allowed user** admin 

## **Getting Host Name** 

**Format  /api/param?network.hostname** 

## **Example of Response  network.hostname=localhost&200 OK** 

**Interpretation** Acquire the current host name. 

**Allowed users** admin, operator, user 

## **Setting Host Name** 

**Format  /api/param?network.hostname=data** 

**Example  /api/param?network.hostname=somename** 

## **Example of Response  network.hostname&200 OK** 

**Interpretation** Change the host name. Characters that may be used for the host name are alphanumerics, 

hyphens (-) and period. Maximum size is 63 bytes. 

Specify as %00 when the host name setting is to be left blank. 

## **Example when leaving field blank   /api/param?network.hostname=%00** 

**Allowed user** admin 

## **Getting DNS Server On/Off Status** 

**Format  /api/param?network.dns.status** 

## **Example of Response  network.dns.status=off&200 OK** 

**Interpretation** Acquire the on/off status of the DNS server. Either on or off will be returned. 

**Allowed users** admin, operator, user 

## **Setting DNS Server Status to On/Off, or Validate Changes** 

**Format  /api/param?network.dns.status=data** 

71 

Downloaded from www.Manualslib.com manuals search engine 
