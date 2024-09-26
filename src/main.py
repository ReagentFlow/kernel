from datetime import datetime
from time import sleep

from scanner import barcode_scanner
from scales import getting_weight
from constants import KEY, COLLECTION
from button import Button, PinOUT, PinIN
from display.display_i2c import Display
from connection.base import APIConnection


def scanner_check() -> int:
    while True:
        key = barcode_scanner()
        try:
            if api_conn.get_item(key):
                return key
            else:
                display.clear()
                display.display_message("try again")
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
            display.display_message("try again")
            print("Пожалуйста, положите предмет на весы и попробуйте еще раз.")
        sleep(1.5)


def main() -> None:
    display.clear()
    display.display_message("scan")
    print("Отсканируйте вещество.")
    key = scanner_check()
    display.display_message(str(key))
    display.display_message("success")
    sleep(4)
    print("Сканирование успешно. Положите предмет на весы.")
    display.display_message("Put on the scale")
    weight = scales_check()
    display.display_message(str(weight))
    print(f"Вес: {weight} г")

    updated_data = {
        "container_id": key,
        "mass": weight,
    }

    sleep(5)

    try:
        response = api_conn.update_item(key, updated_data)
        display.display_message("data updated")
        print("Данные успешно обновлены.")
    except Exception as e:
        display.display_message("data error")
        print(f"Ошибка при обновлении данных: {e}")


if __name__ == "__main__":

    api_conn = APIConnection("https://www.reagentflow.ru/api/data", "device1")
    display = Display()

    try:
        while True:
            main()
            sleep(3)
    except KeyboardInterrupt:
        print("Программа завершена пользователем.")
    finally:
        display.clear()
        display.close()
