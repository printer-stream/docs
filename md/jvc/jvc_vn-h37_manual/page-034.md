**Interpretation** Acquire resolution of the encode channel. Encode channel is from encode(1) to encode(3). 

**Allowed users** admin, operator, user 

## **Setting Resolution (Frame Size)** 

## **Format   /api/param?encode(number).framesize=data** 

## **Example  /api/param?encode(1).framesize=1920x1080** 

## **Example of response   encode(1).type&202 Accepted(encode.status=save)** 

**Interpretation** Change resolution of the encode channel.  Set "1920x1080", "quadvga", "1280x720", "vga", 

"qvga" or "640x360". The change of the first encode channel is availed by the API, encode(1). 

Maximum resolution of VN-H37/137/237/57/157/257 is 1920x1080. 

Maximum resolution of VN-V17/217 is 1280x720. 

Caution: All channels need to have same aspect ratio, 16:9 or 4:3. 

**Allowed users** admin, operator 

## **Getting Rate Control Setting** 

## **Format  /api/param?encode(number).cbr_mode** 

## **Example of response  encode(1).cbr_mode=afs&200 OK** 

**Interpretation** Acquire the rate control setting. 

When compression format is JPEG, "vfs" or "afs" is returned. Quantization table is fixed in the case of vfs (VariableFileSize). In the case of afs (AverageFileSize), bit rates are controlled such that the average size of 

multiple files remains constant. 

When compression format is H.264 or MPEG-4, "cbr" or "vbr" is returned. Bitrate is controlled to be constant in the case of cbr (Constant Bitrate). In the case of vbr (Variable Bitrate), bitrate can be larger by input image. **Allowed users** admin, operator, user 

## **Setting Rate Control** 

**Format   /api/param?encode(number).cbr_mode=data** 

## **Example  /api/param?encode(1).cbr_mode=vfs** 

## **Example of response   encode(1).cbr_mode&202 Accepted(encode.status=save)** 

**Interpretation** Change rate control. When compression format is JPEG, set "vfs" or "afs". This parameter is not included file size/quality information. Parameters of JPEG File Size can be set by other APIs, 

encode(number).quality. 

When compression format is H.264 or MPEG-4, set "cbr" or "vbr". The change of the first channel is availed by the API, encode(1).status=save. 

**Allowed users** admin, operator 

31 

Downloaded from www.Manualslib.com manuals search engine 
