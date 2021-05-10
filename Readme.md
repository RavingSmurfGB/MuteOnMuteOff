
# MuteOnMuteOff
A Python script that mutes and unmutes your microphone, via hotkey or Macro!

## Contents
* [How It Works](#How_It_Works)
* [Installation](#Installation)
* [Setup](#Setup)
* [References](#References)


## How It Works
This program will mute and unmute your microhpone via a hotkey or a macro key.
You will need python for this program and was created using Python 3.9.5 although the latest update should work!

Download here: https://www.python.org/downloads/windows/

The default hotkey to Mute/ Unmute is ctrl + enter

You will need to confugre the microphone in order to use this program, see ...

## Installation
### Automated Install
 1. Extract .zip
 2. Run setup.py
 3. Double check that all files where moved to `C:\Py_Ormolu\MuteOnMuteOff`
 > By Default the Program will be added to start menu and set to boot on power up, if this is not wanted follow Manual Install

### Manual Install
 1. Create Folder path `C:\Py_Ormolu\MuteOnMuteOff`
 2. Extract .zip contents to above path
 3. If user wants the program to startup with Windows: 
> Copy the shortcut located under: `C:\Py_Ormolu\MuteOnMuteOff\support_files\startup`
> 
> Then move it to the following path: 
> `AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
> Find AppData on your device by pressing the keys `Win + R`
 4. If the user wants the program to be added to the Start Menu
> Copy the shortcut located under: `C:\Py_Ormolu\MuteOnMuteOff\support_files\start_menu` 
> Then move it to the following path: `C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs`
 5. Install the requirements by opening a Command Prompt Window 
> pip install pillow  
> pip install keyboard  
> pip install pystray  
> pip install progressbar2 


## Setup
  This section will cover setting up the program for your use.
### Configuring the Microhpone   
In this example we are configuring the Microhpone called Focusright Usb Audio
 1. Open Windows Sound Control Panel; Start > Control Panel > Hardware and Sound > Sound > Recordings tab
 2. Take note of the exact spelling which microphone you would like this program to use
 
![alt text](https://github.com/RavingSmurfGB/MuteOnMuteOff/blob/master/Images/Microhpone_config.png "Logo Title Text 1")
> Only use the second line, here we should use Focusright Usb Audio as the text
 3. Navitage to C:\Py_Ormolu\MuteOnMuteOff in Windows explorer
 4. Right click on config.cfg and open with, scroll down and select Notepad
 5. Scroll down under "Configuration:" and change the microhpone name fetched earlier after MICROPHONE_TO_USE:
 ![alt text](https://github.com/RavingSmurfGB/MuteOnMuteOff/blob/master/Images/Windows%20Sound%20Control%20Panel.png "Logo Title Text 1")
 6. Save the file.

### Configuring the Hotkey
The default hotkey for the program is ctrl + enter, If you would like to change this:
1. Navitage to C:\Py_Ormolu\MuteOnMuteOff in Windows explorer
2. Right click on config.cfg and open with notepad, scroll down and select Notepad
3. Scroll down under "Configuration:" and append after KEYBOARD_HOTKEY: the keys/key you would like to use
> Enter the keys you would like to use exactly as seen on your keyboard, with a + inbetween then if you have multiple keys you would like to use.
> The text entered should all be in lower case.
> 

![alt text](https://github.com/RavingSmurfGB/MuteOnMuteOff/blob/master/Images/Hotkey_config.png "Logo Title Text 1")


Following these instructions above the default ctrl + enter

![alt text](https://github.com/RavingSmurfGB/MuteOnMuteOff/blob/master/Images/Hotkey_config.png "Logo Title Text 1")


Is changed to hhift






## References
This program utilises Sound Volume view by Nirsoft in order to control the microphone.
https://www.nirsoft.net/articles/mute_microphone_command_line.html
