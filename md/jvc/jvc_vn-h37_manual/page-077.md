## **Getting Unicast TTL Value** 

## **Format  /api/param?network.interface.ttl.unicast** 

## **Example of Response  network.interface.ttl.unicast=16&200 OK** 

**Interpretation** Acquire TTL of unicast. 1-255 is returned. 

**Allowed users** admin, operator, user 

## **Setting Unicast TTL** 

**Format  /api/param?network.interface.ttl.unicast=data** 

**Example  /api/param?network.interface.ttl.unicast=56** 

## **Example of Response** 

## **network.interface.ttl.unicast&202 Accepted(network.interface.status=restart)** 

**Interpretation** Change TTL of unicast. The range of set value is between 1 to 255. To validate the change, use 

"network.interface.status=restart" API. 

**Allowed user** admin 

## **Getting Multicast TTL Value** 

**Format  /api/param?network.interface.ttl.multicast** 

## **Example of Response  network.interface.ttl.multicast=16&200 OK** 

**Interpretation** Acquire TTL of multicast. 1-255 is returned. 

**Allowed users** admin, operator, user 

## **Setting Multicast TTL** 

**Format  /api/param?network.interface.ttl.multicast=data** 

**Example  /api/param?network.interface.ttl.multicast=56** 

## **Example of Response** 

## **network.interface.ttl.multicast&202 Accepted(network.interface.status=restart)** 

**Interpretation** Change TTL of multicast. The range of set value is between 1 to 255. To validate the change, use 

"network.interface.status=restart" API. 

**Allowed user** admin 

## **Getting MTU Value** 

**Format  /api/param?network.interface.mtu** 

**Example of Response  network.interface.mtu=1420&200 OK** 

**Interpretation** Acquire the MTU value. 

**Allowed users** admin, operator, user 

74 

Downloaded from www.Manualslib.com manuals search engine 
