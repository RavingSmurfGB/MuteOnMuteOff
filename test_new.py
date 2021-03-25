''' # how to find and kill by process id
import os, signal

pid = os.getpid()
print(pid)

os.kill(pid, signal.SIGTERM)
print("hi there")
input("Press Enter to continue...") # Makes the user hit enter to conitnue
'''





import psutil, os, signal


#pid = os.getpid()

with open('support_files\\current_pid.dat', 'r') as file: #Creates mute.dat and writes Unmuted to it  # 'w+' can create, write and read the file  
    pid = file.read()
    os.kill(pid, signal.SIGTERM) 