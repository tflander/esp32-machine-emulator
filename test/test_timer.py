import machine
import pytest


@pytest.fixture
def timer():
    return machine.Timer(0)


def test_timer_does_not_run_on_construction(timer):
    assert not timer.is_running_for_testing


def test_timer_runs_on_init(timer):
    timer.init(period=1000)
    assert timer.is_running_for_testing

