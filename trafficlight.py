#!/usr/bin/env python3
"""
trafficlight.py - build a traffic light with Raspberry Pi (Zero) and Pimoroni Blinkt!

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by "Christian Becker <mail@christianbecker.name>"
"""

try:
    import time
    import blinkt
except ImportError:
    exit("This script requires some modules...\nInstall with: sudo pip3 install blinkt")



def red_light():
    """set the red light on top of blinkt!"""
    blinkt.set_pixel(7, 255, 0, 0)
    blinkt.set_pixel(6, 255, 0, 0)
    blinkt.show()

def yellow_light():
    """set the yellow light in the middle of blinkt!"""
    blinkt.set_pixel(4, 255, 100, 0)
    blinkt.set_pixel(3, 255, 100, 0)
    blinkt.show()

def green_light():
    """set the green light at the bottom of blinkt!"""
    blinkt.set_pixel(1, 0, 255, 0)
    blinkt.set_pixel(0, 0, 255, 0)
    blinkt.show()


def main():
    """start the traffic light"""
    blinkt.set_clear_on_exit()
    blinkt.set_brightness(0.4)

    cycle_time = 60   # time from "green to green" - should be between 45 and 120 seconds
    yellow_time = 3   # 3s = 50 km/h // 4s = 60 km/h // 5s = 70km/h
    #
    red_yellow_time = 2   # should always be two seconds
    red_green_time = (cycle_time - yellow_time - red_yellow_time) / 2   # generated

    while True:
        blinkt.clear()

        # RED
        red_light()
        time.sleep(red_green_time)

        # RED YELLOW
        yellow_light()
        time.sleep(red_yellow_time)

        blinkt.clear()

        # GREEN
        green_light()
        time.sleep(red_green_time)

        blinkt.clear()

        # YELLOW
        yellow_light()
        time.sleep(yellow_time)


if __name__ == "__main__":
    # execute only if run as a script
    try:
        main()
    except KeyboardInterrupt:
        # if the user presses control-c
        print('\ninterrupted...traffic light stopped!\n')

