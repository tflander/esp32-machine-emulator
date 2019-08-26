import time

import machine


class LedSwitcher:

    def __init__(self, green_led_pin, red_led_pin):
        self.greenLed = machine.Pin(green_led_pin, machine.Pin.OUT)
        self.redLed = machine.Pin(red_led_pin, machine.Pin.OUT)

    def green(self):
        self.greenLed.on()
        self.redLed.off()

    def red(self):
        self.greenLed.off()
        self.redLed.on()


ledSwitcher = LedSwitcher(green_led_pin=21, red_led_pin=22)


def demoToAlternateGreenAndRedLeds():
    while True:
        ledSwitcher.green()
        time.sleep_ms(300)
        ledSwitcher.red()
        time.sleep_ms(300)
