**Allowed users** admin, operator, user 

## **Getting Preset Data of Scene File** 

**Format  /api/param?camera.scene(number).status** 

## **Example of getting scene file 0  /api/param?camera.scene(0).status** 

## **Example of response** 

## **camera.scene(0).status=General-55--0.45-30-auto-off-0-51-off-low-53-mid-autoM-2-combo-color-8-8-auto** 

## **W-107-65-off-off-0-normal&200 OK** 

**Interpretation** Acquire preset data of specified scene file. The preset data is joined with hyphen as follows. scenename-color-monitortype[*1] -gamma-shutter-brightness.highgain[*2] -auto_focus-iris-pedestal-autoblack[*1] -enha nce_band[*1] -enhance-3ddnr-brightness-senseup_limit-auto_exposure.priority-true_daynight[*2] -avpk_color-avpk_b w[*3] -white_balance-white_balance_r-white_balance_b-blc-clvi-autoexposure.reference-atw_convergence[*1 ] parameter that is marked with[*1  ] : The parameter is not used or data value is invalid. parameter that is marked with[*2  ] : The parameter is used for VN-H37and VN-H237VP. parameter that is marked with[*3  ] : The parameter is used for VN-H137and VN-H237. **Allowed users** admin, operator, user 

## **Loading/Saving/Initializing Scene File** 

**Format  /api/param?camera.scene(number).status=data** 

**Example of loading scene file 0   /api/param?camera.scene(0).status=goto** 

**Example of saving scene file 0   /api/param?camera.scene(0).status=save** 

**Example of initializing scene file 0   /api/param?camera.scene(0).status=initialize** 

## **Example of response  camera.scene(0).status&200 OK** 

**Interpretation** Load/save/initialize scene file setting. Specify from scene(0) to scene(7). Loading scene file changes current camera settings. Saving scene file saves setting s of specified scene file. Initializing scene file changes settings of specified scene file to default values. 

**Allowed users** admin, operator 

## **Getting Current Scene File Name** 

**Format  /api/param?camera.scene(number).name** 

## **Example of response  camera.scene(0).name=general&200 OK** 

**Interpretation** Acquire current scene file name. Range of scene file number is between 0 to 7. 

Scene file names are General, Indoor, Outdoor, CLVI, Traffic, DataSaving, Day, and Night. Scene file name is read only. 

**Allowed users** admin, operator, user 

22 

Downloaded from www.Manualslib.com manuals search engine 
