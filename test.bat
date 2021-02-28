@ECHO OFF
soundget, isMute, MICROPHONE, MUTE
if isMute = Off
    toMute = 1
else
    toMute=0
SoundSet, toMute, MICROPHONE, MUTE
return