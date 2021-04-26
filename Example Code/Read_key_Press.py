import keyboard

#This program will simply listen for a single key press and print out the key it detects it as
# very usefull for detecting what your macro keys are...

print(keyboard.read_key(suppress=False))
