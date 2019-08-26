import network
import pytest


@pytest.fixture
def sta_if():
    return network.WLAN(network.STA_IF)


def test_activate_station_interface(sta_if):
    sta_if.active(True)
    assert sta_if.active_for_testing


def test_deactivate_station_interface(sta_if):
    sta_if.active(False)
    assert not sta_if.active_for_testing


def test_connect(sta_if):
    sta_if.connect(ssid="foo", password="bar")
    assert sta_if.isconnected()
