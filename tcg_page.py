from pathlib import Path
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

my_app = QApplication([])


class TCGPage(QWidget):
    def __init__(self):
        super().__init__()
        
        #main layout
        content_box = QVBoxLayout()
        mbox = QHBoxLayout()
        
        header_box = QHBoxLayout()
        header_box.add_widget(QPushButton("Back"), alignment=Qt.AlignLeft, stretch=1)
        header_box.add_widget(QLabel("TCG Collection Tracker"), alignment=Qt.AlignLeft, stretch=1)
        
        search_box = QHBoxLayout()
        search_box.add_widget(QLineEdit("Search"), alignment=Qt.AlignRight, stretch=2)
        search_box.add_widget(QPushButton("Search"), alignment=Qt.AlignRight, stretch=1)
        header_box.add_layout(search_box, stretch=1)
        content_box.add_layout(header_box, stretch=1)
        
        
        card_game_box = QVBoxLayout()
        
        highlighted_card_box = QHBoxLayout()
        highlighted_card_box.add_widget(QLabel("Highlighted Card"), alignment=Qt.AlignTop | Qt.AlignCenter)
        
        card_list_box = QVBoxLayout()
        card_list_box.add_widget(QLabel("Card List"), alignment=Qt.AlignTop | Qt.AlignCenter)
        
        game_list_box = QVBoxLayout()
        game_list_box.add_widget(QLabel("Game List"), alignment=Qt.AlignTop | Qt.AlignCenter, stretch=1)
        
        list_box = QHBoxLayout()
        list_box.add_widget(QLabel("pokemon"), alignment=Qt.AlignTop | Qt.AlignCenter)
        list_box.add_widget(QLabel("magic"), alignment=Qt.AlignTop | Qt.AlignCenter)
        list_box.add_widget(QLabel("yugioh"), alignment=Qt.AlignTop | Qt.AlignCenter)
             
        
        game_list_box.add_layout(list_box, stretch=4)
        
        card_game_box.add_layout(highlighted_card_box, stretch=4)
        card_game_box.add_layout(game_list_box, stretch=1)
        
        mbox.add_layout(card_game_box, stretch=3)
        mbox.add_layout(card_list_box, stretch=1)
        
        content_box.add_layout(mbox, stretch=20)
        
        self.set_layout(content_box)
        self.resize(900, 600)
        self.show()
    


my_win = TCGPage()
sys.exit(my_app.exec())