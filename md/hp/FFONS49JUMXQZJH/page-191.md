- 4, The Remote Message. This message causes all devices currently addressed to listen to switch from local front-panel control to remote program control. 

5. The Local Message. This message clears the Remote Message from the listening device(s) and returns the device(s) to local frontpanel control. 

6. The Local Lockout Message. This message prevents a device operator from manually inhibiting remote program control. 

7. The Clear Lockout/Local Message. This message causes all devices on the bus to be removed from Local Lockout and revert to Local. This message also clears the Remote Message for all devices on the bus. 

8. The Require Service Message. A device can send this message at any time to signify that the device needs some type of interaction with the controller. This message is cleared by sending the device’s Status Byte Message if the device no longer requires service. 

9. The Status Byte Message. A byte that represents the status of a single device on the bus. Bit 6 indicates whether the device sent a Require Service Message, and the remaining bits indicate operational conditions defined by the device. This byte is sent from a talking device in response to a serial poll operation performed by a controller. 

10. The Status Bit Message. This byte represents the operational conditions of a group of devices on the bus. Each device responds on a particular bit of the byte thus identifying a device-dependent condition. This bit is typically sent by devices in response to a parallel poll operation. 

   - The Status Bit Message can also be used by a controller to specify the particular bit and logic level at which a device will respond when a parallel poll operation is performed. Thus, more than one device can respond on the same bit. 

11. The Pass Control Message. This transfers the bus management responsibilities from the active controller to another controller. 

12. The Abort Message. The system controller sends this message to unconditionally assume control of the bus from the active controller. This message terminates all bus communications (but does not implement a Clear Message). 

These messages represent the full implementation of all HP-IB system capabilities. Each device in a system may be designed to use only the messages that are applicable to its purpose in the system. It is 

AN HP-IB OVERVIEW A-3 
