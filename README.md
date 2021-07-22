# DWIN_T5UIC1_LCD

!!!   NOT REALLY WORKING, I HAVE JUST PUSHED THE FIRST STUFF THAT GIVEN SOMETHING BOOTABLE  !!!

!!!                 FEEL FREE TO OPEN FEATURE REQUEST AND ISSUE                             !!!

!!!                    I'll spend some time on it these weeks                               !!!


## Python class for the Ender 3 V2 LCD runing klipper3d with Moonraker 

https://www.klipper3d.org

https://github.com/arksine/moonraker


## Setup:

### [Disable Linux serial console](https://www.raspberrypi.org/documentation/configuration/uart.md)
  By default, the primary UART is assigned to the Linux console. If you wish to use the primary UART for other purposes, you must reconfigure Raspberry Pi OS. This can be done by using raspi-config:

  * Start raspi-config: `sudo raspi-config.`
  * Select option 3 - Interface Options.
  * Select option P6 - Serial Port.
  * At the prompt Would you like a login shell to be accessible over serial? answer 'No'
  * At the prompt Would you like the serial port hardware to be enabled? answer 'Yes'
  * Exit raspi-config and reboot the Pi for changes to take effect.
  
  For full instructions on how to use Device Tree overlays see [this page](https://www.raspberrypi.org/documentation/configuration/device-tree.md). 
  
  In brief, add a line to the `/boot/config.txt` file to apply a Device Tree overlay.
    
    dtoverlay=disable-bt

### [Enabling Klipper's API socket](https://www.klipper3d.org/API_Server.html)
  By default, the Klipper's API socket is not enabled. In order to use the API server, the file /etc/default/klipper need to be updated form

    KLIPPY_ARGS="/home/pi/klipper/klippy/klippy.py /home/pi/printer.cfg -l /tmp/klippy.log"
To:

    KLIPPY_ARGS="/home/pi/klipper/klippy/klippy.py /home/pi/printer.cfg -a /tmp/klippy_uds -l /tmp/klippy.log"

### Library requirements 

  Thanks to [wolfstlkr](https://www.reddit.com/r/ender3v2/comments/mdtjvk/octoprint_klipper_v2_lcd/gspae7y)

  `sudo apt-get install python3-pip python3-gpiozero python3-serial git`

  `sudo pip3 install multitimer`

  `git clone https://github.com/Biorn1950/DWIN_T5UIC1_LCD.git`


### Wire the display 
  * Display <-> Raspberry Pi GPIO BCM
  * 1  - Nc
  * 2  - Nc
  * 3  - Rx   = 8  - GPIO14  (Tx)
  * 4  - Tx   = 10 - GPIO15  (Rx)
  * 5  - Ent  = 33 - GPIO13
  * 6  - Nc
  * 7  - A    = 35 - GPIO19
  * 8  - B    = 37 - GPIO26
  * 9  - Vcc  = 4  - (5v)
  * 10 - Gnd  = 6  - (GND)
### Optional wire for buzzer
  * 6  - BEEP = 31 - GPIO6


### Run The Code

Enter the downloaded DWIN_T5UIC1_LCD folder.
Make new file run.py and add

```python
#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

encoder_Pins = (26, 19)
button_Pin = 13
buzzer_Pin = 6
LCD_COM_Port = '/dev/ttyAMA0'
API_Key = 'XXXXXX'

DWINLCD = DWIN_LCD(
  LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	buzzer_Pin,
	API_Key
)
```

Run with `python3 ./run.py`

# Run at boot:

	Note: Delay of 30s after boot to allow webservices to settal.
	
	path of `run.py` is expected to be `/home/pi/DWIN_T5UIC1_LCD/run.py`

   `sudo chmod +x run.py`
   
   `sudo chmod +x simpleLCD.service`
   
   `sudo mv simpleLCD.service /lib/systemd/system/simpleLCD.service`
   
   `sudo chmod 644 /lib/systemd/system/simpleLCD.service`
   
   `sudo systemctl daemon-reload`
   
   `sudo systemctl enable simpleLCD.service`
   
   `sudo reboot`
   
   

# Status:

## Working:

  Status Area:
 
    * nozzle/bed temperature
    * Fan speed
    * Display Print time, Progress, Temps, and Job name.
    * Pause / Resume / Cancle Job
    * Tune Menu: Print speed & Temps

 Perpare Menu:
 
    * Disable stepper
    * Auto Home
    * Z offset
    * Preheat
    * cooldown
 
 Info Menu
 
    * Shows printer info.

  While printing
    * Pause
    * Resume
    * Cancel


## Notworking:

  The rest


# Thanks:
  
  * KevinOConnor --- For Klipper(https://github.com/KevinOConnor/klipper)
  * Arksine      --- For Moonraker(https://github.com/arksine/moonraker)
  * odwdinc      --- For DWIN_T5UIC1_LCD(https://github.com/odwdinc/DWIN_T5UIC1_LCD)

