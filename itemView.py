from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Slot, Signal
from __feature__ import snake_case, true_property

class ItemViewPage(QWidget):
    go_back = Signal()

    def __init__(self, item_name="Item Name", item_description="Item description goes here."):
        super().__init__()

        # Main layout
        content_box = QVBoxLayout()

        # --- Header ---
        header_box = QHBoxLayout()
        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.on_back_clicked)
        header_box.add_widget(back_btn, alignment=Qt.AlignLeft, stretch=1)
        header_box.add_widget(QLabel("Item View"), alignment=Qt.AlignCenter, stretch=3)
        header_box.add_widget(QLabel(""), stretch=1)  # Spacer to balance the back button
        content_box.add_layout(header_box, stretch=1)

        # --- Item Name ---
        name_label = QLabel(item_name)
        name_label.alignment = Qt.AlignCenter
        name_label.set_style_sheet("font-size: 22px; font-weight: bold;")
        content_box.add_widget(name_label, stretch=1)

        # --- Item Description ---
        desc_label = QLabel(item_description)
        desc_label.alignment = Qt.AlignTop | Qt.AlignLeft
        desc_label.word_wrap = True
        desc_label.set_style_sheet("font-size: 14px; padding: 10px;")
        content_box.add_widget(desc_label, stretch=8)

        self.set_layout(content_box)
        self.resize(900, 600)
        # self.show()
    
    @Slot()
    def on_back_clicked(self):
        self.go_back.emit()