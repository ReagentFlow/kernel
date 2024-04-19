import serial
from src.constants import SCANNER_PORT


def barcode_scanner():
    ser = serial.Serial(SCANNER_PORT, 9600, timeout=0.1)
    s = ser.readline()
    while s == b'':
        s = ser.readline()
    ser.close()

    # Тут при декодировании рухнет с ошибкой, если считывать не штрих код, а QR допустим (сканнер может все подряд считывать)
    decoded = s.decode('utf-8').strip('\r')
    return int(decoded)


if __name__ == '__main__':
    for _ in range(20):
        print(barcode_scanner())
