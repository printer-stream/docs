## **Setting MTU Value** 

**Format  /api/param?network.interface.mtu=data** 

## **Example  /api/param?network.interface.mtu=1500** 

## **Example of Response** 

## **network.interface.mtu&202 Accepted(network.interface.status=restart)** 

**Interpretation** Change the MTU value. The range of set value is between 1280 to 1500. To validate the change, use "network.interface.status=restart" API. 

**Allowed user** admin 

## **Getting Network Negotiation Setting** 

**Format  /api/param?network.interface.negotiation** 

## **Example of Response  network.interface.negotiation=auto&200 OK** 

**Interpretation** Acquire the network Negotiation setting. Either auto, 100full, 100half, 10full or 10half will be 

returned. 

**Allowed users** admin, operator, user 

## **Setting Network Negotiation** 

**Format  /api/param?network.interface.negotiation=data** 

**Example  /api/param?network.interface.negotiation=auto** 

## **Example of Response** 

## **network.interface.negotiation&202 Accepted(network.interface.status=restart)** 

**Interpretation** Change the network Negotiation setting. Specify auto, 100full, 100half, 10full or 10half. To 

validate the change, use "network.interface.status=restart" API. 

**Allowed user** admin 

## **20. JVC API for Protocol** 

The APIs below are related to protocol. These are equivalent to the features on the Protocol page of the WEB 

setting page. Refer to the instruction manual for details on the Protocol page. 

## **Getting Port Number of HTTP** 

**Format  /api/param?network.http.port** 

## **Example of Response  network.http.port=80&200 OK** 

**Interpretation** Acquire port number of HTTP server in the camera. 

**Allowed users** admin, operator 

75 

Downloaded from www.Manualslib.com manuals search engine 
