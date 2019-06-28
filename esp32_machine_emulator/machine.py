"""
The purpose of this module is to emulate the machine module of the ESP32 chip.  The primary reason to 
emulate the chip is for test-driving code (TDD).

Firmware version: esp32-20190610-v1.11-37-g62f004ba4
"""
import time
EMULATION_MODE = True

__version__ = '0.0.0'
__author__ = 'Todd Flanders https://github.com/tflander/Esp32IotKata'
__license__ = "Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0"

expectedPulseTimeForTesting = 0
expectedPulseTimeErrorForTesting = None

def resetExpectationsForTesting():
    global expectedPulseTimeForTesting, expectedPulseTimeErrorForTesting
    expectedPulseTimeForTesting = 0
    expectedPulseTimeErrorForTesting = None

def time_pulse_us(pin, pulse_level, timeout_us):
    global expectedPulseTimeErrorForTesting
    if expectedPulseTimeErrorForTesting is not None:
        raise expectedPulseTimeErrorForTesting # pylint: disable=raising-bad-type

    try:
        pulseTime = expectedPulseTimeForTesting.pop(0)
    except:
        pulseTime = expectedPulseTimeForTesting

    if type(pulseTime) == int:
        return pulseTime
    else:
        if pulseTime == []:
            raise Exception("unexpected call to time_pulse_us on empty expectation list")
        raise pulseTime

def sleep_usForMonkeyPatching(delayUs):
    time.sleep(delayUs / 1000000)

def sleep_msForMonkeyPatching(delayMs):
    time.sleep(delayMs / 1000)

time.sleep_us = sleep_usForMonkeyPatching
time.sleep_ms = sleep_msForMonkeyPatching

class Pin:
    IN = "in"
    OUT = "out"

    def resetExpectationsForTesting(self):
        self.pinForTesting = None
        self.currentStateForTesting = None

    def __init__(self, pin, mode=OUT, pull=None):
        self.pinForTesting = pin

    def on(self):
        self.currentStateForTesting = 1

    def off(self):
        self.currentStateForTesting = 0

    def value(self, newValue=None):
        if newValue == 0:
            self.off()
        elif newValue == 1:
            self.on()
        return self.currentStateForTesting

