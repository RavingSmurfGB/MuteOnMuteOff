import os, shutil



#////////////////////////////////Moving Main Files///////////////////////////////
source_dir = '\\source'
target_dir = 'C:\\Users\\Joe\\Documents\\GitHub\\MuteOnMuteOff\\dest'
file_names = os.listdir(source_dir)

try:
    print("Moving files to program files \n")
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
except:
    print("Unable to move files")
#///////////////////////////////



#////////////////////////////////Setting launch at Startup///////////////////////////////
print("Setting program to start on boot")

#Get's current username
username = os.getlogin()


#Creates the path to startup, including the current user.
path = ("C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")



#shutil.copy(os.path.join(source_dir, file_names), target_dir)
#Moving the shortcut to startup
source_dir = 'C:\\Users\\Joe\\Documents\\GitHub\\MuteOnMuteOff\\source'
target_dir = 'C:\\Users\\Joe\\Documents\\GitHub\\MuteOnMuteOff\\dest'
file_name = os.listdir(source_dir)
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
#///////////////////////////////


#////////////////////////////////Adding to start menu///////////////////////////////

#C:\ProgramData\Microsoft\Windows\Start Menu\Programs

source_dir = 'C:\\Users\\Joe\\Documents\\GitHub\\MuteOnMuteOff\\source'
target_dir = 'C:\\Users\\Joe\\Documents\\GitHub\\MuteOnMuteOff\\dest'
file_name = os.listdir(source_dir)
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)