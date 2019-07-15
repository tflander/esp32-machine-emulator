from resetMachine import *

@pytest.fixture
def outPin():
    machine.resetExpectationsForTesting()
    ledPin = machine.Pin(1, machine.Pin.OUT)
    ledPin.resetExpectationsForTesting()
    return ledPin


class TestPinOut:

    def test_ErrorRaisedWhenGettingValueOfUnitializedPin(self, outPin):
        machine.resetExpectationsForTesting()
        ledPin = machine.Pin(1, machine.Pin.OUT)
        try:
            ledPin.value()
            raise Exception("Expected Exception. None Raised.")
        except Exception as ex:
            assert ex.args[0] == 'Checking Value of Uninitialized OUT Pin.  Set the value before checking.'

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
        assert outPin.triggerValuesForTesting == [0, 1, 1]
