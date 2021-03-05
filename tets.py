import time, os, sys

print("hi there folks")

time.sleep(2)

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar

print("good bye now")

time.sleep(2)

os.system('cls') # Clears the screen
input("Press Enter to continue...") # Makes the user hit enter to conitnue