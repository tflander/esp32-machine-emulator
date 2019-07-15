import time

class NeoPixel:

    def __init__(self, pin, n, bpp=3, timing=1):
        self.pin = pin
        self.n = n
        self.bpp = bpp
        self.timing = timing
        self.writesForTesting = []
        self.firstWriteTime = None
        self.currentPixelColors = StrandHistoryForTesting(n, bpp)

    def __setitem__(self, index, val):
        self.currentPixelColors[index] = val

    def __getitem__(self, index):
        return self.currentPixelColors[index]

    def write(self):
        if self.firstWriteTime is None:
            self.firstWriteTime = time.gmtime()
            self.currentPixelColors.timeFromFirstWrite = 0
        else:
            self.currentPixelColors.timeFromFirstWrite = time.gmtime() - self.firstWriteTime

        self.writesForTesting.append(self.currentPixelColors)


class StrandHistoryForTesting:

    timeFromFirstWrite = 0

    def __init__(self, numPixels, bytesPerPixel):
        self.numPixels = numPixels
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
