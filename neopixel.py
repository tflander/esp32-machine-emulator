import copy
import time


def _perfTimeMs():
    return round(time.perf_counter() * 1000)


class NeoPixel:

    def __init__(self, pin, n, bpp=3, timing=1):
        self.pin = pin
        self.n = n
        self.bpp = bpp
        self.timing = timing
        self.writesForTesting = []
        self.firstWriteTimeForTesting = None
        self.currentPixelColors = StrandHistoryForTesting(n, bpp)

    def fill(self, color):
        for i in range(self.n):
            self[i] = color

    def __setitem__(self, index, val):
        self.currentPixelColors[index] = val

    def __getitem__(self, index):
        return self.currentPixelColors[index]

    def write(self):
        if self.firstWriteTimeForTesting is None:
            self.firstWriteTimeForTesting = _perfTimeMs()
            self.currentPixelColors.timeFromFirstWrite = 0
        else:
            self.currentPixelColors.timeFromFirstWrite = _perfTimeMs() - self.firstWriteTimeForTesting

        self.writesForTesting.append(copy.deepcopy(self.currentPixelColors))


class StrandHistoryForTesting:
    timeFromFirstWrite = 0

    def __init__(self, numPixels, bytesPerPixel):
        self.n = numPixels
        self.bytesPerPixel = bytesPerPixel
        if bytesPerPixel == 3:
            self.defaultColor = (0, 0, 0)
        elif bytesPerPixel == 4:
            self.defaultColor = (0, 0, 0, 0)
        else:
            raise OSError
        self.colorList = [self.defaultColor] * numPixels

    def __setitem__(self, index, val):
        self.colorList[index] = val

    def __getitem__(self, index):
        return self.colorList[index]
