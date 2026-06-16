## C O N F I D E N T I A L

```
TM-U230 : Function A m = 1, 49 Function B m = 66; 0 ≤ n ≤ 255
```

[Default]

None

[Printers not featuring this command] None

[Description]

Executes paper cutting specified by m , as follows:

| m   | m     | Function                                                                                                                                                        |
|-----|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <A> | 0, 48 | Executes a full cut (cuts the paper completely).                                                                                                                |
| <A> | 1, 49 | Executes a partial cut (one point left uncut).                                                                                                                  |
| <B> | 65    | Feeds paper to (cutting position + n × vertical motion unit) and executes a full cut (cuts the paper completely).                                               |
| <B> | 66    | Feeds paper to (cutting position + n × vertical motion unit) and executes a partial cut (one point left uncut).                                                 |
| <C> | 97    | Specifies a paper cutting range to (basic paper feed amount + [ n × vertical motion unit] and executes a full cut.                                              |
| <C> | 98    | Specifies a paper cutting range to (basic paper feed amount + [ n × vertical motion unit] and executes a partial cut (one point left uncut).                    |
| <D> | 103   | Feeds paper to (cutting position + n × vertical motion unit) and executes a full cut (cuts the paper completely), then feeds paper to the print start position. |
| <D> | 104   | Feeds paper to (cutting position + n × vertical motion unit) and executes a partial cut (one point left uncut), then feeds paper to the print start position.   |

- n of &lt;B&gt; and &lt;D&gt; specify paper feed amount executed immediately before a paper cut.
- n of &lt;C&gt; specifies a range of paper cut.

[Notes for &lt;A&gt;, &lt;B&gt;,&lt;C&gt;, and &lt;D&gt;]

- ■ When standard mode is selected, these commands are enabled only when processed at the beginning of the line.

```
Function C m = 98; 0 ≤ n ≤ 255
```
