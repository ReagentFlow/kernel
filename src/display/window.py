import tkinter as tk
from tkinter import font
from src.scanner import barcode_scanner
from src.scales import getting_weight

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ReagentFlow system barcode and weight info")
        self.geometry("800x480")  # Размер экрана Raspberry Pi

        self.font = font.Font(size=30)

        self.barcode_label = tk.Label(self, font=self.font, bg="grey")
        self.barcode_label.pack(expand=True, fill=tk.BOTH)

        self.weight_label = tk.Label(self, font=self.font, bg="grey")
        self.weight_label.pack(expand=True, fill=tk.BOTH)

        self.scan_button = tk.Button(self, text="Scan Barcode", font=self.font, command=barcode_scanner)
        self.scan_button.pack(expand=True, fill=tk.BOTH)

        self.weight_button = tk.Button(self, text="Get Weight", font=self.font, command=getting_weight)
        self.weight_button.pack(expand=True, fill=tk.BOTH)

    def update_info(self, barcode=None, weight=None):
        if barcode is not None:
            self.barcode_label.config(text=f"Barcode: {barcode}")
        if weight is not None:
            self.weight_label.config(text=f"Weight: {weight}")

if __name__ == "__main__":
    window = MainWindow()

    window.update_info(barcode=777)
    window.after(2000, lambda: window.update_info(barcode=777777, weight=12))
    window.after(4000, lambda: window.update_info(barcode=111111, weight=1232323))
    window.after(6000, lambda: window.update_info(barcode=9090090, weight=100))
    window.after(8000, window.quit)

    window.mainloop()
