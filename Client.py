import pystray, os, keyboard, time
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
        m = Muted

    if contents == "Unmuted":
        m = Unmuted

except:
    print("something really broke")





#////////////////////////////////IMAGE FILES///////////////////////////////
#This sets the variables Muteon and Muteoff to the pictures in the location.
Muteon = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteon.png')
Muteoff = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteoff.png')
#////////////////////////////////





#////////////////////////////////CORE CODE///////////////////////////////

#This code mutes and mutes the mic
def Mute():
    os.system('cmd /c "start SoundVolumeView.exe /Mute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Muted")
    f.close()


#This code mutes and un mutes the mic
def Unmute():
    os.system('cmd /c "start SoundVolumeView.exe /Unmute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Unmuted")
    f.close()


#This code will choose whether to mute ot not to mute...
def ToMuteOrNotToMute():
    if m == "Muted":
        Mute()

    if m == "Unmuted":
        Unmute()

#neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeds to be in a infinte loop (in another thread)
#Alsoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo look in to using keyboard.on_release aswell # to act everytime you release the buttons
# This code detects keyboard input and run the mute definition
while True:
    if keyboard.is_pressed("ctrl") & keyboard.is_pressed("enter"):
        ToMuteOrNotToMute()
        print("You pressed buttons")
        time.sleep(.500)
#////////////////////////////////





#////////////////////////////////Icon loop///////////////////////////////

# This code will create an icon in the task bar and set to either the variable (pictue) Muteon or Muteoff
# This code also will need to be run in a continues loop so threading is needed for any other code to run
while True:

    if m == True:

        icon = pystray.Icon(name="name", icon=Muteon, title="Muted")
        icon.run()

    if m == False:

        icon = pystray.Icon(name="name", icon=Muteoff, title="Un Muted")
        icon.run()
#////////////////////////////////