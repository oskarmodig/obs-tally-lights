#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from gpiozero import LED

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, events  # noqa: E402

host = "YOUR-HOST"
port = 4444
password = "YOUR-OBS-WEBSOCKET-PASSWORD"

red = LED(17)
green = LED(18)

def on_switch(message):
    scenename = message.getSceneName()

    camera1 = ["Scene 1", "Camera 1", "PiP ProPresenter Cam1", "PiP Camera 1"] # Name of all OBS scenes to trigger light 1
    camera2 = ["Scene 2", "Camera 2", "PiP ProPresenter Cam2", "PiP Camera 2"] # Name of all OBS scenes to trigger light 2

    if(scenename in camera1):
        # SET LIGHT 1
        green.off()
        red.on()

    elif(scenename in camera2):
        # SET LIGHT 2
        red.off()
        green.on()

    else:
        # SET LIGHTS OFF
        print("Lights off")
        green.off()
        red.off()



ws = obsws(host, port, password)
ws.register(on_switch, events.SwitchScenes)

connected = False

while not connected:
    try:
        ws.connect()
        connected = True
    except KeyboardInterrupt:
        exit()
    except:
        print("Retry connect")

try:
    while True: # infinite loop to prevent script end. Someone who actually knows python is very welcome to write a cleaner way
        time.sleep(42)

except KeyboardInterrupt:
    pass

ws.disconnect();