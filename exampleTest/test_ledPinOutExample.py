from exampleSrc.ledPinOutExample import LedSwitcher

ledSwitcher = LedSwitcher(greenLedPin=1, redLedPin=2)

def test_pinAssignments():
    assert(ledSwitcher.greenLed.pinForTesting == 1)
    assert(ledSwitcher.redLed.pinForTesting == 2)

def test_green():
        ledSwitcher.green()
        assert ledSwitcher.greenLed.value() == 1
        assert ledSwitcher.redLed.value() == 0

def test_red():
        ledSwitcher.red()
        assert ledSwitcher.greenLed.value() == 0
        assert ledSwitcher.redLed.value() == 1

