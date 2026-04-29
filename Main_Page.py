from pathlib import Path
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        # Layout type
        vbox = QVBoxLayout()
        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        title_lbl = QLabel("Everything Dashboard - Websites Scraped Here!")
        title_lbl.alignment = Qt.AlignCenter
        title_lbl.set_style_sheet("""
            QLabel {
                font-size: 36px;
                font-weight: bold;
                color: White;
                margin-bottom: 20px;
            }
        """)

        # Create button (widget type)
        my_btn1 = QPushButton('')
        my_btn2 = QPushButton('')
        my_btn3 = QPushButton('')
        my_btn4 = QPushButton('')


        # Style Sheets for the backgorund images
        my_btn1.set_style_sheet("""
            QPushButton {
                border-image: url(newsImage.jpg) 0 0 0 0 stretch stretch;
                border: 1px solid black;
                color: white;
                font-size: 32px;
                min-width: 600px;
                min-height: 400px;
            }
        """)
        my_btn2.set_style_sheet("""
            QPushButton {
                border-image: url(sportsImage.jpg) 0 0 0 0 stretch stretch;
                border: 1px solid black;
                color: white;
                font-size: 32px;
                min-width: 600px;
                min-height: 400px;
            }
        """)
        my_btn3.set_style_sheet("""
            QPushButton {
                border-image: url(cardImage.jpg) 0 0 0 0 stretch stretch;
                border: 1px solid black;
                color: black;
                font-size: 32px;
                min-width: 600px;
                min-height: 400px;
            }
        """)
        my_btn4.set_style_sheet("""
            QPushButton {
                border-image: url(todoImage.jpg) 0 0 0 0 stretch stretch;
                border: 1px solid black;
                color: black;
                font-size: 32px;
                min-width: 600px;
                min-height: 400px;
            }
        """)



        #self.my_lbl = QLabel('button not yet clicked')

        # Connect the button (widget) to the desired function (@Slot())
        #my_btn1.clicked.connect(self.on_click)

        #vbox.add_widget(self.my_lbl)

        # Add button (widget) to layout type
        vbox.add_widget(title_lbl)
        row1.add_widget(my_btn1)
        row1.add_widget(my_btn2)

        row2.add_widget(my_btn3)
        row2.add_widget(my_btn4)

        vbox.add_layout(row1)
        vbox.add_layout(row2)

        self.set_layout(vbox)
        
        self.resize(1300, 900)
        self.show()

    # Change this to be connected to a scene change
    # @Slot()
    # def on_click(self):
    #     self.my_lbl.text = 'button has been clicked!'


app = QApplication([])
my_class = MainPage()
my_class.show()
sys.exit(app.exec())