from datetime import datetime
from time import sleep
import RPI.GPIO as GPIO
from RPLCD.gpio import CharLCD

from scanner import barcode_scanner
from scales import getting_weight
from constants import KEY, COLLECTION
from button import Button, PinOUT, PinIN
from display.display_melton import Display
from connection.base import APIConnection



def scanner_check() -> int:
    key = barcode_scanner()
    return key


def scales_check() -> int:
    weight = getting_weight()
    if weight > 0:
        return weight
    else:
        scales_check()


def main() -> None:
    #отсканируйте штрих-код
    key = scanner_check()
    print(key)
    #успешно
    #положите предмет на весы
    weight = scales_check()
    print(weight)
    #{масса}
    #создание/обновление data
    #задержка


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass
