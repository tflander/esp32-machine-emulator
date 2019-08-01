"""
The purpose of this module is to emulate the machine module of the ESP32 chip.  The primary reason to 
emulate the chip is for test-driving code (TDD).

Verified Firmware version: esp32-20190610-v1.11-37-g62f004ba4

Portions also tested with esp8266-20190529-v1.11
"""
import time
EMULATION_MODE = True

__author__ = 'Todd Flanders https://github.com/tflander/Esp32IotKata'

expectedPulseTimeForTesting = 0
expectedPulseTimeErrorForTesting = None
expectedTimeSleepMs = []
expectedTimeSleepUs = []

def resetExpectationsForTesting():
    global expectedPulseTimeForTesting
    global expectedPulseTimeErrorForTesting
    global expectedTimeSleepMs
    global expectedTimeSleepUs

    expectedPulseTimeForTesting = 0
    expectedPulseTimeErrorForTesting = None
    expectedTimeSleepMs = []
    expectedTimeSleepUs = []

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
    expectedTimeSleepUs.append(delayUs)

def sleep_msForMonkeyPatching(delayMs):
    time.sleep(delayMs / 1000)
    expectedTimeSleepMs.append(delayMs)

time.sleep_us = sleep_usForMonkeyPatching
time.sleep_ms = sleep_msForMonkeyPatching

class Pin:
    IN = "in"
    OUT = "out"

    triggerValuesForTesting = []

    def resetExpectationsForTesting(self):
        self.currentStateForTesting = None
        self.triggerValuesForTesting = []

    def __init__(self, pin, mode=OUT, pull=None):
        self.pinForTesting = pin
        self.resetExpectationsForTesting()

    def on(self):
        self.currentStateForTesting = 1
        self.triggerValuesForTesting.append(self.currentStateForTesting)

    def off(self):
        self.currentStateForTesting = 0
        self.triggerValuesForTesting.append(self.currentStateForTesting)

    def value(self, newValue=None):
        if newValue == 0:
            self.off()
        elif newValue == 1:
            self.on()
        if(self.currentStateForTesting == None):
            raise Exception("Checking Value of Uninitialized OUT Pin.  Set the value before checking.")
        return self.currentStateForTesting

