from pathlib import Path
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot, Qt, Signal
from __feature__ import snake_case, true_property

'''
Add tooltip / popup info for buttons
Push animation when buttons are clicked
'''

class MainPage(QWidget):
    go_to_news = Signal()
    go_to_sports = Signal()
    go_to_tcg = Signal()
    go_to_image = Signal()

    def __init__(self):
        super().__init__()

        # Layout type
        vbox = QVBoxLayout()
        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        title_lbl = QLabel("Anything Dashboard - Websites Scraped Here!")
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

        # Tool tips
        my_btn1.tool_tip = "View live news articles and headlines."
        my_btn2.tool_tip = "View live sports news and sports updates."
        my_btn3.tool_tip = "Open the TCG collection tracker."
        my_btn4.tool_tip = "Open the Image of the Day manipulator."

        # Style Sheets for the background images
      
        my_btn1.set_style_sheet("""
            QPushButton {
                border-image: url(newsImage.jpg) 0 0 0 0 stretch stretch;
                border: 4px solid #333;
                border-radius: 16px;
                color: white;
                font-size: 28px;
                min-width: 400px;
                min-height: 270px;
            }
            QPushButton:hover {
                background-color: rgba(41, 128, 185, 0.6);
                border-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: rgba(28, 89, 138, 0.7);
            }
        """)
        my_btn2.set_style_sheet("""
            QPushButton {
                border-image: url(sportsImage.jpg) 0 0 0 0 stretch stretch;
                border: 4px solid #333;
                border-radius: 16px;
                color: white;
                font-size: 28px;
                min-width: 400px;
                min-height: 270px;
            }
            QPushButton:hover {
                background-color: rgba(41, 128, 185, 0.6);
                border-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: rgba(28, 89, 138, 0.7);
            }
        """)
        my_btn3.set_style_sheet("""
            QPushButton {
                border-image: url(cardImage.jpg) 0 0 0 0 stretch stretch;
                border: 4px solid #333;
                border-radius: 16px;
                color: white;
                font-size: 28px;
                min-width: 400px;
                min-height: 270px;
            }
            QPushButton:hover {
                background-color: rgba(41, 128, 185, 0.6);
                border-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: rgba(28, 89, 138, 0.7);
            }
        """)
        my_btn4.set_style_sheet("""
            QPushButton {
                border-image: url(nasa_logo.png) 0 0 0 0 stretch stretch;
                border: 4px solid #333;
                border-radius: 16px;
                color: white;
                font-size: 28px;
                min-width: 400px;
                min-height: 270px;
                background-color: rgba(255, 255, 255, 0.7);
            }
            QPushButton:hover {
                background-color: rgba(41, 128, 185, 0.6);
                border-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: rgba(28, 89, 138, 0.7);
            }
        """)


        # Hook up buttons to signals
        my_btn1.clicked.connect(self.go_to_news)
        my_btn2.clicked.connect(self.go_to_sports)
        my_btn3.clicked.connect(self.go_to_tcg)
        my_btn4.clicked.connect(self.go_to_image)

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