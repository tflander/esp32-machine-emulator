import time
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

class Hcsr04UltrasonicDistanceSensor:
    
    def __init__(self, triggerPin = 5, echoPin = 6):
        self.trigger = machine.Pin(triggerPin, machine.Pin.OUT)
        self.echo = machine.Pin(echoPin, machine.Pin.IN)

    def distanceCm(self):
        pulse_time = self.sample()
        return int(round((pulse_time / 2) / 29.1))

    def sample(self):
        self.stabilizeSensor()
        self.sendTriggerSignal()
        try:
            return machine.time_pulse_us(self.echo, 1, 30000)
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError("out of range")
            raise ex

    def stabilizeSensor(self):
        self.trigger.value(0)
        time.sleep_us(5)

    def sendTriggerSignal(self):
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
