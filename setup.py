import os, shutil, pathlib, ctypes, time, sys, glob

current_file_path = pathlib.Path(__file__).parent.absolute() #This will get the current file path but will not update if you move the setup.py, move the setup.py last 
print(current_file_path)

#-1. Relaunch program as admin if not:                          Not Working
#0. Install pip requirements!!!                                 Not started

#1. Move files to setup at launch:                              Done
#2. Move files to start menu:                                   Done
#3. Move all files to program files in permanent location       Not started
#4. Launch program                                              Not started

#*. Perhaps work on gui showing what is happening
#*. Recreate the shortcuts under programfiles...
#*. If already installed perhaps delete and reinstall



#-1.#////////////////////////////////Admin Check///////////////////////////////
#Is ran to determine if the program was started with admin rights, if so continues, if not uac prompt 

###DOES NOT WORK..................................................................................................................................
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    print("Setup already initialised with Administrator rights")
else:
    # Re-run the program with admin rights
    print("Setup was not started with Administrator rights, restarting...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


'''
#1.#////////////////////////////////Setting launch at Startup///////////////////////////////
print("Setting program to start on boot")

#Get's current username
username = os.getlogin()



dst_launch_startup_path = ("C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup") #Creates the path to startup, including the current user.
src_launch_startup_path = current_file_path.joinpath("support_files\\startup") #Adds support_files\startup to the current file path
print(src_launch_startup_path)



file_names = os.listdir(src_launch_startup_path)
for file_name in file_names:
    shutil.move(os.path.join(src_launch_startup_path, file_name), dst_launch_startup_path)
#///////////////////////////////
'''



'''
#2.#////////////////////////////////Adding to start menu///////////////////////////////

#C:\ProgramData\Microsoft\Windows\Start Menu\Programs


dst_launch_startup_path = ("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs") #Creates the path to startup, including the current user.
src_launch_startup_path = current_file_path.joinpath("support_files\\start_menu") #Adds support_files\startup to the current file path
print(src_launch_startup_path)


try:
    file_names = os.listdir(src_launch_startup_path)
    for file_name in file_names:
        shutil.move(os.path.join(src_launch_startup_path, file_name), dst_launch_startup_path)
except:
    print("ERROR: Most likley did not run as administrator")
#///////////////////////////////

'''




#3. ////////////////////////////////Moving Main Files///////////////////////////////

 ###################################################################################################currently get's confused with subdirectories and errors
print("Moving main files \n")


source_dir = current_file_path
target_dir = 'C:\\Program Files\\MuteOnMuteOff ' #actual destinatiommmn C:\Program Files 
file_names = os.listdir(source_dir)

p = pathlib.Path(target_dir)

for file_name in file_names:
    if p.is_dir == False:
        p.mkdir(target_dir)
    shutil.move(os.path.join(source_dir, file_name), target_dir)  ## trie shutil.moveAndCreateDir insted!!!!!



'''
#try:
print("Moving files to program files \n")
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)  ## trie shutil.moveAndCreateDir insted!!!!!
#except:
 #   print("ERROR: Most likley did not run as administrator")
#///////////////////////////////
'''