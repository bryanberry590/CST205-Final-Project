import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QVBoxLayout,
    QHBoxLayout, QGroupBox
)


def get_news():
    url = "https://www.npr.org/sections/news/"

    try:
        site_html = urlopen(url)
        soup = BeautifulSoup(site_html.read(), "lxml")

        articles = []
        story_items = soup.find_all("article")

        for story in story_items:
            category = "General"
            title = ""
            summary = "No summary found."
            link = url

            category_tag = story.find("h3")
            if category_tag:
                category = category_tag.get_text(strip=True)

            title_tag = story.find("h2")
            if title_tag:
                title = title_tag.get_text(strip=True)

                link_tag = title_tag.find("a")
                if link_tag:
                    link = link_tag.get("href")

            paragraph = story.find("p")
            if paragraph:
                summary = paragraph.get_text(strip=True)

            if title:
                articles.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "category": category
                })

            if len(articles) == 30:
                break

        return articles

    except Exception as e:
        print("Error scraping news:", e)
        return []


class LiveNewsWindow(QWidget):

    go_back = Signal()

    def __init__(self):
        super().__init__()

        self.articles = []
        self.displayed_articles = []

        self.setWindowTitle("Live News")

        title = QLabel("<h2>Live News</h2>")
        title.setAlignment(Qt.AlignCenter)
        title.setMaximumHeight(40)

        search_label = QLabel("Search:")
        self.search_box = QLineEdit()
        search_btn = QPushButton("Search")

        sort_label = QLabel("Sort by:")
        self.sort_box = QComboBox()
        self.sort_box.addItem("Newest")
        self.sort_box.addItem("Oldest")

        category_label = QLabel("Category:")
        self.category_box = QComboBox()
        self.category_box.addItem("All")

        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_box)
        search_layout.addWidget(search_btn)
        search_layout.addWidget(sort_label)
        search_layout.addWidget(self.sort_box)
        search_layout.addWidget(category_label)
        search_layout.addWidget(self.category_box)

        headlines_box = QGroupBox("Headlines")
        headlines_layout = QVBoxLayout()
        headlines_layout.setAlignment(Qt.AlignTop)

        self.headline1 = QLabel("Placeholder 1")
        self.headline2 = QLabel("Placeholder 2")
        self.headline3 = QLabel("Placeholder 3")
        self.headline4 = QLabel("Placeholder 4")
        self.headline5 = QLabel("Placeholder 5")
        self.headline6 = QLabel("Placeholder 6")
        self.headline7 = QLabel("Placeholder 7")
        self.headline8 = QLabel("Placeholder 8")
        self.headline9 = QLabel("Placeholder 9")
        self.headline10 = QLabel("Placeholder 10")

        self.headline_labels = [
            self.headline1,
            self.headline2,
            self.headline3,
            self.headline4,
            self.headline5,
            self.headline6,
            self.headline7,
            self.headline8,
            self.headline9,
            self.headline10
        ]

        for i, label in enumerate(self.headline_labels):
            label.setWordWrap(True)
            label.setMinimumHeight(30)
            label.setStyleSheet("""
                QLabel:hover {
                    color: lightblue;
                }
            """)
            label.mousePressEvent = lambda event, index=i: self.show_story(index)
            headlines_layout.addWidget(label)

        headlines_box.setLayout(headlines_layout)

        story_box = QGroupBox("Selected Story")
        story_layout = QVBoxLayout()
        story_layout.setSpacing(5)
        story_layout.setAlignment(Qt.AlignTop)

        self.story_title = QLabel("Title: ")
        self.category_label = QLabel("Category: ")
        self.summary_label = QLabel("Summary: ")
        self.summary_line2 = QLabel("")
        self.summary_line3 = QLabel("")
        self.link_label = QLabel("Link: ")

        story_labels = [
            self.story_title,
            self.category_label,
            self.summary_label,
            self.summary_line2,
            self.summary_line3,
            self.link_label
        ]

        for label in story_labels:
            label.setWordWrap(True)
            label.setMinimumHeight(20)
            story_layout.addWidget(label)

        story_box.setLayout(story_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(10)
        bottom_layout.addWidget(headlines_box)
        bottom_layout.addWidget(story_box)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addWidget(title)
        main_layout.addLayout(search_layout)
        main_layout.addLayout(bottom_layout)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)

        top_layout = QHBoxLayout()
        top_layout.addWidget(back_btn, alignment=Qt.AlignLeft)
        top_layout.addStretch()

        main_layout.insertLayout(0, top_layout)

        self.setLayout(main_layout)
        self.resize(1100, 600)

        search_btn.clicked.connect(self.search_news)
        self.category_box.currentTextChanged.connect(self.filter_news)
        self.sort_box.currentTextChanged.connect(self.filter_news)

        self.load_news()

    def load_news(self):
        self.articles = get_news()

        categories = []

        for article in self.articles:
            if article["category"] not in categories:
                categories.append(article["category"])

        categories.sort()

        self.category_box.clear()
        self.category_box.addItem("All")

        for category in categories:
            self.category_box.addItem(category)

        self.display_articles(self.articles)

    def display_articles(self, articles):
        self.displayed_articles = articles[:10]

        if self.displayed_articles:
            for i in range(len(self.headline_labels)):
                if i < len(self.displayed_articles):
                    self.headline_labels[i].setText(
                        self.displayed_articles[i]["title"]
                    )
                else:
                    self.headline_labels[i].setText("")

            self.show_story(0)

        else:
            for label in self.headline_labels:
                label.setText("No matching headlines found.")

            self.story_title.setText("Title: No story selected")
            self.category_label.setText("Category: ")
            self.summary_label.setText("Summary: No summary available.")
            self.summary_line2.setText("")
            self.summary_line3.setText("")
            self.link_label.setText("Link: https://www.npr.org/sections/news/")

    def search_news(self):
        self.filter_news()

    def filter_news(self):
        search_text = self.search_box.text().lower()
        selected_category = self.category_box.currentText()
        selected_sort = self.sort_box.currentText()

        results = []

        for article in self.articles:
            title_match = search_text == "" or search_text in article["title"].lower()
            category_match = (
                selected_category == "All"
                or selected_category == article["category"]
            )

            if title_match and category_match:
                results.append(article)

        if selected_sort == "Oldest":
            results.reverse()

        self.display_articles(results)

    def show_story(self, index):
        if index >= len(self.displayed_articles):
            return

        article = self.displayed_articles[index]

        self.story_title.setText("Title: " + article["title"])
        self.category_label.setText("Category: " + article["category"])
        self.summary_label.setText("Summary: " + article["summary"])
        self.summary_line2.setText("")
        self.summary_line3.setText("")
        self.link_label.setText("Link: " + article["link"])


app = QApplication([])

win = LiveNewsWindow()
win.show()

sys.exit(app.exec())