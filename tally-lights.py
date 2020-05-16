#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from gpiozero import LED

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, events  # noqa: E402

host = "YOUR-HOST" # Replace with IP or hostname of you OBS computer
port = 4444 # 4444 is the default port, you can change it in obs-websocket on your computer
password = "YOUR-OBS-WEBSOCKET-PASSWORD" # Password set in obs-websocket

light = LED(17) # 17 is the GPIO PIN id

def on_switch(message):
    scenename = message.getSceneName()

    scenes = ["Scene 1", "Camera 1", "PiP ProPresenter Cam1", "PiP Camera 1"] # Name of all OBS scenes to trigger light

    if(scenename in scenes):
        light.on()

    else:
        # SET LIGHTS OFF
        light.off()



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