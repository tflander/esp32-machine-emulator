import time
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine
    from support.demoSupport import *

class Hcsr04:
    
    def __init__(self, triggerPin = 5, echoPin = 6):
        self.trigger = machine.Pin(triggerPin, machine.Pin.OUT)
        self.echo = machine.Pin(echoPin, machine.Pin.IN)

    def stabilizeSensor(self):
        pass

if isOffChipForTesting():

    class TestHcsr04:

        distanceSensor = Hcsr04(triggerPin = 5, echoPin = 6)

        def test_verifyPinAssignments(self):
            assert self.distanceSensor.echo.pinForTesting == 6
            assert self.distanceSensor.trigger.pinForTesting == 5

        def test_stabilizeSensor(self):
            self.distanceSensor.trigger.resetExpectationsForTesting()
            self.distanceSensor.stabilizeSensor()
            assert self.distanceSensor.trigger.triggerValuesForTesting == [0,1]

    # Fake test runner for demo
    tests = TestHcsr04()
    tests.test_verifyPinAssignments()
    tests.test_stabilizeSensor()
    print("tests complete.")
