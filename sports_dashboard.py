from pathlib import Path
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser, QScrollArea)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal, Slot
from urllib.request import urlopen
from __feature__ import snake_case, true_property
from sports_scrape import (bball_article_text, ftball_article_text, bsball_article_text, tenn_article_text, wnba_article_text, 
ftball_text_title, bball_text_title, bsball_text_title, tenn_text_title, wnba_text_title, 
bball_image_url, ftball_image_url, bsball_image_url, tenn_image_url, wnba_image_url)

"""
Displays the scraped article data from ESPN. Users can input keyword(s) and click "Search" to display full article text, 
or click "Read More" to display full article text.

Author: Jeslyn See (unless otherwise stated)
"""

class SportsDashboard(QWidget):
    go_back = Signal()

    # helper function to load images using QPixmap 
    def load_image_from_url(self, url):
        data = urlopen(url).read()
        pixmap = QPixmap()
        pixmap.load_from_data(data)
        return pixmap

    # individual slots for each article's read more button
    @Slot()
    def show_bball(self):
        self.detail_title.text = bball_text_title
        self.detail_body.text = bball_article_text

    @Slot()
    def show_ftball(self):
        self.detail_title.text = ftball_text_title
        self.detail_body.text = ftball_article_text

    @Slot()
    def show_bsball(self):
        self.detail_title.text = bsball_text_title
        self.detail_body.text = bsball_article_text

    @Slot()
    def show_tenn(self):
        self.detail_title.text = tenn_text_title
        self.detail_body.text = tenn_article_text

    @Slot()
    def show_wnba(self):
        self.detail_title.text = wnba_text_title
        self.detail_body.text = wnba_article_text

    # wiring up search button here; if keyword appears in article body text, will display that article
    @Slot()
    def search_article(self):
        keyword = self.search_edit.text
        if keyword in ftball_article_text:
            self.detail_title.text = ftball_text_title
            self.detail_body.text = ftball_article_text
        elif keyword in bball_article_text:
            self.detail_title.text = bball_text_title
            self.detail_body.text = bball_article_text
        elif keyword in bsball_article_text:
            self.detail_title.text = bsball_text_title
            self.detail_body.text = bsball_article_text
        elif keyword in tenn_article_text:
            self.detail_title.text = tenn_text_title
            self.detail_body.text = tenn_article_text
        elif keyword in wnba_article_text:
            self.detail_title.text = wnba_text_title
            self.detail_body.text = wnba_article_text


    def __init__(self):
        super().__init__()

        no_scroll_layout = QVBoxLayout()

        # Added back button - Bryan
        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)
        no_scroll_layout.add_widget(back_btn, alignment=Qt.AlignLeft)

        page_title = QLabel('Live Sports News')
        title_font = page_title.font
        title_font.set_point_size(22)
        title_font.set_bold(True)
        page_title.font = title_font
        page_title.alignment = Qt.AlignHCenter
        no_scroll_layout.add_widget(page_title)

        # search bar wired up to search_article slot
        search_bar = QHBoxLayout()
        self.search_edit = QLineEdit()
        self.search_edit.placeholder_text = 'Search…'
        search_btn = QPushButton('Search')
        search_btn.clicked.connect(self.search_article)
        search_bar.add_widget(self.search_edit)
        search_bar.add_widget(search_btn)
        no_scroll_layout.add_layout(search_bar)

        # defining CSS style sheet for the article cards to apply below
        card_style = """
            QWidget#article_card {
                border: 1px solid #b0b0b0;
                border-radius: 10px;
                background-color: #f7f7f7;
                padding: 12px;
            }
            QWidget#article_card QLabel {
                color: #000000;
            }
        """

        # vbox holds all article cards on the left side
        vbox = QVBoxLayout()

        # hardcoded start and end of text body to give excerpt style display

        # basketball card - image on left, title and excerpt on right
        head1 = QLabel(bball_text_title)
        hf1 = head1.font
        hf1.set_point_size(15)
        hf1.set_bold(True)
        head1.font = hf1
        img1 = QLabel()
        pixmap1 = self.load_image_from_url(bball_image_url)
        img1.pixmap = pixmap1.scaled(200, 120, Qt.KeepAspectRatio)
        body1 = QLabel(bball_article_text[97:300] + '...')
        body1.word_wrap = True
        read_more1 = QPushButton('Read More')
        read_more1.style_sheet = "color: black;"
        read_more1.clicked.connect(self.show_bball)
        card1 = QWidget()
        card1.object_name = 'article_card'
        card1.style_sheet = card_style
        inner1 = QHBoxLayout()
        text_side1 = QVBoxLayout()
        text_side1.add_widget(head1)
        text_side1.add_widget(body1)
        text_side1.add_widget(read_more1)
        inner1.add_widget(img1)
        inner1.add_layout(text_side1)
        card1.set_layout(inner1)
        vbox.add_widget(card1)

        # football card - image on left, title and excerpt on right
        head2 = QLabel(ftball_text_title)
        hf2 = head2.font
        hf2.set_point_size(15)
        hf2.set_bold(True)
        head2.font = hf2
        img2 = QLabel()
        pixmap2 = self.load_image_from_url(ftball_image_url)
        img2.pixmap = pixmap2.scaled(200, 120, Qt.KeepAspectRatio)
        body2 = QLabel(ftball_article_text[41:300] + '...')
        body2.word_wrap = True
        read_more2 = QPushButton('Read More')
        read_more2.style_sheet = "color: black;"
        read_more2.clicked.connect(self.show_ftball)
        card2 = QWidget()
        card2.object_name = 'article_card'
        card2.style_sheet = card_style
        inner2 = QHBoxLayout()
        text_side2 = QVBoxLayout()
        text_side2.add_widget(head2)
        text_side2.add_widget(body2)
        text_side2.add_widget(read_more2)
        inner2.add_widget(img2)
        inner2.add_layout(text_side2)
        card2.set_layout(inner2)
        vbox.add_widget(card2)

        # baseball card - image on left, title and excerpt on right
        head3 = QLabel(bsball_text_title)
        hf3 = head3.font
        hf3.set_point_size(15)
        hf3.set_bold(True)
        head3.font = hf3
        img3 = QLabel()
        pixmap3 = self.load_image_from_url(bsball_image_url)
        img3.pixmap = pixmap3.scaled(200, 120, Qt.KeepAspectRatio)
        body3 = QLabel(bsball_article_text[78:300] + '...')
        body3.word_wrap = True
        read_more3 = QPushButton('Read More')
        read_more3.style_sheet = "color: black;"
        read_more3.clicked.connect(self.show_bsball)
        card3 = QWidget()
        card3.object_name = 'article_card'
        card3.style_sheet = card_style
        inner3 = QHBoxLayout()
        text_side3 = QVBoxLayout()
        text_side3.add_widget(head3)
        text_side3.add_widget(body3)
        text_side3.add_widget(read_more3)
        inner3.add_widget(img3)
        inner3.add_layout(text_side3)
        card3.set_layout(inner3)
        vbox.add_widget(card3)

        # tennis card - image on left, title and excerpt on right
        head4 = QLabel(tenn_text_title)
        hf4 = head4.font
        hf4.set_point_size(15)
        hf4.set_bold(True)
        head4.font = hf4
        img4 = QLabel()
        pixmap4 = self.load_image_from_url(tenn_image_url)
        img4.pixmap = pixmap4.scaled(200, 120, Qt.KeepAspectRatio)
        body4 = QLabel(tenn_article_text[76:300] + '...')
        body4.word_wrap = True
        read_more4 = QPushButton('Read More')
        read_more4.style_sheet = "color: black;"
        read_more4.clicked.connect(self.show_tenn)
        card4 = QWidget()
        card4.object_name = 'article_card'
        card4.style_sheet = card_style
        inner4 = QHBoxLayout()
        text_side4 = QVBoxLayout()
        text_side4.add_widget(head4)
        text_side4.add_widget(body4)
        text_side4.add_widget(read_more4)
        inner4.add_widget(img4)
        inner4.add_layout(text_side4)
        card4.set_layout(inner4)
        vbox.add_widget(card4)

        # wnba card - image on left, title and excerpt on right
        head5 = QLabel(wnba_text_title)
        hf5 = head5.font
        hf5.set_point_size(15)
        hf5.set_bold(True)
        head5.font = hf5
        img5 = QLabel()
        pixmap5 = self.load_image_from_url(wnba_image_url)
        img5.pixmap = pixmap5.scaled(200, 120, Qt.KeepAspectRatio)
        body5 = QLabel(wnba_article_text[98:300] + '...')
        body5.word_wrap = True
        read_more5 = QPushButton('Read More')
        read_more5.style_sheet = "color: black;"
        read_more5.clicked.connect(self.show_wnba)
        card5 = QWidget()
        card5.object_name = 'article_card'
        card5.style_sheet = card_style
        inner5 = QHBoxLayout()
        text_side5 = QVBoxLayout()
        text_side5.add_widget(head5)
        text_side5.add_widget(body5)
        text_side5.add_widget(read_more5)
        inner5.add_widget(img5)
        inner5.add_layout(text_side5)
        card5.set_layout(inner5)
        vbox.add_widget(card5)

        vbox.add_stretch()

        # created container and scroll view, so the cards on the left are scrollable (using QScrollArea)
        container = QWidget()
        container.set_layout(vbox)
        container.minimum_height = 1000

        scroll = QScrollArea()
        scroll.set_widget(container)
        scroll.widget_resizable = True

        # right panel - displays full article text when Read More is clicked
        self.detail_title = QLabel('Select an article to read more.')
        self.detail_title.word_wrap = True
        self.detail_title.alignment = Qt.AlignTop
        detail_title_font = self.detail_title.font
        detail_title_font.set_point_size(15)
        detail_title_font.set_bold(True)
        self.detail_title.font = detail_title_font
        self.detail_body = QLabel('')
        self.detail_body.word_wrap = True
        self.detail_body.alignment = Qt.AlignTop
        self.detail_panel = QVBoxLayout()
        self.detail_panel.add_widget(self.detail_title)
        self.detail_panel.add_widget(self.detail_body)
        self.detail_panel.add_stretch()

        # wrapping right panel in container then scroll area so article text is scrollable
        right_container = QWidget()
        right_container.set_layout(self.detail_panel)
        right_container.minimum_height = 1000

        right_panel_scroll = QScrollArea()
        right_panel_scroll.set_widget(right_container)
        right_panel_scroll.widget_resizable = True

        # cards on left and detail panel on the right
        cards_and_detail = QHBoxLayout()
        cards_and_detail.add_widget(scroll)
        cards_and_detail.add_widget(right_panel_scroll)

        outer = QVBoxLayout()
        outer.add_layout(no_scroll_layout)
        outer.add_layout(cards_and_detail)
        self.set_layout(outer)
        self.resize(800, 600)
        # self.show()


if __name__ == '__main__':
    app = QApplication([])
    my_class = SportsDashboard()
    my_class.show()
    sys.exit(app.exec())