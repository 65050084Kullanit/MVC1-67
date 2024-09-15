import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog, QLineEdit, QPushButton, QVBoxLayout
from Controller.inputValid import validInput

class MainWindow(QWidget):
    def __init__(self):
        # สร้าง window
        super().__init__()
        self.setWindowTitle('My PyQt5 Window')
        self.setGeometry(100, 100, 500, 100)

        self.layout = QVBoxLayout()

        #รับข้อมูล input id
        self.idInputLabel = QLabel("Enter ID :")
        self.idInput = QLineEdit()

        #ทำปุ่มหน้ารับ input
        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.submitButtonclicked)

        # ปรับแต่งขนาดตัวอักษรและสีของ label, input และปุ่ม
        self.idInputLabel.setStyleSheet("font-weight:, bold; font-size: 14px;")
        self.idInput.setStyleSheet("font-size: 14px;")
        self.submitButton.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px; padding 10px;")

        # เพิ่มทุกอย่างในหน้า UI
        self.layout.addWidget(self.idInputLabel)
        self.layout.addWidget(self.idInput)
        self.layout.addWidget(self.submitButton)

        self.setLayout(self.layout)


    # สร้าง Action เมื่อกดปุ่ม
    def submitButtonclicked(self):
        id = self.idInput.text()
        print("Id : ", id)

        isValid = validInput(id)
        print("Is Valid : ", isValid)

