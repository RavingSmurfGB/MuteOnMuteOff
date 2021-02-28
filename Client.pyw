import pystray, os, keyboard, subprocess, yaml, pathlib
from PIL import Image
from pystray import MenuItem as item


#/////////////////////////// TO DO LIST ///////////////////////////////////////////////
# 
# clean up any unused code                                                                      Done
# move essential program files to another directory                                             Done
# change shortcuts to referance under program files                                             Done
# change image links to dynamic using pathlib                                                   Done
# change any other code to referance current directory using pathlib                            Done
# implement other configuration options import to code from file                                Done
# implement turning notifications on and off                                                    Done
# implement logitech LED control
# implement logging # ideally converting print statements or summit
# look into using a windows command to mute microphone
# enable microphone selection 
# look into querying whether the microphone is muted or not, rather than using mute.dat 
# setup.py to get information from requirements and install, maybe using yaml??
# in setup.py detect whether the folders exist before copying
# in setup.py have try/except in place to catch any errors
# setup.py gui
# setup.py option to reinstall
# setup.py option to uninstall, passing through to a uninstall.py
# change creation of file to use with open and pathlib where appropriate                        Done
# re-write readme to make it fancy
# Perhaps change name to PyMute                                                              


#///////////////////////// Current errors:

#       perhaps lookinto https://superuser.com/questions/55598/super-key-to-pause-mute-mic-and-mute-speakers-in-windows
# setup.py admin check does not work, ideally allways open as admin
# setup.py cannot move all subdirectories, it does not create the subdirectories in the target location (permision error)






#////////////////////////////////Startup///////////////////////////////
#This loads the file config.cfg and then pulls and assigns each variable as needed
with open("config.cfg", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.SafeLoader)
    print("Config file read successful")

keyboard_hotkey = (data[0]['Configuration']['KEYBOARD_HOTKEY'])
windows_notifications = (data[0]['Configuration']['WINDOWS_NOTIFICATIONS'])
logging = (data[0]['Configuration']['LOGGING'])
keyboard_integration = (data[0]['Configuration']['KEYBOARD_INTEGRATION'])
microphone_to_use = (data[0]['Configuration']['MICROPHONE_TO_USE'])


#Get the current directory for where the program is ran
current_file_path = pathlib.Path(__file__).parent.absolute() #This will get the current file path but will not update if the .py is moved


#Define variable m to be used whether the microphone is currently muted or not
m = "unsure"

#Creates mute.dat if not already created
try: 
    if pathlib.Path("support_files\\mute.dat").is_file(): #Checks if mute.dat exists if so prints file.exists and continues
        print("file exists")
    else:
        with open('support_files\\mute.dat', 'w+') as file: #Creates mute.dat and writes Unmuted to it  # 'w+' can create, write and read the file  
            file.write("Unmuted")
except:
    print("file mute.dat cannot be read ")


try: #Loads the vlalue from mute.dat and assigns it to the variable m
    with open('support_files\\mute.dat', 'rt') as file:
        contents = file.read()
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


#This sets the variables Muteon and Muteoff to the .png's under Images.
Muteon = Image.open("Images\\Muteon.png")
Muteoff = Image.open("Images\\Muteoff.png")

#////////////////////////////////











#////////////////////////////////CORE CODE///////////////////////////////
#This code mutes and mutes the mic
def Mute():
    global m        #Sets m varible to be global so it can be read outisde of the function
    global icon     #Sets icon varible to be global so it can be read outisde of the function
    print("I GOT TO THE MUTE STAGE")
    subprocess.call('cmd /c "start support_files\\SoundVolumeView.exe /mute Scarlett Solo USB "')
    with open('support_files\\mute.dat', 'w') as file: #writes muted to mute.dat    
            file.write("Muted")
    m = "Muted"
    print(m)
    if windows_notifications == True: #Checks to see whether notications are enabled, if so pushes
        icon.notify(message= " ", title="Muted")
    icon.visible = False #sets the icon invisible
    icon.stop()
   

#This code mutes and un mutes the mic
def Unmute():
    global m        #Sets m varible to be global so it can be read outisde of the function
    global icon     #Sets icon varible to be global so it can be read outisde of the function
    print("I GOT TO THE UNMUTE STAGE")
    subprocess.call('cmd /c "start support_files\\SoundVolumeView.exe /unmute Scarlett Solo USB "')
    with open('support_files\\mute.dat', 'w') as file: #writes unmuted to mute.dat    
            file.write("Unmuted")
    m = "Unmuted"
    print(m)
    if windows_notifications == True: #Checks to see whether notications are enabled, if so pushes
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
    relaunch_script = current_file_path.joinpath("support_files\\relaunch.vbs") #Adds the relaunch script to the current directory path
    subprocess.call("cmd /c " + str(relaunch_script)) #str() is needed to convert the windows_path to a string for subproccess
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
