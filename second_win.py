# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.setLayout(self.layout)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
