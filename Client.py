import pystray, os
from PIL import Image
from pystray import MenuItem as item

#Defining the variable m for whether mic is muted or not, this will change to load value on startup
m = False


#This sets the variables Muteon and Muteoff to the pictures in the location.
Muteon = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteon.png')
Muteoff = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteoff.png')




#This code mutes and un mutes the mic
def Mute():
    os.system('cmd /c "start SoundVolumeView.exe /Mute Scarlett Solo USB "')

def Unmute():
    os.system('cmd /c "start SoundVolumeView.exe /Unmute Scarlett Solo USB "')

Mute()

# This code will create an icon in the task bar and set to either the variable (pictue) Muteon or Muteoff
# This code also will need to be run in a continues loop so threading is needed for any other code to run
while True:

    if m == True:

        icon = pystray.Icon(name="name", icon=Muteon, title="Muted")
        icon.run()

    if m == False:

        icon = pystray.Icon(name="name", icon=Muteoff, title="Un Muted")
        icon.run()