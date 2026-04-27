import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QComboBox, QVBoxLayout, QHBoxLayout, QGroupBox
)
from PySide6.QtCore import Qt, QMargins
from __feature__ import snake_case, true_property


class LiveNewsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = "Live News"

        title = QLabel("<h2>Live News</h2>")
        title.alignment = Qt.AlignCenter
        title.maximum_height = 40

        search_label = QLabel("Search:")
        search_box = QLineEdit()
        search_btn = QPushButton("Search")

        sort_label = QLabel("Sort by:")
        sort_box = QComboBox()
        sort_box.add_item("Newest")
        sort_box.add_item("Oldest")

        category_label = QLabel("Category:")
        category_box = QComboBox()
        category_box.add_item("All")
        category_box.add_item("Breaking")
        category_box.add_item("World")
        category_box.add_item("Tech")
        category_box.add_item("Sports")

        search_layout = QHBoxLayout()
        search_layout.spacing = 5
        search_layout.add_widget(search_label)
        search_layout.add_widget(search_box)
        search_layout.add_widget(search_btn)
        search_layout.add_widget(sort_label)
        search_layout.add_widget(sort_box)
        search_layout.add_widget(category_label)
        search_layout.add_widget(category_box)

        headlines_box = QGroupBox("Headlines")

        headlines_layout = QVBoxLayout()
        headlines_layout.spacing = 5
        headlines_layout.alignment = Qt.AlignTop

        headline1 = QLabel("Placeholder 1")
        headline2 = QLabel("Placeholder 2")
        headline3 = QLabel("Placeholder 3")
        headline4 = QLabel("Placeholder 4")

        for h in [headline1, headline2, headline3, headline4]:
            h.maximum_height = 20
            headlines_layout.add_widget(h)

        headlines_box.set_layout(headlines_layout)

        story_box = QGroupBox("Selected Story")

        story_layout = QVBoxLayout()
        story_layout.spacing = 5
        story_layout.alignment = Qt.AlignTop

        title_label = QLabel("Title: ________________________________")
        summary_label = QLabel("Summary: _____________________________")
        summary_line2 = QLabel("______________________________________")
        summary_line3 = QLabel("______________________________________")
        link_label = QLabel("Link: _________________________________")

        for s in [title_label, summary_label, summary_line2, summary_line3, link_label]:
            s.maximum_height = 20
            story_layout.add_widget(s)

        story_box.set_layout(story_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.spacing = 10
        bottom_layout.add_widget(headlines_box)
        bottom_layout.add_widget(story_box)

        main_layout = QVBoxLayout()
        main_layout.spacing = 5
        main_layout.contents_margins = QMargins(10, 10, 10, 10)
        main_layout.alignment = Qt.AlignTop

        main_layout.add_widget(title)
        main_layout.add_layout(search_layout)
        main_layout.add_layout(bottom_layout)

        self.set_layout(main_layout)
        self.resize(900, 500)
        self.show()


app = QApplication([])
win = LiveNewsWindow()
sys.exit(app.exec())