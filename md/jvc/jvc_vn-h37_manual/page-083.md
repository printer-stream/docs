## **Setting Audio Multicast Address** 

## **Format  /api/param?network.destination(4).host=data** 

## **Example  /api/param?network.destination(4).host=225.0.1.3** 

## **Example of Response** 

## **network.destination(4).host&202 Accepted(network.destination(4).host=save)** 

**Interpretation** Change audio multicast address. Specify from 224.0.0.0 to 239.255.255.255. To validate the 

change, use "network.destination(4).host=save" API. After the save, start streaming by 

"network.destination(4).host=start" API. 

## **Allowed user** admin 

## **Getting Audio Multicast Port Number** 

**Format  /api/param?network.destination(4).port** 

## **Example of Response  network.destination(4).port=39152&200 OK** 

**Interpretation** Acquire audio multicast port number. 

**Allowed users** admin, operator 

## **Setting Audio Multicast Port Number** 

**Format  /api/param?network.destination(4).port=data** 

## **Example  /api/param?network.destination(4).port=39152** 

## **Example of Response** 

## **network.destination(4).port&202 Accepted(network.destination(4).host=save)** 

**Interpretation** Change audio multicast port number. Specify from 2 to 65534. To validate the change, use 

"network.destination(4).host=save" API. After the save, start streaming by "network.destination(4).host=start" API. 

## **Allowed user** admin 

## **22. JVC API for Access Restrictions** 

The APIs below are related to access restrictions. These are equivalent to the features on the Access Restrictions page of the WEB setting page. Refer to the instruction manual for details on the Access Restrictions page. 

## **Getting Deny/Allow Setting of Client Restrictions** 

## **Format  /api/param?network.access_control(stream_out).logic** 

## **Example of Response  network.access_control(stream_out).logic=deny&200 OK** 

**Interpretation** Acquire the deny/allow setting of client restrictions. Either deny or allow will be returned. These 

80 

Downloaded from www.Manualslib.com manuals search engine 
