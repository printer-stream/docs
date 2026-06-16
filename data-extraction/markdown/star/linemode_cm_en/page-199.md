<!-- image -->

## 5.7.  5-7)  Appendix 7 Explanation of Print Startup Control Starting Printing When Set to Page Units

When print startup control is set to page units, printing starts when the image buffer length is full or the following commands are run.

If the following commands are not received, start printing after a 1-second timeout.

For details on image buffer length and how to set print startup control, see the product specifications manual.

## Print starting trigger

- Cutter command

: &lt;ESC&gt; d n

- FF command

: &lt;FF&gt;

- BM detection command

: &lt;ESC&gt; d n, &lt;FF&gt;

- Print startup command

: &lt;ESC&gt;&lt;GS&gt; g 0 m n

- Raster mode

: &lt;ESC&gt; &lt;FF&gt; &lt;NUL&gt;

: &lt;ESC&gt; &lt;FF&gt; &lt;EOT&gt;

-----------------------------------------------------------------------------
