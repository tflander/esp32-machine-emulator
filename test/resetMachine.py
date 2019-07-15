import esp32_machine_emulator.machine as machine
import pytest

@pytest.fixture()
def resetMachine():
    machine.resetExpectationsForTesting()
