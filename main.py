import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from Main_Page import MainPage
from live_news import LiveNewsWindow
from sports_dashboard import SportsDashboard
from tcg_page import TCGPage
from itemView import ItemViewPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.page_titles = [
            "Everything Dashboard",
            "Live News",
            "Live Sports News",
            "TCG Collection Tracker",
            "Item View",
        ]

        self.stack = QStackedWidget()
        self.set_central_widget(self.stack)

        self.main_page   = MainPage()
        self.news_page   = LiveNewsWindow()
        self.sports_page = SportsDashboard()
        self.tcg_page    = TCGPage()
        self.item_page   = ItemViewPage()

        self.stack.add_widget(self.main_page)
        self.stack.add_widget(self.news_page)
        self.stack.add_widget(self.sports_page)
        self.stack.add_widget(self.tcg_page)
        self.stack.add_widget(self.item_page)

        # MainPage buttons
        self.main_page.go_to_news.connect(lambda: self._go(1))
        self.main_page.go_to_sports.connect(lambda: self._go(2))
        self.main_page.go_to_tcg.connect(lambda: self._go(3))

        # Back buttons - this tells the specific back buttons where to go to using the index positions from lines 25-29
        self.news_page.go_back.connect(lambda: self._go(0))
        self.sports_page.go_back.connect(lambda: self._go(0))
        self.tcg_page.go_back.connect(lambda: self._go(0))
        self.tcg_page.go_to_item_view.connect(lambda: self._go(4))
        self.item_page.go_back.connect(lambda: self._go(3))

        self.resize(1300, 900)
        self.window_title = self.page_titles[0]
        self.show()

    @Slot()
    def _go(self, index: int):
        self.stack.current_index = index
        self.window_title = self.page_titles[index]


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())