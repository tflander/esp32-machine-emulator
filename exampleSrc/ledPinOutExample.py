import time, sys
import machine

class LedSwitcher:

    def __init__(self, greenLedPin, redLedPin):
        self.greenLed = machine.Pin(greenLedPin, machine.Pin.OUT)
        self.redLed = machine.Pin(redLedPin, machine.Pin.OUT)

    def green(self):
        self.greenLed.on()
        self.redLed.off()

    def red(self):
        self.greenLed.off()
        self.redLed.on()

ledSwitcher = LedSwitcher(greenLedPin = 21, redLedPin = 22)

def demoToAlternateGreenAndRedLeds():
    while True:
        ledSwitcher.green()
        time.sleep_ms(300)
        ledSwitcher.red()
        time.sleep_ms(300)
