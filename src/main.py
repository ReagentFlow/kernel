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


def scanner_check() -> int | None:
    while True:
        key = barcode_scanner()
        response = api_conn.get_item(key)
        if response:
            formula = response.get("formula", "No formula")
            display.clear()
            display.display_message(formula)
            print(f"Формула вещества: {formula}")
            return key
        else:
            display.clear()
            display.display_message("TRY AGAIN")
            print("Этого вещества нет в базе данных. Попробуйте еще раз.")


def scales_check(restart_callback, timer) -> int | None:
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
            display.clear()
            display.display_message("TRY AGAIN")
            print("Пожалуйста, положите предмет на весы и попробуйте еще раз.")
        sleep(1.5)


def main() -> None:
    display.clear()
    display.display_message("SCAN")
    print("Отсканируйте вещество.")

    if not (key := scanner_check()):
        return None
    sleep(2)

    display.clear()
    display.display_message("PUT ON THE SCALE")
    print("Сканирование успешно. Положите предмет на весы.")

    timer = TimerThread(restart_callback=main)
    weight = scales_check(restart_callback=main, timer=timer)  # Передаем main как колбэк
    if weight is None:
        return None

    display.clear()
    display.display_message(f"{weight} grams")
    print(f"Вес: {weight} г")
    sleep(2)

    updated_data = {
        "container_id": key,
        "mass": weight,
    }

    try:
        response = api_conn.update_item(key, updated_data)
        display.clear()
        display.display_message("DATA UPDATED")
        print("Данные успешно обновлены.")
        sleep(2)
    except Exception as e:
        display.clear()
        display.display_message("DATA ERROR")
        print(f"Ошибка при обновлении данных: {e}")


if __name__ == "__main__":
    api_conn = APIConnection("https://www.reagentflow.ru/api/data", "device1")
    display = Display()

    try:
        while True:
            main()
            display.clear()
            sleep(1.5)
    except KeyboardInterrupt:
        print("Программа завершена пользователем.")
    finally:
        # Завершите таймер, если он активен
        if 'timer' in locals() and timer.is_running:
            timer.stop()
            timer.join()
        display.clear()
        display.close()
