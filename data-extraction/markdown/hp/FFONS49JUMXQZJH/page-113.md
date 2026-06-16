## Summary of Output Response Types

The following table shows the number and type of items in the re­ sponse to each HP-GL output command. The table includes output com­ mands explained in Chapters 2 and 6 as well as in this chapter. This table will be helpful when programming in languages such as FOR­ TRAN which require you to specify the type of and number of digits in a variable.

| Instruction                  | Number of Parameters Returned*   | Type and Range                                                                                                                                                                                                                     |
|------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OA OC** OD OE OF OI OO OP OS | 3 3 3 1 2 1 8 4 1                | integers, all < 5 digits decimals, all S 11 digits integers, all S 5 digits integer, 1 digit integers, 2 digits each 5-characterstring integers, 1 digit each integers, 1st and 3rd < 5 2nd and 4th S 4 digits integer, < 3 digits |
