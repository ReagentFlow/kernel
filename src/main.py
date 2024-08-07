from datetime import datetime

from scanner import barcode_scanner
from scales import getting_weight
from fire_db import FireDataBase
from models import Container, ContainerData
from constants import KEY, COLLECTION
from button import Button, PinOUT, PinIN
from display import MainWindow


def _updating(key: int, weight: int) -> None:
    data = ContainerData(name=str(key), weight=weight, barcode_id=key,
                         container_id=0, density=0, date=datetime.now())
    container = Container(key=key, data=data)
    database.update(COLLECTION, container)


def _creating(key: int, weight: int) -> None:
    container_id = len(database.list(collection=COLLECTION)) + 1
    data = ContainerData(name=str(key), weight=weight, barcode_id=key,
                         container_id=container_id, density=0, date=datetime.now())
    container = Container(key=key, data=data)
    database.create(COLLECTION, container)


def main(window_instance: MainWindow) -> None:

    key = barcode_scanner()
    window_instance.update_info(barcode=key)

    if key:
        weight = getting_weight()
        window_instance.update_info(barcode=key, weight=weight)

        if database.get(str(key), COLLECTION):
            _updating(key, weight)
            print('update')
        else:
            _creating(key, weight)
            print('create')
    else:
        print("Видимо вы считали QR код, а не штрих код!")


if __name__ == "__main__":
    database = FireDataBase(KEY)
    pin_in = PinIN(40)
    pin_out = PinOUT(38)
    button = Button(pin_in, pin_out)
    window = MainWindow()

    try:
        while True:
            if button.is_pressed():
                main(window)
    except KeyboardInterrupt:
        button.cleanup()
        window.quit()
