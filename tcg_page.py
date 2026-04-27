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
        mbox = QHBoxLayout()
        
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
        
        
        self.set_layout(mbox)
        self.resize(900, 600)
        self.show()
    


my_win = TCGPage()
sys.exit(my_app.exec())