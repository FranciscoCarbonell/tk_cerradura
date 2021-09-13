from threading import Thread
from evdev import InputDevice
from select import select
import logging

logger = logging.getLogger(__name__)

try:
    import RPi.GPIO as GPIO
except RuntimeError as error:
    print(error)
    from mock import GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)


class Rfid(Thread):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.dev = InputDevice('/dev/input/event0')
        self.running = True
        self.buffer = []
        print(app)

    def run(self):
        while self.running:
            self.read_events()

    def stop(self):
        self.running = False
    
    def read_events(self):
        r, x, z = select([self.dev], [], [])
        for event in self.dev.read():
            if event.type==1 and event.value==1 and event.code == 28:
                # Key code 28 (Enter)
                # 4804804 (last 7 character)


                logging.warning('push enter')
                logging.warning(''.join(map(str, self.buffer)))
                self.buffer = []
            else:
                self.buffer.append(event.code)
