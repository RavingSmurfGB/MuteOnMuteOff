from logipy import logi_led
import time



#logi_led.load_dll(path_dll="C:\Program Files\LGHUB\sdk_legacy_led_x64.dll")
logi_led.logi_led_init()
time.sleep(5) # Give the SDK a second to initialize
logi_led.logi_led_set_target_device(815)
time.sleep(1)
#logi_led.logi_led_flash_lighting(0, 255, 0, 10, 1)
logi_led.logi_led_set_lighting(0, 0, 255)
logi_led.logi_led_shutdown()

print("poop")