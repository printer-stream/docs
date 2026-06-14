**ESC * r A** [Name] Enter raster mode [Code] ASCII ESC * r A Hex. 1B 2A 72 41 Decimal 27 42 114 65 [Defined Area] - - - [Initial Value] - - - [Function] Enters raster mode. This command is ignored when in the raster mode. The following shows the details regard processing of this command. 

(1) Reception of this command. (2) When using parallel I/F, IEEE 1284 reverse mode is prohibited. (3) All data remaining in the reception buffer and image buffer is printed equivalent to the FF command. (4)  Initialize raster mode 

(5)  Enter raster mode 

When in the raster mode, the raster mode is initialized. The following shows the contents of the initialization. 

- Raster page length setting (ESC * r P n NUL) 

- Raster print quality setting (ESC * Q n NUL) 

- Raster left margin setting (ESC * r m l n NUL) 

- Raster right margin setting (ESC * r m r n NUL) 

- Raster EOT mode setting (ESC FF EOT) 

- Raster FF mode setting (ESC FF NUT) 

- Raster image buffer clear 

(*) Only raster data print color setting is not initialized when entering the raster mode. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-70 
