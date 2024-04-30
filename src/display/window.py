from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Barcode and Weight Information")

        self.barcode_label = QLabel()
        self.weight_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.barcode_label)
        layout.addWidget(self.weight_label)

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
    window.update_info(barcode=1234477777777, weight=1235)
    app.exec_()
