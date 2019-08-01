
ESP32 Machine Emulator
======================


The purpose of this package is to enable you to test-drive (TDD) your
MicroPython code in an IDE running on your computer.  It seems a lot
of people are test-driving python, but not many are test-driving MicroPython.
That's understandable, since many MicroPython projects are simple, and
emulating real hardware in a test environment is difficult.

The typical approach to emulating hardware is to replicate the hardware
programming interface (the API).  As of this writing, this library emulates
a very small slice of the ESP32 API.  I don't know if the library will mature.
Hopefully I'll either flesh it out, someone else will take over, or a
replacement will emerge.

If you are unfamiliar with the benefits of TDD or test-driving python, I
encourage you to take some time to Google and learn.  I prefer the pytest
library over the unittest library that comes with python3, but you are free
to test as you choose.

Getting Started
===============

Take a look at the examples folder in the GitHub repository.  Like I said,
as of this writing, the library emulates a very small slice of the API,
so if you don't see an example for something you want to do, the feature
is not available.  Feel free to contact me or fork the repo and send me
a pull request for the feature.

Here is the github repo for this project:
https://github.com/tflander/esp32-machine-emulator

Here is the project on PyPi:
https://pypi.org/project/esp32-machine-emulator

Note that the examples are only in the GitHub repo, and are not part of the
PyPi distribution.

Supported Features
==================

- Emulating sending a GPIO digital out signal, and verifying the signal value.
- Extending the time library to support sleep_ns() and sleep_ms()
- Emulating the read pulse value of an input pin, such as that received by
  the echo pin of an HCSR04 Ultrasonic Distance Sensor.
- Full emulation of HCSR04 Ultrasonic Distance Sensor in examples
