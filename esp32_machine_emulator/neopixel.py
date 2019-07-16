import time, copy

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
            self.firstWriteTimeForTesting = self._perfTimeMs()
            self.currentPixelColors.timeFromFirstWrite = 0
        else:
            self.currentPixelColors.timeFromFirstWrite = self._perfTimeMs() - self.firstWriteTimeForTesting

        self.writesForTesting.append(copy.deepcopy(self.currentPixelColors))

    def _perfTimeMs(self):
        return round(time.perf_counter() * 1000)

class StrandHistoryForTesting:

    timeFromFirstWrite = 0

    def __init__(self, numPixels, bytesPerPixel):
        self.n = numPixels
        self.bytesPerPixel = bytesPerPixel
        self.buf = bytearray(numPixels * bytesPerPixel)

    def __setitem__(self, index, val):
        offset = index * self.bytesPerPixel
        for i in range(self.bytesPerPixel):
            self.buf[offset + i] = val[i]

    def __getitem__(self, index):
        offset = index * self.bytesPerPixel
        return tuple(self.buf[offset + i]
                     for i in range(self.bytesPerPixel))
