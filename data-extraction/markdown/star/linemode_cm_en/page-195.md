<!-- image -->

## 5.5.  Appendix 8 TSP828L Cut Command Specifications

## &lt;Line Mode&gt;

| Command   | Normal                            | Thermal Paper                | Label Paper                                        | Label Paper                                       |
|-----------|-----------------------------------|------------------------------|----------------------------------------------------|---------------------------------------------------|
|           |                                   |                              | Tear Bar                                           | Peel Mode                                         |
| <FF>      | <FF>                              | Form Feed                    | Label Gap Detection                                | Label Gap Detection + Peeling Position Conveyance |
| <ESC> d n | n = 0, 48 n = 1, 49               | Tear Bar Position Conveyance | Label Gap Detection + Tear Bar Position Conveyance | Label Gap Detection + Peeling Position Conveyance |
| <ESC> d n | n = 2, 50 n = 3, 51 n = 116 ('t') | Tear Bar Position Conveyance | Label Gap Detection + Tear Bar Position Conveyance | Label Gap Detection + Peeling Position Conveyance |

## &lt;Raster Mode FF/EOT&gt;

| Command   |         | Normal Thermal Paper         | Label Paper                  | Label Paper                 |
|-----------|---------|------------------------------|------------------------------|-----------------------------|
|           |         |                              | Tear Bar                     | Peel Mode                   |
| Form Feed | Valid   | Print                        | Print + Label Gap Detection  | Print + Label Gap Detection |
|           | Invalid | Print                        | Print + Label Gap Detection  | Print + Label Gap Detection |
| Cut Feed  | Valid   | Tear Bar Position Conveyance | Tear Bar Position Conveyance | Peeling Position Conveyance |
|           | Invalid | ---                          | ---                          | Peeling Position Conveyance |

-----------------------------------------------------------------------------
