second are denoted in 2-digit decimal numbers. 

**Allowed users** admin, operator, user 

## **Setting Time** 

## **Format  /api/param?system.date=data** 

## **Example  /api/param?system.date=20050614171537** 

## **Example of Response  system.date&200 OK** 

**Interpretation** Change the time of the built-in clock in the camera. Specify in the order of year, month, day, hour, minute and second. Specify year in a 4-digit decimal number, and month, day, hour, minute and second in 2-digit decimal numbers. 

**Allowed user** admin 

## **Getting Timezone** 

## **Format  /api/param?system.timezone** 

## **Example of Response  system.timezone=Pacific&200 OK** 

**Interpretation** Acquire the timezone from the camera. Character strings in the following table will be returned. 

|Timezone CharacterString|Description|
|---|---|
|GMT-12|Timezone that is 12 hours earlier than the Greenwich Mean Time.|
|GMT-11|Timezone that is 11 hours earlier than the Greenwich Mean Time.|
|GMT-10|Timezone that is 10 hours earlier than the Greenwich Mean Time.|
|Hawaii|Same timezone as GMT-10|
|GMT-9:30|Timezone that is 9 hours and 30 minutes earlier than the Greenwich Mean Time.|
|GMT-9|Timezone that is 9 hours earlier than the Greenwich Mean Time.|
|Alaska|Same timezone as GMT-9|
|GMT-8|Timezone that is 8 hours earlier than the Greenwich Mean Time.|
|Pacific|(GMT-8:00)US/Pacific Time|
|GMT-7|Timezone that is 7 hours earlier than the Greenwich Mean Time.|
|Arizona|Same timezone as GMT-7|
|Mountain|Same timezone as GMT-7|
|GMT-6|Timezone that is 6 hour earlier than the Greenwich Mean Time.|
|Central|Same timezone as GMT-6|
|GMT-5|Timezone that is 5 hour earlier than the Greenwich Mean Time.|
|East-Indiana|Same timezone as GMT-5.|
|Eastern|Same timezone as GMT-5.|
|GMT-4|Timezone that is 4 hour earlier than the Greenwich Mean Time.|
|Atlantic|Same timezone as GMT-4.|
|GMT-3:30|Timezone that is 3 hours and 30 minutes earlier than the Greenwich Mean Time.|
|GMT-3|Timezone that is 3 hour earlier than the Greenwich Mean Time.|
|GMT-2|Timezone that is 2 hour earlier than the Greenwich Mean Time.|
|GMT-1|Timezone that is 1 hour earlier than the Greenwich Mean Time.|
|UTC|Greenwich Mean Time|
|London|Same timezone as UTC.|
|GMT+1|Timezone that is 1 hour later than the Greenwich Mean Time.|
|Berlin|Same timezone as GMT+1.|
|Rome|Same timezone as GMT+1.|
|Madrid|Same timezone as GMT+1.|



84 

Downloaded from www.Manualslib.com manuals search engine 
