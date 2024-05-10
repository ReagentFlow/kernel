from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFrame, QHBoxLayout
from src.scanner import barcode_scanner
from src.scales import getting_weight
import time


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("ReagentFlow system barcode and weight info")

        font = QFont()
        font.setPointSize(30)

        self.barcode_label = QLabel()
        self.barcode_label.setFont(font)
        self.weight_label = QLabel()
        self.weight_label.setFont(font)

        self.scan_button = QPushButton("Scan Barcode")
        self.scan_button.setFont(font)
        self.scan_button.clicked.connect(barcode_scanner)
        self.weight_button = QPushButton("Get Weight")
        self.weight_button.setFont(font)
        self.weight_button.clicked.connect(getting_weight)

        barcode_frame = QFrame()
        barcode_frame.setStyleSheet("background-color: grey;")
        barcode_layout = QHBoxLayout(barcode_frame)
        barcode_layout.addWidget(self.barcode_label)
        barcode_layout.setAlignment(Qt.AlignCenter)

        weight_frame = QFrame()
        weight_frame.setStyleSheet("background-color: grey;")
        weight_layout = QHBoxLayout(weight_frame)
        weight_layout.addWidget(self.weight_label)
        weight_layout.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(barcode_frame)
        layout.addWidget(weight_frame)
        layout.addWidget(self.scan_button)
        layout.addWidget(self.weight_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_info(self, barcode: int, weight: int) -> None:
        self.barcode_label.setText(f"Barcode: {barcode}")
        self.weight_label.setText(f"Weight: {weight}")

    def show(self):
        super(MainWindow, self).showFullScreen()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    window.update_info(barcode=777, weight=0)
    app.processEvents()

    time.sleep(2)
    window.update_info(barcode=777777, weight=12)
    app.processEvents()

    time.sleep(2)
    window.update_info(barcode=111111, weight=1232323)
    app.processEvents()

    time.sleep(2)
    window.update_info(barcode=9090090, weight=100)
    app.processEvents()

    QTimer.singleShot(3000, app.quit)
    app.exec_()
