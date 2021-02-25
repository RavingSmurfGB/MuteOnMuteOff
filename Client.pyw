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
Muteon = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteon.png')
Muteoff = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteoff.png')
#////////////////////////////////





#////////////////////////////////CORE CODE///////////////////////////////

#This code mutes and mutes the mic
def Mute():
    #global m
    print("I GOT TO THE MUTE STAGE")
    os.system('cmd /c "start SoundVolumeView.exe /Mute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Muted")
    f.close()
    m = "Muted"
    print(m)

    icon.stop


#This code mutes and un mutes the mic
def Unmute():
    #global m
    print("I GOT TO THE UNMUTE STAGE")
    os.system('cmd /c "start SoundVolumeView.exe /Unmute Scarlett Solo USB "')
    f = open("mute.dat", "w")
    f.write("Unmuted")
    f.close()
    m = "Unmuted"
    print(m)

    icon.stop

#This code will choose whether to mute ot not to mute...
def ToMuteOrNotToMute():
    global m
    if m == "Muted":
        Unmute()

    elif m == "Unmuted":
        Mute()




#neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeds to be in a infinte loop (in another thread)
#Alsoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo look in to using keyboard.on_release aswell # to act everytime you release the buttons
# This code detects keyboard input and run the mute definition
def hotkey():
    while True:
        if keyboard.is_pressed("ctrl") & keyboard.is_pressed("enter"):
            print("You activated my trap card")
            ToMuteOrNotToMute()
            time.sleep(1)
#////////////////////////////////




#breakthread = True # this controls wether the while loop in main will run
t = threading.Thread(target=hotkey, name = "(hi, I'm a thread)") # set's t to equal a variable
t.start() # this starts the thread





#////////////////////////////////Icon loop///////////////////////////////
# This code will create an icon in the task bar and set to either the variable (pictue) Muteon or Muteoff
# This code also will need to be run in a continues loop so threading is needed for any other code to run


while True:

    if m == "Muted":
        #print("muted")
        icon = pystray.Icon(name="name", icon=Muteon, title="Muted")
        icon.run()

    if m == "Unmuted":
        #print("unmuted")
        icon = pystray.Icon(name="name", icon=Muteoff, title="Unmuted")
        icon.run()
#////////////////////////////////


