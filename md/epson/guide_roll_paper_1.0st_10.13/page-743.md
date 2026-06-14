## **C O N F I D E N T I A L** 

- **Print density is based on the setting (print density) when** _**a**_ **= 5.** 

|**(**nL**+**nH ×**256)**|**Print density**|**Print density**|
|---|---|---|
|**65530**|**Print density level 1**|**Light**|
|**65531**|**Print density level 2**|**|**|
|**65532**|**Print density level 3**|**|**|
|**65533**|**Print density level 4**|**|**|
|**65534**|**Print density level 5**|**|**|
|**65535**|**Print density level 6**|**|**|
|**0**|**Print density level 7**|**Standard**|
|**1**|**Print density level 8**|**|**|
|**2**|**Print density level 9**|**|**|
|**3**|**Print density level 10**|**|**|
|**4**|**Print density level 11**|**|**|
|**5**|**Print density level 12**|**|**|
|**6**|**Print density level 13**|**Dark**|



- **Buzzer function: Enabling/disabling optional external buzzer (when** _**a**_ **= 119)** 

|**Buzzer function:**|**Enabling/disabling optional external buzzer (**|
|---|---|
|**(**nL**+**nH ×**256)**|**Enabling/disabling optional external buzzer**|
|**0**|**Disabled**|
|**1**|**Enabled**|



   - **Set to Enabled when connecting the optional external buzzer.** 

   - **Set to Disabled when not connecting the optional external buzzer or connecting a drawer.** 

   - **The optional external buzzer is connected to the DKD connector; therefore, a drawer cannot be used at the same time. Both signals of drawer kick-out connector pins 2 and 5 are used.** 

- **Buzzer function: Buzzer frequency (Error) (when** _**a**_ **= 120) (optional external buzzer)** 

|**Buzzer function:**|**Buzzer frequency (Error) (when****_a_ = 120)**|
|---|---|
|**(**nL**+**nH ×**256)**|**Buzzer frequency (Error)**|
|**0**|**No sound**|
|**1**|**1 time**|
|**65535**|**Continuous**|



- **This function applies to when an error occurs (unrecoverable errors, recoverable errors, automatic recovery) or when a paper-end occurs.** 
