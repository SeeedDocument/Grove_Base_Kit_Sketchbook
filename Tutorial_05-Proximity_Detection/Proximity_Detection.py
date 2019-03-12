#!/usr/bin/env python

import time

from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

def main():
    # Grove - Ultrasonic Ranger connected to port D5
    sensor = GroveUltrasonicRanger(5)

    # Grove - Relay connected to port D16
    relay = GroveRelay(16)

    while True:
        distance = sensor.get_distance()
        print('{} cm'.format(distance))

        if distance < 20:
            relay.on()
            print('relay on')

            time.sleep(1)

            relay.off()
            print('relay off')

            continue

        time.sleep(1)

if __name__ == '__main__':
    main()
