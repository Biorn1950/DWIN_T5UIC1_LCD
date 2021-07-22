DWIN_Screen.py:
    class T5UIC1_LCD
        - definition variable:
            - divers bytes
            - LCD size
            - font size
            - color
        - __init__
        - Handshake
        - LCD:
            - Backlight_SetLuminance
            - Frame_SetDir "Set screen display direction"
            - UpdateLCD (0x3d ???)
            - Frame_Clear
        - Draw:
            - Draw_Point
            - DrawPoint
            - Draw_Line
            - Draw_Rectangle
            - Frame_AreaMove
            - Draw_Circle
            - CircleFill
        - Text:
            - Draw_String
            - Draw_IntValue
            - Draw_FloatValue
            - Draw_Signed_Float
        - Image:
            - JPG_ShowAndCache
            - ICON_Show
            - JPG_CacheToN
            - JPG_CacheTo1
            - Frame_TitleCopy
            - ICON_Animation
            - ICON_AnimationControl
        - commented:
            - qr
            - memory
            - function

dwinlcd.py:





MENUS

    - home
        - Print
            -
        - Prepare
            - < back
            - move >
                - < Back
                - Move X
                - Move Y
                - Move Z
                - Extruder
            - Disable stepper
            - Auto Home
            - Z-offset +/-
            - Preheat PLA
            - Preheat ABS
            - Cool Down
        - Control
            - < Back
            - Temperature >
                - < Back
                - Nozlle temperature
                - Bed temperature
                - Fan speed (missing bug)
                - Preheat PLA >
                    - < Back
                    - Nozzle temperature
                    - Bed temperature
                    - Fan speed (misssing buggy)
                    - Save prameters
                - Preheat ABS >
                    - < Back
                    - Nozzle temperature
                    - Bed temperature
                    - Fan speed (misssing buggy)
                    - Save prameters
            - Motion >
                - MaxSpeed > (misssing)
                - MaxAcceleration > (misssing)
                - Step per mm > (misssing)
            - Info > (return to info)
        - Info
            - < Back
            - Size
            - Firmware
            - Contact details
    ******************************************************
    - Status
        - hotend temp
        - bed temp
        - fan speed
        - z offset





Divers:

    Todo
        -

    To fix
        - self.Draw_Print_ProgressRemain()
        - 

    Temp fix:
        - Octo to moonraker for boot
        - replace feedrate_percentage by fan speed

    Fixed
        - Involuntary double clic "ENTER"
        - Encoder not sync with rest pos
        - Display issue on exit
        - Sync homing popup

    Removed
        - encoderRate = true -> no wait

