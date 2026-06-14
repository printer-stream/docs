## **C O N F I D E N T I A L** 

## ■ **Automatic replacement of Font B (when a = 112)** 

|**(**nL**+**nH ×**256)**|**Automatic replacement of Font B**|
|---|---|
|**0, 48**|**Font A**|
|**1, 49**|**Font B (Same as no replacement)**|



- **Buzzer function: Enabling/disabling optional external buzzer (when a = 119)** 

|**Buzzer function:**|**Enabling/disabling optional external buzzer (**|
|---|---|
|**(**nL**+**nH ×**256)**|**Enabling/disabling optional external buzzer**|
|**0**|**Disabled**|
|**1**|**Enabled**|



   - **Set to Enabled when connecting the optional external buzzer.** 

   - **Set to Disabled when not connecting the optional external buzzer or connecting a drawer.** 

   - **The optional external buzzer is connected to the DKD connector; therefore, a drawer cannot be used at the same time. Both signals of drawer kick-out connector pins 2 and 5 are used.** 

- **Buzzer function: Buzzer frequency (Error) (when a = 120) (optional external buzzer)** 

|**Buzzer function:**|**Buzzer frequency (Error) (when a = 120)**|
|---|---|
|**(**nL**+**nH ×**256)**|**Buzzer frequency (Error)**|
|**0**|**No sound**|
|**1**|**1 time**|
|**65535**|**Continuous**|



   - **This function applies to when an error occurs (unrecoverable errors, recoverable errors, automatic recovery) or when a paper-end occurs.** 

   - **For the sound patterns, see** ESC ( A **<Function 97>, Sound buzzer in** TM-T20 **models (registered sound pattern specified).** 

- **Buzzer function: Sound pattern (Autocut) (when a = 121) (optional external buzzer) Buzzer function: Sound pattern (Pulse 1) (when a = 123) (optional external buzzer) Buzzer function: Sound pattern (Pulse 2) (when a = 125) (optional external buzzer)** 

   - **Pulse 1 and Pulse 2 are generated with** ESC p **: Generate pulse Pulse 1 when drawer kick-out connector pin 2 is selected. Pulse 2 when drawer kick-out connector pin 5 is selected.** 
