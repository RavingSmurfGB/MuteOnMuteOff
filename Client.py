import pystray
from PIL import Image
from pystray import MenuItem as item

m = False


#This sets the variables Muteon and Muteoff to the pictures in the location.
Muteon = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteon.png')
Muteoff = Image.open(r'C:\Users\Joe\Documents\GitHub\MuteOnMuteOff\Images\Muteoff.png')




# This code will create an icon in the task bar and set to either the variable (pictue) Muteon or Muteoff
# This code also will need to be run in a continues loop so threading is needed for any other code to run
while True:

    if m == True:

        icon = pystray.Icon(name="name", icon=Muteon, title="Muted")
        icon.run()

    if m == False:

        icon = pystray.Icon(name="name", icon=Muteoff, title="Un Muted")
        icon.run()