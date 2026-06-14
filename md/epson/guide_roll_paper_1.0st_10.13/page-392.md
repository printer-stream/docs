## **C O N F I D E N T I A L** 

[Description: Applied to GS1 DataBar Omnidirectional (m = 75)] 

- Transmit the 13-digit product identification number, excluding the application identifier (AI) and check digit, from the host. 

- Adds the application identifier (AI) automatically. The AI is "01". 

- Adds the check digit (1 character) automatically. 

- Adds the guard pattern and finder pattern automatically. 

- Prints the 18 characters of ["(01)", (d1...d13), check digit] as HRI characters when HRI characters are designated to be added. 

- An example of bar code data is shown below. 

   - When printing a bar code with the product identification number [2001234567890]. GS k 75 13 "2001234567890" 

When HRI characters are designated to be added, the HRI characters are [(01)20012345678909]. 

- When the bar code height set with GS h is smaller than [33 times the module width], a bar code with a height (excluding the HRI characters) of [module width x 33] is printed, without reference to the GS h setting. 

[Description: Applied to GS1 DataBar Omnidirectional (m = 76)] 

- Transmit the 13-digit product identification number, excluding the application identifier (AI) and check digit, from the host. 

- Adds the application identifier (AI) automatically. The AI is "01". 

- Adds the check digit (1 character) automatically. 

- Adds the guard pattern and finder pattern automatically. 

- Prints the 18 characters of ["(01)", (d1...d13), check digit] as HRI characters when HRI characters are designated to be added. 

- An example of bar code data is shown below. 

When printing a bar code with the product identification number [0001234567890]. GS k 76 13 "0001234567890" 

When HRI characters are designated to be added, the HRI characters are [(01)00012345678909]. 
