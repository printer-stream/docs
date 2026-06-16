## Getting Status of ONVIF Protocol

Format  /api/param?network.onvif.status

Example of Response  network.onvif.status=on&amp;200 OK

Interpretation Acquire status of ONVIF Protocol in the camera. "on" or "off" is returned.

Allowed users admin, operator, user

## Setting Status of ONVIF Protocol

Format  /api/param?network.onvif.status=data

Example  /api/param?network.onvif.status=on

Example of Response  network.onvif.status&amp;200 OK

Interpretation Change status of ONVIF protocol in the camera. Specify "on" or 'off'. When status of PSIA protocol is set to 'on',  status of ONVIF protocol will not be 'on'.

Allowed users admin, operator

## 21.  JVC API for Multicast Streaming

The APIs below are related to manual streaming. These are equivalent to the features on the Streaming page of the WEB setting page. Refer to the instruction manual for details on the Streaming page.

## Getting Status of Multicast Streaming

Format  /api/param?network.destination(num).status

Example of Response  network.destination(1).status=off&amp;200 OK

Interpretation Acquire status of multicast streaming. 'num' is encoder channel from 1 to 3. Either on or off will be returned.

Allowed users admin, operator

## Setting Status of Multicast Streaming, or Save Changes

Format  /api/param?network.destination(num).status=data

Example  /api/param?network.destination(1).status=start

Example of Response  network.destination(1).status&amp;200 OK

Interpretation Start/stop multicast streaming of specified encode channel, or save changes to multicast streaming settings. 'num' is encoder channel from 1 to 3. Specify "start", "stop" or "save". Changes of multicast streaming settings become valid by "save".

Multicast stream is RTP compliant.

If power becomes off during multicast streaming, the streaming starts automatically after power on.

Allowed users admin, operator
