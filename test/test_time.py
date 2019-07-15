import time
from resetMachine import *

class TestTime:

    def test_sleepMs(self, resetMachine):
        time.sleep_ms(1)
        time.sleep_ms(2)
        time.sleep_ms(3)
        assert machine.expectedTimeSleepMs == [1,2,3]

    def test_sleepUs(self, resetMachine):
        time.sleep_us(4)
        time.sleep_us(5)
        time.sleep_us(6)
        assert machine.expectedTimeSleepUs == [4,5,6]