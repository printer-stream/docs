## • TSP700II 

|Counter Type|Maintenance<br>Counter|Estimated Life|Count Up<br>Predetermined<br>Times|Counter<br>Maximum Value|EEPROM Writing Timing|
|---|---|---|---|---|---|
|Permanent<br>Counter|Head<br>Energizing<br>Count|800<br>Million<br>dot lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||LF<br>Motor<br>Traveling<br>Distance|100 km; 800<br>Million<br>dot<br>lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||Cutter Drive<br>Count|200,000 cuts|Every 10 cuts|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
|User Counter|Head<br>Energizing<br>Count|800<br>Million<br>dot lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||LF<br>Motor<br>Traveling<br>Distance|100 km; 800<br>Million<br>dot<br>lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||Cutter Drive<br>Count|200,000 cuts|Every 10 cuts|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|



- The head energizing count is sometimes counted even when there is not energizing data. (Such as when blank space data is included in the font data.) 

- The estimated life prescribes the number of count of the maintenance counter. It does not match the life specifications. 

- When the permanent counter exceeds the counter maximum value, thereafter the permanent counter and user counter both count up and then stop. 

- It is possible to clear the user counter, but it is not possible to clear the permanent counter. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-18 
