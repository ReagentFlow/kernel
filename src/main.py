from time import sleep
import threading

from scanner import barcode_scanner
from scales import getting_weight
from constants import KEY, COLLECTION
from display.display_i2c import Display
from connection.base import APIConnection


class TimerThread(threading.Thread):
    def __init__(self, duration=7, restart_callback=None):
        super().__init__()
        self.duration = duration
        self.restart_callback = restart_callback
        self._stop_event = threading.Event()
        self.is_running = True

    def run(self):
        sleep(self.duration)
        if not self._stop_event.is_set():
            print("Таймер истек. Перезапуск функции main...")
            if self.restart_callback:
                self.restart_callback()
        self.is_running = False

    def stop(self):
        self._stop_event.set()
        self.is_running = False


def scanner_check() -> int:
    while True:
        key = barcode_scanner()
        try:
            if api_conn.get_item(key):
                return key
            else:
                display.clear()
                display.display_message("TRY AGAIN")
                print("Этого вещества нет в базе данных. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при обращении к базе данных: {e}")
        sleep(1.5)


def scales_check(restart_callback):
    timer = TimerThread(restart_callback=restart_callback)
    timer.start()

    while True:
        weight = getting_weight()
        if weight > 0:
            timer.stop()
            timer.join()
            return weight
        else:
            timer.stop()
            timer.join()
            display.display_message("TRY AGAIN")
            print("Пожалуйста, положите предмет на весы и попробуйте еще раз.")
        sleep(1.5)


def main() -> None:
    display.clear()
    display.display_message("SCAN")
    print("Отсканируйте вещество.")

    key = scanner_check()
    display.display_message(str(key))
    print(f"Штрих-код {key}")
    sleep(2)

    display.display_message("PUT ON THE SCALE")
    print("Сканирование успешно. Положите предмет на весы.")
    sleep(2)

    weight = scales_check(restart_callback=main)  # Передаем main как колбэк
    if weight is None:
        return

    display.display_message(f"{weight} grams")
    print(f"Вес: {weight} г")

    updated_data = {
        "container_id": key,
        "mass": weight,
    }

    try:
        response = api_conn.update_item(key, updated_data)
        display.display_message("DATA UPDATED")
        print("Данные успешно обновлены.")
    except Exception as e:
        display.display_message("DATA ERROR")
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
        # Завершите таймер, если он активен
        if 'timer' in locals():
            timer.stop()
            timer.join()
        display.clear()
        display.close()
