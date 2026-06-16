## C O N F I D E N T I A L

- ■ 'Label peeling position' is the position where the label can be peeled off by hand. Details are different depending on the model.
- ■ Models with the peeling function will be in the label removal waiting status when Function 65 is executed. This status continues during label removal and printer reset or label removal and power off. The label removal waiting status can be checked by DLE EOT ( n = 8, a = 3: Peeler status).

[Model-dependent variations]

TM-L90 , TM-P60

## TM-L90

The following operation is executed according to a set value of the paper layout.

| Set value of paper layout                                                                                            | Operation                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Paper layout ( sb - se ) is less than 24 mm{0.94 inch} or Paper layout ( sb - se ) is more than or 29mm {1.1 inches} | Execute the paper feed to the manual cutter position by 'Cutting position' ( se ) specified by the paper layout. |
| Paper layout ( b - e ) is between 24 mm{0.94 inch} and 29mm {1.1 inches}                                             | Execute the paper feed by the amount which corresponds to paper layout ( sb - se ).                              |

## TM-L90 with Peeler:

When the peeling issuing mode is selected, the status changes to label removal standby when this function is executed. You can check the label removal standby status with DLE EOT ( n = 8, a = 3: Peeler status) or the basic ASB status. When the label removal is checked by pressing the FEED button, the printer is in the waiting status for the FEED button to be pressed. The waiting status for the FEED button to be pressed can be checked by the basic ASB status or DLE EOT ( n = 1: Printer status) 'Online recovery waiting status.'

Switching between the peeling issuing mode and the continuous issuing mode can be done with a slide switch on the printer. This switch can be used when the roll paper cover is open.

## TM-P60

This function operates when ( sm = "1", "2") is specified for the layout reference.
