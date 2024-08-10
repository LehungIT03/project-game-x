import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import QSize, Qt


class hienThiTen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hiển thị tên")
        self.setGeometry(800, 400, 200, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.text_edit = QLineEdit()
        self.display_button = QPushButton("Hiển thị")
        self.result_label = QLabel("")

        layout = QVBoxLayout()

        layout.addWidget(self.text_edit)
        layout.addWidget(self.display_button)
        layout.addWidget(self.result_label)

        central_widget.setLayout(layout)

        self.display_button.clicked.connect(self.display_text)

    def display_text(self):
        entered_text = self.text_edit.text()
        self.result_label.setText(f"Tên của bạn là : {entered_text}")


def main():
    app = QApplication(sys.argv)
    window = hienThiTen()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
