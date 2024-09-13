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
    global is_scanner
    key = barcode_scanner()
    if key:
        is_scanner = True
        return key
    else:
        is_scanner = False


def scales_check():
    global is_scale
    weight = getting_weight()
    if weight:
        is_scale = True
        return weight
    else:
        is_scale = False


def main():
    global is_scanner
    global is_scale

    key = 0
    while not is_scanner:
        key = scanner_check()
        print("отсканируйте еще раз")
    print(key)
    print("положите на весы")

    weight = ""
    while not is_scale:
        scales_check()
        print("положите еще раз на весы")
    print(weight)
    print("данные занесены в базу")





is_scanner = False
is_scale = False


if __name__ == "__main__":
    # pin_in = PinIN(40)
    # pin_out = PinOUT(38)
    # button = Button(pin_in, pin_out)

    display = Display()
    display.clear()

    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass
