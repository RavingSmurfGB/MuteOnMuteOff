import pystray, os, keyboard, time, threading
from PIL import Image
from pystray import MenuItem as item
from pathlib import Path

#Define variable M
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
    os.system('cmd /c "start SoundVolumeView.exe /Mute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Muted")
    f.close()
    m = "Muted"
    print(m)
    icon.stop()
   


#This code mutes and un mutes the mic
def Unmute():
    global m
    global icon
    print("I GOT TO THE UNMUTE STAGE")
    os.system('cmd /c "start SoundVolumeView.exe /Unmute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Unmuted")
    f.close()
    m = "Unmuted"
    print(m)
    icon.stop()


#This code will choose whether to mute ot not to mute...
def ToMuteOrNotToMute():
    global m
    if m == "Muted":
        Unmute()

    elif m == "Unmuted":
        Mute()



keyboard.add_hotkey("ctrl+enter", ToMuteOrNotToMute, args=(), suppress=False, timeout=1, trigger_on_release=False)


#////////////////////////////////Icon loop///////////////////////////////
# This code will create an icon in the task bar and set to either the variable (pictue) Muteon or Muteoff
# This code also will need to be run in a continues loop so threading is needed for any other code to run


while True:

    if m == "Muted":
        #print("muted")
        icon = pystray.Icon(name="name", icon=Muteon, title="Muted")
        icon.run()


    elif m == "Unmuted":
        #print("unmuted")
        icon = pystray.Icon(name="name", icon=Muteoff, title="Unmuted")
        icon.run()

#////////////////////////////////


