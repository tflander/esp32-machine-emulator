import time
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

class Hcsr04UltrasonicDistanceSensor:
    
    def __init__(self, triggerPin = 5, echoPin = 6):
        self.trigger = machine.Pin(triggerPin, machine.Pin.OUT)
        self.echo = machine.Pin(echoPin, machine.Pin.IN)

    def stabilizeSensor(self):
        pass
