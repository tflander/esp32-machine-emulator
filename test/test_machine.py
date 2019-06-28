import time
import esp32_machine_emulator.machine as machine
import pytest

@pytest.fixture()
def resetMachine():
    machine.resetExpectationsForTesting()
    print("machine reset")

@pytest.fixture
def outPin():
    machine.resetExpectationsForTesting()
    ledPin = machine.Pin(1, machine.Pin.OUT)
    ledPin.resetExpectationsForTesting()
    return ledPin

class TestPinOut:
    
    def test_pinOnSetsValueHigh(self, outPin):
        outPin.on()
        assert outPin.value() == 1

    def test_pinOffSetsValueLow(self, outPin):
        outPin.off()
        assert outPin.value() == 0

    def test_pinValueHighSetsValueHigh(self, outPin):
        outPin.value(1)
        assert outPin.value() == 1

    def test_pinValueLowSetsValueLow(self, outPin):
        outPin.value(0)
        assert outPin.value() == 0

    def test_supportsCollectingMultiplePinOutValues(self, outPin):
        outPin.value(0)
        outPin.value(1)
        outPin.value(1)
        assert outPin.triggerValuesForTesting == [0,1,1]

class TestPulse:
    
    def test_returnsExpectedPulse(self, resetMachine):
        machine.expectedPulseTimeForTesting = 123
        assert machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 123

    def test_returnsExpectedPulseTimeError(self, resetMachine):
        machine.expectedPulseTimeErrorForTesting = OSError('error for testing')

        try:
            machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000)
            raise Exception("Expected error, none raised")
        except OSError as ex:
            assert(ex.args[0] == 'error for testing')

    def test_supportsMultipleExpectedPulseValues(self, resetMachine):
        machine.expectedPulseTimeForTesting = [123, 456, 789]
        assert machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 123
        assert machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 456
        assert machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 789

    def test_handlesAskingForMoreValuesThanGiven(self, resetMachine):
        machine.expectedPulseTimeForTesting = [123, 456, 789]

        while len(machine.expectedPulseTimeForTesting) > 0:
            machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000)

        try:
            machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000)
            raise Exception("Expected error, none raised")
        except Exception as ex:
            assert ex.args[0] == "unexpected call to time_pulse_us on empty expectation list"

    def test_supportsErrorInExpectedPulseValues(self, resetMachine):
        machine.expectedPulseTimeForTesting = [123, OSError('error for testing'), 789]
        assert machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 123

        try:
            machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 456
            raise Exception("Expected error, none raised")
        except OSError as ex:
            assert(ex.args[0] == 'error for testing')

        assert machine.time_pulse_us(pin=1, pulse_level=1, timeout_us=1000) == 789

class TestTime:

    def test_sleepMs(self, resetMachine):
        time.sleep_ms(1)
        time.sleep_ms(2)
        time.sleep_ms(3)
        assert machine.expectedTimeSleepMs == [1,2,3]        

    def test_sleepUs(self, resetMachine):
        time.sleep_us(4)
        time.sleep_us(5)
        time.sleep_us(6)
        assert machine.expectedTimeSleepUs == [4,5,6]                