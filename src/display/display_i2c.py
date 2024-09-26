from RPLCD.i2c import CharLCD
import smbus2
import time


class Display:
    def __init__(self, i2c_expander_address=0x27, i2c_port=1):
        self.lcd = CharLCD(i2c_expander='PCF8574',
                           address=i2c_expander_address,
                           port=i2c_port,
                           cols=16, rows=2, dotsize=8)

    def display_message(self, message: str):
        self.lcd.clear()
        self.lcd.write_string(message)

    def clear(self):
        self.lcd.clear()

    def close(self):
        self.lcd.close(clear=True)


if __name__ == '__main__':
    display = Display()
    try:
        display.clear()
        display.display_message("start")
        time.sleep(5)
    finally:
        display.clear()
        display.close()
