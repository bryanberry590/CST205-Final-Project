from pathlib import Path
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property


class SportsDashboard(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()

        page_title = QLabel('Live Sports News')
        title_font = page_title.font
        title_font.set_point_size(22)
        title_font.set_bold(True)
        page_title.font = title_font
        page_title.alignment = Qt.AlignHCenter
        vbox.add_widget(page_title)

        # search bar template; doesn't wire to anything yet
        search_bar = QHBoxLayout()
        self.search_edit = QLineEdit()
        self.search_edit.placeholder_text = 'Search…'
        search_btn = QPushButton('Search')
        search_bar.add_widget(self.search_edit)
        search_bar.add_widget(search_btn)
        vbox.add_layout(search_bar)

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

        head1 = QLabel('Sample headline: home team wins in overtime')
        hf1 = head1.font
        hf1.set_point_size(15)
        hf1.set_bold(True)
        head1.font = hf1
        body1 = QLabel('Short excerpt placeholder.')
        card1 = QWidget()
        card1.object_name = 'article_card'
        card1.style_sheet = card_style
        inner1 = QVBoxLayout()
        inner1.add_widget(head1)
        inner1.add_widget(body1)
        card1.set_layout(inner1)
        vbox.add_widget(card1)

        head2 = QLabel('Another story: trade rumors heat up before deadline')
        hf2 = head2.font
        hf2.set_point_size(15)
        hf2.set_bold(True)
        head2.font = hf2
        body2 = QLabel('Second excerpt placeholder.')
        card2 = QWidget()
        card2.object_name = 'article_card'
        card2.style_sheet = card_style
        inner2 = QVBoxLayout()
        inner2.add_widget(head2)
        inner2.add_widget(body2)
        card2.set_layout(inner2)
        vbox.add_widget(card2)

        head3 = QLabel('Injury report: star player listed day-to-day')
        hf3 = head3.font
        hf3.set_point_size(15)
        hf3.set_bold(True)
        head3.font = hf3
        body3 = QLabel('Short excerpt placeholder.')
        card3 = QWidget()
        card3.object_name = 'article_card'
        card3.style_sheet = card_style
        inner3 = QVBoxLayout()
        inner3.add_widget(head3)
        inner3.add_widget(body3)
        card3.set_layout(inner3)
        vbox.add_widget(card3)

        head4 = QLabel('Trade rumors')
        hf4 = head4.font
        hf4.set_point_size(15)
        hf4.set_bold(True)
        head4.font = hf4
        body4 = QLabel('Short excerpt placeholder.')
        card4 = QWidget()
        card4.object_name = 'article_card'
        card4.style_sheet = card_style
        inner4 = QVBoxLayout()
        inner4.add_widget(head4)
        inner4.add_widget(body4)
        card4.set_layout(inner4)
        vbox.add_widget(card4)

        head5 = QLabel('NBA Star retiring')
        hf5 = head5.font
        hf5.set_point_size(15)
        hf5.set_bold(True)
        head5.font = hf5
        body5 = QLabel('Short excerpt placeholder.')
        card5 = QWidget()
        card5.object_name = 'article_card'
        card5.style_sheet = card_style
        inner5 = QVBoxLayout()
        inner5.add_widget(head5)
        inner5.add_widget(body5)
        card5.set_layout(inner5)
        vbox.add_widget(card5)

        self.set_layout(vbox)
        self.resize(800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    my_class = SportsDashboard()
    my_class.show()
    sys.exit(app.exec())
