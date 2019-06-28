import time, sys
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

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

if sys.platform == 'darwin':
    def test_pinAssignments():
        assert(ledSwitcher.greenLed.pinForTesting == 21)
        assert(ledSwitcher.redLed.pinForTesting == 22)

    def test_green():
            ledSwitcher.green()
            assert ledSwitcher.greenLed.value() == 1
            assert ledSwitcher.redLed.value() == 0

    def test_red():
            ledSwitcher.red()
            assert ledSwitcher.greenLed.value() == 0
            assert ledSwitcher.redLed.value() == 1

    ## Normally you would use a test runner, but let's run the tests manually for fun
    print('Testing Pin Assignments...')
    test_pinAssignments()
    print('Testing green...')
    test_green()    
    print('Testing red...')
    test_red()
    print("all tests passed")
