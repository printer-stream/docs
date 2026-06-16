restrictions are applied to getting video stream and bi-directional Audio.

Allowed users admin, operator

## Setting Client Restriction to Deny/Allow

Format  /api/param?network.access\_control(stream\_out).logic=data

Example  /api/param?network.access\_control(stream\_out).logic=deny

Example of Response  network.access\_control(stream\_out).logic&amp;200 OK

Interpretation Change the deny/allow setting of client restrictions. Specify as deny or allow. These restrictions

are applied to getting video stream and bidirectional Audio.

Allowed user admin

## Getting IP Address Setting of Restricted Client

Format  /api/param?network.access\_control(stream\_out).host(Number)

Example When Getting the first IP address

/api/param?network.access\_control(stream\_out).host(1)

Example of Response  network.access\_control(stream\_out).host(1)=10.0.0.100&amp;200 OK

Interpretation Acquire the IP address setting of the restricted client. Setting is possible up to 10 items. Specify a value between 1 to 10 for the number. The following will be returned if subnet mask was specified.

Example of Response 2

network.access\_control(stream\_out).host(1)=10.0.0.0/24&amp;200 OK

The above example indicates that the range is between 10.0.0.0 to 10.0.0.255. There are also cases when FQDN instead of IP address is set.

Example of Response 3

network.access\_control(stream\_out).host(1)=somedivision.somecompany.com&amp;200 OK

Allowed users admin, operator

## Setting IP Address of Restricted Client

Format /api/param?network.access\_control(stream\_out).host(Number)=data

Example When setting the first IP address

/api/param?network.access\_control(stream\_out).host(1)=10.0.0.100

Example of Response  network.access\_control(stream\_out).host(1)&amp;200 OK

Interpretation Change the IP address setting of client restriction. Setting is possible up to 10 items. Specify a

value between 1 to 10 for the number. A range of IP address may be specified if the subnet mask is also specified.

For example, set as follows to specify a range between 10.0.0.0 to 10.0.0.255.

Example  /api/param?network.access\_control(stream\_out).host(1)=10.0.0.0/24

It is also possible to set using FQDN instead of IP address. Set as follows if the setting is to be left blank.
