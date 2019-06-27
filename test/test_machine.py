import esp32_machine_emulator.machine as machine
import pytest

@pytest.fixture()
def resetMachine():
    machine.resetExpectationsForTesting()
    print("machine reset")

class TestPinOut:
    
    def test_pinOnSetsValueHigh(self, resetMachine):
        ledPin = machine.Pin(1, machine.Pin.OUT)
        ledPin.on()
        assert ledPin.value() == 1

    def test_pinOffSetsValueLow(self, resetMachine):
        ledPin = machine.Pin(1, machine.Pin.OUT)
        ledPin.off()
        assert ledPin.value() == 0

    def test_pinValueHighSetsValueHigh(self, resetMachine):
        ledPin = machine.Pin(1, machine.Pin.OUT)
        ledPin.value(1)
        assert ledPin.value() == 1

    def test_pinValueLowSetsValueLow(self, resetMachine):
        ledPin = machine.Pin(1, machine.Pin.OUT)
        ledPin.value(0)
        assert ledPin.value() == 0

## TODO: Pin in tests

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
