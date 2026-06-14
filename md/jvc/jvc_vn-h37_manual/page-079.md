## **Setting Port Number of HTTP** 

## **Format  /api/param?network.http.port=data** 

## **Example of Response  network.http.port&202 Accepted(network.http(configuration).status=restart)** 

**Interpretation** Change port number of HTTP server in the camera. Default value is 80. To validate the change, 

use "network.http(configuration).status=restart" or "network.http.status=restart" API. 

**Allowed users** admin, operator 

## **Getting Status of AMX Discovery Protocol** 

## **Format  /api/param?network.amx.beacon.status** 

## **Example of Response  network.amx.beacon.status=on&200 OK** 

**Interpretation** Acquire status of AMX Discovery Protocol in the camera. "on" or "off" is returned. 

**Allowed users** admin, operator 

## **Setting Status of AMX Discovery Protocol** 

## **Format  /api/param?network.amx.beacon.status=data** 

## **Example  /api/param?network.amx.beacon.status=on** 

## **Example of Response  network.amx.beacon.status&200 OK** 

**Interpretation** Change status of AMX Discovery Protocol in the camera. Specify "on" for interoperability with AMX products. 

**Allowed users** admin, operator 

## **Getting Status of PSIA Protocol** 

## **Format  /api/param?network.psia.status** 

## **Example of Response  network.psia.status=on&200 OK** 

**Interpretation** Acquire status of PSIA Protocol in the camera. "on" or "off" is returned. 

**Allowed users** admin, operator, user 

## **Setting Status of PSIA Protocol** 

## **Format  /api/param?network.psia.status=data** 

## **Example  /api/param?network.psia.status=on** 

## **Example of Response  network.psia.status&200 OK** 

**Interpretation** Change status of PSIA protocol in the camera. Specify "on" or “off”. When status of ONVIF protocol is set to “on”,  status of PSIA protocol will not be “on”. 

**Allowed users** admin, operator 

76 

Downloaded from www.Manualslib.com manuals search engine 
