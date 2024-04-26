import serial
from src.constants import SCANNER_PORT
from typing import Union


def barcode_scanner() -> Union[int, None]:
    ser = serial.Serial(SCANNER_PORT, 9600, timeout=0.1)
    s = ser.readline()
    while s == b'':
        s = ser.readline()
    ser.close()
    decoded = s.decode('utf-8').strip('\r')

    try:
        return int(decoded)
    except ValueError:
        return None


if __name__ == '__main__':
    for _ in range(20):
        print(barcode_scanner())
