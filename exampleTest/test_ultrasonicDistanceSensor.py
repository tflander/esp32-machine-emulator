import os, sys
sys.path.append(os.path.abspath('.'))

from exampleSrc.ultrasonicDistanceSensorDemo import Hcsr04UltrasonicDistanceSensor

distanceSensor = Hcsr04UltrasonicDistanceSensor(triggerPin = 5, echoPin = 6)

def test_verifyPinAssignments():
    assert distanceSensor.echo.pinForTesting == 6
    assert distanceSensor.trigger.pinForTesting == 5

def test_stabilizeSensor():
    distanceSensor.trigger.resetExpectationsForTesting()
    distanceSensor.stabilizeSensor()
    ## TODO: finish test / code
    # assert distanceSensor.trigger.triggerValuesForTesting == [0,1]
