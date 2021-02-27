import pystray, os, keyboard, subprocess, yaml
from PIL import Image
from pystray import MenuItem as item
from pathlib import Path

#/////////////////////////// TO DO LIST ///////////////////////////////////////////////
# 
# clean up any unused code                                                                      Done
# move essential program files to another directory                                             Partly
# change image links to dynamic using pathlib
# fix setup.py permissions errors
# implement other configuration options import to code from file
# implement 
# look into using a windows command to mute microphone
# look into querying whether the microphone is muted or not, rather than using mute.dat 
# in setup.py detect whether the folders exist before copying
# in setup.py have try/except in place to catch any errors
# setup.py gui
# setup.py option to reinstall






#////////////////////////////////Startup///////////////////////////////

#This loads the file config.cfg and then pulls and assigns each variable as needed
with open("config.cfg", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.SafeLoader)
    print("Read successful")

keyboard_hotkey = (data[0]['Configuration']['KEYBOARD_HOTKEY'])

#Define variable m to be used whether the microphone is currently muted or not
m = "unsure"

try: #Creates file if not exists for non-volitile storage
    my_file = Path("mute.dat")
    if my_file.is_file():
        print("file exists")
    else:
        f = open("mute.dat", "x")
        f.close()
        f = open("mute.dat", "w")
        f.write("Unmuted")
        f.close()
except:
    print("file mute.dat already created ")

try: #Loads the vlalue from mute.dat and assigns it to the variable m
    f = open("mute.dat", "rt")
    contents = f.read()
    f.close()
    print(contents)
    if contents == "Muted":
        m = "Muted"
        print(" m set to muted")
    elif contents == "Unmuted":
        m = "Unmuted"
        print(" m set to unmuted")
    else:
        m = "Unmuted"
        print("VAIRBLAE WAS CHANGED")
except:
    print("something really broke")
#////////////////////////////////



#////////////////////////////////IMAGE FILES///////////////////////////////
#This sets the variables Muteon and Muteoff to the pictures in the location.
Muteon = Image.open(r'C:\\Users\\Joe\\Documents\\GitHub\\MuteOnMuteOff\\Images\\Muteon.png')
Muteoff = Image.open(r'C:\\Users\\Joe\Documents\\GitHub\\MuteOnMuteOff\\Images\\Muteoff.png')
#////////////////////////////////






#////////////////////////////////CORE CODE///////////////////////////////
#This code mutes and mutes the mic
def Mute():
    global m
    global icon
    print("I GOT TO THE MUTE STAGE")
    subprocess.call('cmd /c "start SoundVolumeView.exe /Mute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Muted")
    f.close()
    m = "Muted"
    print(m)
    icon.notify(message= " ", title="Muted")
    icon.visible = False #sets the icon invisible
    icon.stop()
   
#This code mutes and un mutes the mic
def Unmute():
    global m
    global icon
    print("I GOT TO THE UNMUTE STAGE")
    subprocess.call('cmd /c "start SoundVolumeView.exe /Unmute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Unmuted")
    f.close()
    m = "Unmuted"
    print(m)
    icon.notify(message= " ", title="Unmuted")
    icon.visible = False
    icon.stop()

#This code will choose whether to mute ot not to mute...
def ToMuteOrNotToMute():
    global m
    if m == "Muted":
        Unmute()

    elif m == "Unmuted":
        Mute()

#This code sets the key binding to Ctrl & Enter in order to active the ToMuteOrNotToMute function
keyboard.add_hotkey(keyboard_hotkey, ToMuteOrNotToMute, args=(), suppress=False, timeout=1, trigger_on_release=False)

#Exits the program
def exit():
    icon.visible = False
    icon.stop()
    os._exit(0)

#Opens the sound panel menu
def sound_panel():
    subprocess.call('cmd /c "start mmsys.cpl soundsmmsys.cpl sounds "')

#Restarts the program
def restart():
    print("restarted Program")
    subprocess.call("cmd /c \support_files\\relaunch.vbs")
    exit()

#Opens the config file for the program
def config_file():
    print("Opened config file")
    programName = "notepad.exe"
    fileName = "config.cfg"
    subprocess.Popen([programName, fileName])
#////////////////////////////////

#////////////////////////////////Icon loop///////////////////////////////
#Declares the menu itmes that will be used in the icon menu
configure_menu = item('Configure', config_file, default=False)
exit_menu = item('Exit', exit, default=False)
relaunch_menu = item('Relaunch', restart, default=False)
sound_panel_menu = item('Sound Panel', sound_panel, default=True)

# This code will create an icon in the task bar and set to either the variable (pictue) Muteon or Muteoff
# This code also will need to be run in a continues loop so threading is needed for any other code to run
while True:

    if m == "Muted":
        menu = pystray.Menu(relaunch_menu, exit_menu, configure_menu, sound_panel_menu) 
        icon = pystray.Icon(name="name", icon=Muteon, title="Muted", menu=menu)
        icon.run()



    elif m == "Unmuted":
        menu = pystray.Menu(relaunch_menu, exit_menu, configure_menu, sound_panel_menu) 
        icon = pystray.Icon(name="name", icon=Muteoff, title="Unmuted", menu=menu)
        icon.run()

#////////////////////////////////


###TO DO LIST
'''
create a config entry to turn notifications on and off, then implement the config entry in the code
CREATE SETUP FILE WHICH INSTALLS TO PROGRAM FILES
 -- THEN CLEAN UP FILE LOCATIONS IN THE PROGRAM IN TO DIFFERENT FOLDERS
 -- PUT SHORTCUT IN STARTUP AND WINDOWS TASK BAR AUTO


'''