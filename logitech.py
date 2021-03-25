

from logipy import logi_led
import time

logi_led.logi_led_init()
time.sleep(1) # Give the SDK a second to initialize
logi_led.logi_led_set_lighting(255, 0, 0)
logi_led.logi_led_shutdown()

'''
from pynput.keyboard import Listener




def on_press(key):
    print("Key pressed: {0}".format(key))

def on_release(key):
    print("Key released: {0}".format(key))
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
'''