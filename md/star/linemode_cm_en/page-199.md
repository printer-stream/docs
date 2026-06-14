## **5.7. 5-7) Appendix 7 Explanation of Print Startup Control Starting Printing When Set to Page Units** 

When print startup control is set to page units, printing starts when the image buffer length is full or the following commands are run. 

If the following commands are not received, start printing after a 1-second timeout. 

For details on image buffer length and how to set print startup control, see the product specifications manual. 

Print starting trigger • Cutter command : <ESC> d n • FF command : <FF> • BM detection command : <ESC> d n, <FF> • Print startup command : <ESC><GS> g 0 m n • Raster mode : <ESC> <FF> <NUL> : <ESC> <FF> <EOT> 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-27 
