## **Example  /api/param?network.dns.status=on** 

## **Example of Response  network.dns.status&200 OK** 

**Interpretation** Change status of DNS server setting, or validate changes to DNS server settings. Specify "on", 

"off" or "restart". Changes of DNS server settings become valid by "restart". 

**Allowed users** admin, operator 

## **Getting DNS Server IP Address** 

**Format  /api/param?network.dns.ip** 

**Example of Response  network.dns.ip=10.0.0.150&200 OK** 

**Interpretation** Acquire IP address of DNS server. 

**Allowed users** admin, operator, user 

## **Setting DNS Server IP Address** 

**Format  /api/param?network.dns.ip=data** 

**Example  /api/param?network.dns.ip=10.0.0.150** 

**Example of Response** 

## **network.dns.ip&202 Accepted(network.dns.status=restart)** 

**Interpretation** Change IP address of DNS server. To validate the change, use "network.dns.status=restart" API. **Allowed users** admin, operator 

## **Getting IPv6 status** 

**Format  /api/param?network.interface.ipv6.status** 

## **Example of Response  network.interface.ipv6.status=off&200 OK** 

**Interpretation** Acquire IPv6 status. "on" or "off" is returned. 

**Allowed users** admin, operator, user 

## **Setting IPv6 status** 

**Format  /api/param?network.interface.ipv6.status=data** 

**Example  /api/param?network.interface.ipv6.status=on** 

## **Example of Response** 

## **network.interface.ipv6.status&202 Accepted(network.dns.status=restart)** 

**Interpretation** Change IPv6 status. To validate the change, use "network.interface.status=restart" API that 

reboots the camera in about 1 minute. 

**Allowed users** admin, operator 

## **Getting Link Local Address of IPv6** 

72 

Downloaded from www.Manualslib.com manuals search engine 
