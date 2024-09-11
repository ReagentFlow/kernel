from datetime import datetime
import RPI.GPIO as GPIO
from RPLCD.gpio import CharLCD
from time import sleep

from scanner import barcode_scanner
from scales import getting_weight
from constants import KEY, COLLECTION
from button import Button, PinOUT, PinIN
from display.display_melton import Display
from connection.base import APIConnection




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def scanner_check():
    pass

def scales_check():
    pass


def main():
    pass


if __name__ == "__main__":
    # pin_in = PinIN(40)
    # pin_out = PinOUT(38)
    # button = Button(pin_in, pin_out)

    display = Display()
    display.clear()

    try:
        while True:
            if button.is_pressed():
                main(window)
    except KeyboardInterrupt:
        button.cleanup()
        window.quit()
