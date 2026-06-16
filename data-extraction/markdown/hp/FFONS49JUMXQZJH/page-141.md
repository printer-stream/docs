Displayed current pen position and identification.

```
1000 1000 0 7470a
```

## Apple II Applesoft BASICExample:

```
10 PRu 3: IN# 3
```

```
20 zs= 'NT2' + CHR$ (25) 30 Y$= 'RUE' + CHR$ <25) 40 PRINT zs; 'PH1000,1000;UC;' 50 PRINT vs; 50 INPUT H,B,C ?0 PRINT vs; so INPUT us so PRINT zs; 'D1' 100 PRINT vs; 110 INPUT H$ 120 PRINT vs 130 INPUT D$ 140 PRa 0: IN# 0 150 PRINT H,s,c,Hs 150 END
```

Displayed current pen position and identification.

```
1000 1000 0 7470A
```

For an explanation of PR# 3, Z$ and PR# 0, refer to the Apple II example in the prior section. The string Y$ instructs the plotter at address 5 to talk. The Apple II sends an untalk command after it re­ ceives a carriage return character. The plotter with an HP-IB interface terminates all output with a carriage return followed by a line feed. Therefore, in order to clear the plotter's buffer for future output, another talk instruction and another input statement containing a dummy variable (D$in this program) must follow the input statement which reads parameters of the plotter output statement. The additional talk and input instructions will read the line feed character, thus clearing the plotter's buffer.
