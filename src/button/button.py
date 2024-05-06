import RPi.GPIO as GPIO
from typing import NewType

PinIN = NewType('PinIN', int)
PinOUT = NewType('PinOUT', int)

class Button:
    def __init__(self, pin_in: PinIN, pin_out: PinOUT) -> None:
        self.pin_in = pin_in
        self.pin_out = pin_out
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_in, GPIO.IN)
        GPIO.setup(self.pin_out, GPIO.OUT)

    def is_pressed(self) -> bool:
        return GPIO.input(self.pin_in) == 0

    @staticmethod
    def cleanup() -> None:
        GPIO.cleanup()
