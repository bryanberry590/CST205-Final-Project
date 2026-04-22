from pathlib import Path
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

class RenameMe(QWidget):
    def __init__(self):
        super().__init__()

        # Layout type
        vbox = QVBoxLayout()

        # Create button (widget type)
        my_btn1 = QPushButton('button 1')
        my_btn2 = QPushButton('button 2')
        my_btn3 = QPushButton('button 3')
        my_btn4 = QPushButton('button 4')



        self.my_lbl = QLabel('button not yet clicked')

        # Connect the button (widget) to the desired function (@Slot())
        my_btn1.clicked.connect(self.on_click)

        vbox.add_widget(self.my_lbl)

        # Add button (widget) to layout type
        vbox.add_widget(my_btn1)
        vbox.add_widget(my_btn2)
        vbox.add_widget(my_btn3)
        vbox.add_widget(my_btn4)



        self.set_layout(vbox)
        self.resize(400, 400)
        self.show()

    # Change this to be connected to a scene change
    @Slot()
    def on_click(self):
        self.my_lbl.text = 'button has been clicked!'


app = QApplication([])
my_class = RenameMe()
my_class.show()
sys.exit(app.exec())