from pathlib import Path
import sys
from urllib import request
from __feature__ import snake_case, true_property
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot, Qt, Signal

from tcg_scrape import get_random_card, get_sets, get_set_cards, get_set
import requests


# my_app = QApplication([])


class TCGPage(QWidget):
    go_back = Signal()
    go_to_item_view = Signal()

    def __init__(self):
        super().__init__()
        
        #information for set and respective cards
        lorwyn_details = get_set("ECL")
        tmnt_details = get_set("TMT")
        stixhaven_details = get_set("SOS")
        
        highlighted_card = get_random_card()
        
        #main layout
        self.content_box = QVBoxLayout()
        self.mbox = QHBoxLayout()
        
        self.header_box = QHBoxLayout()
        # header_box.add_widget(QPushButton("Back"), alignment=Qt.AlignLeft, stretch=1)
        #Connected back button - Bryan
        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)
        self.header_box.add_widget(back_btn, alignment=Qt.AlignLeft, stretch=1)
        self.header_box.add_widget(QLabel("TCG Collection Tracker"), alignment=Qt.AlignLeft, stretch=1)
        
        search_box = QHBoxLayout()
        search_box.add_widget(QLineEdit("Search"), alignment=Qt.AlignRight, stretch=2)
        search_box.add_widget(QPushButton("Search"), alignment=Qt.AlignRight, stretch=1)
        self.header_box.add_layout(search_box, stretch=1)
        self.content_box.add_layout(self.header_box, stretch=1)
        
        
        self.card_set_box = QVBoxLayout()
        
        self.highlighted_card_box = QVBoxLayout()
        self.highlighted_card_box.add_widget(QLabel("Highlighted Card"), alignment=Qt.AlignTop | Qt.AlignCenter)
        
        self.highlight_details_box = QVBoxLayout()
        
        self.card_image_label = QLabel()
        image_path = Path(__file__).parent / "highlight_card.jpg"
        card_pixmap = QPixmap(str(image_path))
        self.card_image_label.pixmap = card_pixmap
        self.highlight_details_box.add_widget(self.card_image_label, alignment=Qt.AlignTop | Qt.AlignCenter)
        self.highlight_details_box.add_widget(QLabel(f"Name: {highlighted_card['name']}"), alignment=Qt.AlignTop | Qt.AlignCenter)
        self.highlight_details_box.add_widget(QLabel(f"Set: {highlighted_card['set_name']}"), alignment=Qt.AlignTop | Qt.AlignCenter)
        self.highlighted_card_box.add_layout(self.highlight_details_box, stretch=4)
        
        
        self.card_list_box = QVBoxLayout()
        self.card_list_box.add_widget(QLabel("Card List"), alignment=Qt.AlignTop | Qt.AlignCenter, stretch=1)
        self.card_list = QVBoxLayout()
        self.card_list_box.add_layout(self.card_list, stretch=19)
        
        # Added view card button that utilizes item view - Bryan
        # view_card_btn = QPushButton("View Card")
        # view_card_btn.clicked.connect(self.go_to_item_view)
        # self.card_list_box.add_widget(view_card_btn, alignment=Qt.AlignTop | Qt.AlignCenter)
        
        self.set_list_box = QVBoxLayout()
        self.set_list_box.add_widget(QLabel("Set List"), alignment=Qt.AlignTop | Qt.AlignCenter, stretch=1)
        
        self.list_box = QHBoxLayout()
        self.lorwyn_btn = QPushButton("Lorwyn")
        self.lorwyn_btn.clicked.connect(lambda: self.display_set_cards("ECL"))
        self.tmnt_btn = QPushButton("TMNT")
        self.tmnt_btn.clicked.connect(lambda: self.display_set_cards("TMT"))
        self.stixhaven_btn = QPushButton("Secrets of Strixhaven")
        self.stixhaven_btn.clicked.connect(lambda: self.display_set_cards("SOS"))

        self.list_box.add_widget(self.lorwyn_btn, alignment=Qt.AlignTop | Qt.AlignCenter)
        self.list_box.add_widget(self.tmnt_btn, alignment=Qt.AlignTop | Qt.AlignCenter)
        self.list_box.add_widget(self.stixhaven_btn, alignment=Qt.AlignTop | Qt.AlignCenter)
             
        
        self.set_list_box.add_layout(self.list_box, stretch=4)
        
        self.card_set_box.add_layout(self.highlighted_card_box, stretch=4)
        self.card_set_box.add_layout(self.set_list_box, stretch=1)
        
        self.mbox.add_layout(self.card_set_box, stretch=3)
        self.mbox.add_layout(self.card_list_box, stretch=1)
        
        self.content_box.add_layout(self.mbox, stretch=20)
        
        self.display_set_cards("ECL")
        self.set_layout(self.content_box)
        self.resize(900, 600)
    
    def clear_displayed_cards(self):
        for i in reversed(range(self.card_list.count())):
            widget = self.card_list.item_at(i).widget()
            if widget is not None:
                widget.set_parent(None)
        
    def display_set_cards(self, set_code):
        cards = get_set_cards(set_code)
        self.clear_displayed_cards()
        
        for card in cards['data'][:10]:
            self.card_list.add_widget(QLabel(f"Name: {card['name']}, Set: {card['set_name']}"))