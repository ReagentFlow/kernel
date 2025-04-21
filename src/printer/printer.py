import barcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageWin
import win32print
import win32ui
import win32con
import os


class Printer:
    def __init__(self):
        self.printers = self.get_all_printers()
        self.printer_name = None

    def get_all_printers(self):
        """Возвращает список всех доступных принтеров"""
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        return [printer[2] for printer in printers]

    def select_printer_by_index(self, index):
        """Выбирает принтер по индексу (с 1)"""
        if 0 < index <= len(self.printers):
            self.printer_name = self.printers[index - 1]
        else:
            raise ValueError("Неверный номер принтера")

    def generate_barcode(self, data: str, output_path="barcode_print_ready.png"):
        """Генерирует EAN-13 штрихкод"""
        if len(data) != 12 or not data.isdigit():
            raise ValueError("EAN-13 код должен содержать ровно 12 цифр")

        barcode_image = EAN13(data, writer=ImageWriter())
        filename = barcode_image.save("barcode_temp")

        img = Image.open(filename).convert("RGB")
        img = img.resize((228, 118))  # 58x30 мм при 300 DPI
        img.save(output_path)
        os.remove(filename)  # удаляем временный файл
        return output_path

    def print_image(self, image_path: str):
        """Отправляет изображение на печать"""
        if not self.printer_name:
            raise RuntimeError("Принтер не выбран")

        hprinter = win32print.OpenPrinter(self.printer_name)
        img = Image.open(image_path).convert("RGB")
        try:
            hdc = win32ui.CreateDC()
            hdc.CreatePrinterDC(self.printer_name)

            printable_width = hdc.GetDeviceCaps(win32con.HORZRES)
            printable_height = hdc.GetDeviceCaps(win32con.VERTRES)

            dib = ImageWin.Dib(img)

            hdc.StartDoc("Barcode Print")
            hdc.StartPage()

            x_pos = (printable_width - img.width) // 2
            y_pos = (printable_height - img.height) // 2

            dib.draw(hdc.GetHandleOutput(), (x_pos, y_pos, x_pos + img.width, y_pos + img.height))

            hdc.EndPage()
            hdc.EndDoc()

            print(f"Штрих-код отправлен на принтер: {self.printer_name}")

        finally:
            win32print.ClosePrinter(hprinter)

    def list_printers(self):
        """Печатает список доступных принтеров"""
        print("Доступные принтеры:")
        for i, printer in enumerate(self.printers):
            print(f"{i + 1}. {printer}")
