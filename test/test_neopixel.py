from resetMachine import *
import esp32_machine_emulator.neopixel as neopixel
import pytest

@pytest.fixture()
def tenPixelStrand():
    pin = machine.Pin(5)
    return neopixel.NeoPixel(pin, n=10)


black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


class TestNeoPixel:

    pin = machine.Pin(5)

    def test_canSetPixelColor(self, resetMachine, tenPixelStrand):
        tenPixelStrand[0] = green
        tenPixelStrand[1] = red
        assert tenPixelStrand[0] == green
        assert tenPixelStrand[1] == red
        assert len(tenPixelStrand.writesForTesting) == 0

    def test_writeUpdatesPixels(self, resetMachine, tenPixelStrand):
        tenPixelStrand[0] = green
        tenPixelStrand[1] = red
        tenPixelStrand.write()
        assert len(tenPixelStrand.writesForTesting) == 1
        writtenStrand = tenPixelStrand.writesForTesting[0]
        assert writtenStrand[0] == green
        assert writtenStrand[1] == red
        assert writtenStrand.timeFromFirstWrite == 0

    def test_initWithDefaults(self, resetMachine):
        np = neopixel.NeoPixel(self.pin, n=10)
        assert np.pin == self.pin
        assert np.n == 10
        assert np.bpp == 3
        assert np.timing == 1

    def test_initWithOverrides(self, resetMachine):
        np = neopixel.NeoPixel(self.pin, n=10, bpp=4, timing=2)
        assert np.bpp == 4
        assert np.timing == 2
