**==> picture [392 x 518] intentionally omitted <==**

**----- Start of picture text -----**<br>
</OBJECT><br><!-- PTZ Control ActiveX --><br><OBJECT ID="PTZCtrl"<br>    WIDTH = 1<br>    HEIGHT= 1<br>    CLASSID="CLSID:5506B06A-9FED-4dc0-99E1-9AEF2F2B0509"><br></OBJECT><br><FORM NAME="myForm"><br><table><br>    <tr><br>        <td><br>            VN-H37 IP Address<br>            <INPUT TYPE="TEXT" NAME="IP" VALUE="192.168.0.2"><br>            HTTP Port<br>            <INPUT TYPE="TEXT" NAME="HTTP_PORT" VALUE="80"><br>        </td><br>    </tr><br>    <tr><br>        <td><br>            Viewer<br>            <INPUT TYPE="BUTTON" NAME="PLAY_BTN" style="width:70px"<br>                                                           VALUE="Play"  onclick="play_click(PLAY_BTN,  IP,<br>HTTP_PORT)"><br>            <INPUT TYPE="BUTTON" NAME="CAPTURE_BTN" style="width:70px"<br>                                                           VALUE="Capture"  onclick="capture_click()"><br>        </td><br>    </tr><br></table><br><p STYLE="top:506px;left:21px;position:absolute" >PTZ Control</p><br><INPUT TYPE="BUTTON" VALUE="Up"<br>            STYLE="width:40px;top:530px;left:61px;position:absolute"<br>            onmousedown="PTControl(8)" onmouseup="mouse_up()" onmouseout="mouse_up()"><br><INPUT TYPE="BUTTON" VALUE="Left"<br>            STYLE="width:40px;top:550px;left:41px;position:absolute"<br>            onmousedown="PTControl(4)" onmouseup="mouse_up()" onmouseout="mouse_up()"><br><INPUT TYPE="BUTTON" VALUE="Right"<br>            STYLE="width:40px;top:550px;left:81px;position:absolute"<br>            onmousedown="PTControl(6)" onmouseup="mouse_up()" onmouseout="mouse_up()"><br><INPUT TYPE="BUTTON" VALUE="Down"<br>            STYLE="width:40px;top:570px;left:61px;position:absolute"<br>            onmousedown="PTControl(2)" onmouseup="mouse_up()" onmouseout="mouse_up()"><br><INPUT TYPE="BUTTON" NAME="TELE_BTN" VALUE="+"<br>            STYLE="width:40px;top:535px;left:134px;position:absolute"<br>            onmousedown="ZoomControl(0)" onmouseup="mouse_up()" onmouseout="mouse_up()"><br><INPUT TYPE="BUTTON" NAME="WIDE_BTN" VALUE="-"<br>            STYLE="width:40px;top:565px;left:134px;position:absolute"<br>            onmousedown="ZoomControl(1)" onmouseup="mouse_up()" onmouseout="mouse_up()"><br></FORM><br></BODY><br></HTML><br>**----- End of picture text -----**<br>


## **34.6 Notes** 

- Enable the JPEG/H.264 frame size that you want in “Basic Settings2” or “Encoding” page of the camera. 

- Start Multicast stream on the camera Web page to use Multicast. The ActiveX control does not send request to the camera for starting Multicast stream. 

107 

Downloaded from www.Manualslib.com manuals search engine 
