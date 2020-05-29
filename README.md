# obs-tally-lights
 Raspberry Pi Tally Light script for OBS

## Requirements

### Hardware
* 1 Raspberry Pi with GPIO pins and network access
* 1 Breadboard
* 1 LED
* 1 resistor (330Ω)
* 2 jumper cables

*Everything needed excluding the RPi is included in the [CamJam EduKit](https://thepihut.com/products/camjam-edukit) from https://thepihut.com*

### Software
* [gpiozero](https://gpiozero.readthedocs.io/en/stable/)
* [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py)

*[obs-websocket](https://github.com/Palakis/obs-websocket/) is also required to be installed on the machine running OBS*

## Setup
* Install the required packages on you RPi
* Install [obs-websocket](https://github.com/Palakis/obs-websocket/) on your computer running OBS and set password
* Create a python file on you RPi, with one of the to .py files from this repository
  * tally-lights.py is used with multiple raspberry pis, to turn on and off a single light for each pi depending on what scene is active
  * tally-lights-single.py is used whith only 1 raspberry pi, to turn on different lights on the same board for different scenes
* Edit the variables to match your setup
  * See comments in file. *host*, *port*, *password* and *scenes*
* Add the file to startup for a more convenient workflow
* Connect the LED to your RPi. From RPi ground, via resistor to LED to RPi PIN 17 (or, if you are using tally-lights-single.py, to numbers set on line 19 and below)

**Read [here](https://docs.google.com/document/d/1nQFsDAIhL4BkFzd1uDLOn3cNSB8JWlAI0Og3YWVYy6E) for detailed instructions.**

**Note** that this is my first ever python project, so I'll happily accept improvements.
