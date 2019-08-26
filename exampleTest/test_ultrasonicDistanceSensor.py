from exampleSrc.ultrasonicDistanceSensorDemo import Hcsr04UltrasonicDistanceSensor
import pytest
import machine

expectedTriggerStabilizationValues = [0]
expectedTriggerSignalValues = [1, 0]


@pytest.fixture
def distanceSensor():
    distanceSensor = Hcsr04UltrasonicDistanceSensor(triggerPin=5, echoPin=6)
    machine.resetExpectationsForTesting()
    distanceSensor.trigger.resetExpectationsForTesting()
    return distanceSensor


def test_verifyPinAssignments(distanceSensor):
    assert distanceSensor.echo.pinForTesting == 6
    assert distanceSensor.trigger.pinForTesting == 5


def test_distanceCm(distanceSensor):
    machine.expectedPulseTimeForTesting = 123
    assert distanceSensor.distanceCm() == 2


def test_distanceCmExceptionOutOfRange(distanceSensor):
    machine.expectedPulseTimeErrorForTesting = OSError(110)
    try:
        distanceSensor.distanceCm()
        assert False, "expected exception to be raised"
    except OSError as ex:
        assert ex.args[0] == "out of range"


def test_distanceCmUnexpectedException(distanceSensor):
    machine.expectedPulseTimeErrorForTesting = OSError('Unexpected Exception')
    try:
        distanceSensor.distanceCm()
        assert False, "expected exception to be raised"
    except OSError as ex:
        assert ex.args[0] == "Unexpected Exception"


def test_sampleSendsExpectedTriggerSignals(distanceSensor):
    distanceSensor.sample()
    expectedTriggerSignals = expectedTriggerStabilizationValues + expectedTriggerSignalValues
    assert distanceSensor.trigger.triggerValuesForTesting == expectedTriggerSignals


def test_sampleReturnsExpectedEchoValue(distanceSensor):
    machine.expectedPulseTimeForTesting = 123
    assert distanceSensor.sample() == machine.expectedPulseTimeForTesting


def test_stabilizeSensorSetsTriggerLow(distanceSensor):
    distanceSensor.stabilizeSensor()
    assert distanceSensor.trigger.triggerValuesForTesting == expectedTriggerStabilizationValues


def test_stabilizeSensorExecutesDelay(distanceSensor):
    distanceSensor.stabilizeSensor()
    assert machine.expectedTimeSleepUs == [5]


def test_sendTriggerSignalSetsTriggerHighThenLow(distanceSensor):
    distanceSensor.sendTriggerSignal()
    assert distanceSensor.trigger.triggerValuesForTesting == expectedTriggerSignalValues


def test_sendTriggerSignalExecutesDelay(distanceSensor):
    distanceSensor.sendTriggerSignal()
    assert machine.expectedTimeSleepUs == [10]

## TODO: test pulse timeout value
