from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

from scanner import barcode_scanner
from scales import getting_weight
from constants import KEY, COLLECTION
from button import Button, PinOUT, PinIN
from display.display_melton import Display
from connection.base import APIConnection


def scanner_check() -> int:
    while True:
        key = barcode_scanner()
        try:
            if api_conn.get_item(key):
                return key
            else:
                print("Этого вещества нет в базе данных. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при обращении к базе данных: {e}")
        sleep(1.5)


def scales_check() -> int:
    while True:
        weight = getting_weight()
        if weight > 0:
            return weight
        else:
            print("Пожалуйста, положите предмет на весы и попробуйте еще раз.")
        sleep(1.5)


def main() -> None:
    print("Отсканируйте вещество.")
    key = scanner_check()

    print("Сканирование успешно. Положите предмет на весы.")

    weight = scales_check()
    print(f"Вес: {weight} г")

    updated_data = {
        "container_id": key,
        "mass": weight,
    }

    try:
        response = api_conn.update_item(key, updated_data)
        print("Данные успешно обновлены.")
    except Exception as e:
        print(f"Ошибка при обновлении данных: {e}")


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    api_conn = APIConnection("http://0.0.0.0:8000/data", "device1")
    display = Display()

    try:
        while True:
            main()
            sleep(1)
    except KeyboardInterrupt:
        print("Программа завершена пользователем.")
    finally:
        GPIO.cleanup()
