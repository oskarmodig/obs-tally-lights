# https://gpiozero.readthedocs.io/en/stable/recipes.html#shutdown-button

from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(2, hold_time=2)
shutdown_btn.when_held = shutdown

pause()