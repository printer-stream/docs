<!-- image -->

&lt;CRC calculation procedure, sample codes, C language&gt;

- #define CRC16 0xA001 unsigned int CalcCrc16( int size, unsigned char data[] ) { unsigned int result; int i,j; result = 0xFFFF; for( i=0 ; i&lt;size; i++) { result ^= data[i]; for(j = 0x0001; j &lt; 0x0100; j = j &lt;&lt; 1) { if( result &amp; 0x0001 ) { result &gt;&gt;= 1; result ^= CRC16; } else { result &gt;&gt;= 1; } } } result = (~result) &amp; 0xFFFF; return result; } Notes · If a logo is registered by the 'FS q' command, the logo data already existing is erased. · If a logo is registered by the 'GS (L' or 'GS 8 L' command, the logo that has been registered by the 'FS q' command is erased and the new one is registered. Reference GS ( L, GS 8 L
