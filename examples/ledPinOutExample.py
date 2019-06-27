import time
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

greenLed = machine.Pin(21, machine.Pin.OUT)
redLed = machine.Pin(22, machine.Pin.OUT)

# Note that the machine emulator is monkeypatching the time library.  Python3 expects
# the sleep() function to take a float, so for a 300ms sleep, you would code
# >>> import time
# >>> time.sleep_ms(300)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# AttributeError: module 'time' has no attribute 'sleep_ms'
# >>> import esp32_machine_emulator.machine as machine
# >>> time.sleep_ms(300)

def demo():
    while True:
        greenLed.on()
        redLed.off()
        time.sleep_ms(300)
        greenLed.off()
        redLed.on()
        time.sleep_ms(300)