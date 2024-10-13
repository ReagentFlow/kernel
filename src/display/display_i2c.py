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

        # Разбиваем сообщение на строки по 16 символов (cols = 16)
        max_cols = 16
        lines = []
        for i in range(0, len(message), max_cols):
            lines.append(message[i:i + max_cols])

        # Выводим строки на дисплей
        for i, line in enumerate(lines[:2]):  # Выводим только 2 строки (lcd на 2 строки)
            self.lcd.cursor_pos = (i, 0)  # Устанавливаем позицию курсора
            self.lcd.write_string(line)  # Печатаем строку как есть

    def display_message_centered(self, message: str):
        self.lcd.clear()

        # Разбиваем сообщение на строки по 16 символов (cols = 16)
        max_cols = 16
        lines = []
        for i in range(0, len(message), max_cols):
            lines.append(message[i:i + max_cols])

        # Центрирование каждой строки
        for i, line in enumerate(lines[:2]):
            line = line.strip()  # Убираем лишние пробелы по краям
            padding = (max_cols - len(line)) // 2  # Вычисляем количество пробелов для центрирования
            centered_line = ' ' * padding + line  # Добавляем нужное количество пробелов перед строкой
            self.lcd.cursor_pos = (i, 0)  # Устанавливаем позицию курсора
            self.lcd.write_string(centered_line)  # Печатаем строку по центру

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
