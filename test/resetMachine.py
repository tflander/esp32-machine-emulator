import machine
import pytest

@pytest.fixture()
def resetMachine():
    machine.resetExpectationsForTesting()
