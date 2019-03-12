#!/usr/bin/env python

import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer

from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.display.jhd1802 import JHD1802

def main():
    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    # Grove - Moisture Sensor connected to port A0
    sensor = GroveMoistureSensor(0)

    # Grove - Buzzer connected to port PWM
    buzzer = upmBuzzer.Buzzer(getGpioLookup('GPIO12'))

    while True:
        mois = sensor.moisture
        if 0 <= mois and mois < 300:
            level = 'dry'
        elif 300 <= mois and mois < 600:
            level = 'moist'
        else:
            level = 'wet'
            buzzer.playSound(upmBuzzer.BUZZER_DO, 200000)

        print('moisture: {}, {}'.format(mois, level))

        lcd.setCursor(0, 0)
        lcd.write('moisture: {0:>6}'.format(mois))

        lcd.setCursor(1, 0)
        lcd.write('{0:>16}'.format(level))

        time.sleep(1)

if __name__ == '__main__':
    main()
