#!/usr/bin/env python

import time

from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
from grove.grove_relay import GroveRelay

def main():
    # Grove - mini PIR motion sensor connected to port D5
    sensor = GroveMiniPIRMotionSensor(5)

    # Grove - Relay connected to port D16
    relay = GroveRelay(16)

    def on_detect():
        print('motion detected')

        relay.on()
        print('relay on')

        time.sleep(1)

        relay.off()
        print('relay off')

    sensor.on_detect = on_detect

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
