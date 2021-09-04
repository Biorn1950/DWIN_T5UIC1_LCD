#!/usr/bin/env python3
from dwinlcd import DWIN_LCD
from lcd import T5UIC1_LCD

encoder_Pins = (26, 19)
button_Pin = 13
buzzer_Pin = 6
LCD_COM_Port = '/dev/tty.usbserial-A50285BI'
API_Key = '49f53c13b5504563a83e8f82c8b7186d'

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	buzzer_Pin,
	API_Key
)
