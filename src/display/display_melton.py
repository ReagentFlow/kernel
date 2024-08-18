import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD


class Display:
    def __init__(self, rs_pin, e_pin, data_pins, cols=16, rows=2):
        # Настройка GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Настройка дисплея
        self.lcd = CharLCD(pin_rs=rs_pin, pin_rw=None, pin_e=e_pin, pins_data=data_pins,
                           numbering_mode=GPIO.BCM, cols=cols, rows=rows, dotsize=8)

    def display_message(self, message: str):
        self.lcd.clear()
        self.lcd.write_string(message)

    def clear(self):
        self.lcd.clear()

    def close(self):
        self.lcd.close(clear=True)
        GPIO.cleanup()


if __name__ == '__main__':
    rs_pin = 26
    e_pin = 19
    data_pins = [13, 6, 5, 11]

    display = Display(rs_pin=rs_pin, e_pin=e_pin, data_pins=data_pins)

    display.display_message("start")
