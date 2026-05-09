# image_filter_app.py

import sys
import random
import math
from pathlib import Path

from PIL import Image

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Slot

from __feature__ import snake_case, true_property


'''
The image manipulation is performed on top of the previous manipulation
So, we can apply Random and then preform a Negative on top of that
Until we hit the restart button
'''

class ImageFilterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = "Image of the Day Filter"

        # Image paths
        #TODO: Change test.jpg to Image of the Day after we get web scraped data
        self.original_path = Path("test.jpg")
        self.temp_path = Path("temp.jpg")

        # Make sure temp.jpg starts as a copy of original.jpg
        self.reset_image()

        # Main layout -------------
        main_layout = QVBoxLayout()

        # Title
        title = QLabel("Image of the Day Filter")
        title.alignment = Qt.AlignCenter
        title.set_style_sheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                margin: 15px;
            }
        """)
        main_layout.add_widget(title)

        # Image display layout -------------
        image_layout = QHBoxLayout()

        # Left side: Original image
        original_box = QVBoxLayout()

        original_title = QLabel("Original")
        original_title.alignment = Qt.AlignCenter
        original_title.set_style_sheet("font-size: 20px; font-weight: bold;")

        self.original_label = QLabel()
        self.original_label.alignment = Qt.AlignCenter

        original_box.add_widget(original_title)
        original_box.add_widget(self.original_label)

        # Right side: Manipulated image
        filtered_box = QVBoxLayout()

        self.filtered_title = QLabel("Filtered")
        self.filtered_title.alignment = Qt.AlignCenter
        self.filtered_title.set_style_sheet("font-size: 20px; font-weight: bold;")

        self.filtered_label = QLabel()
        self.filtered_label.alignment = Qt.AlignCenter

        filtered_box.add_widget(self.filtered_title)
        filtered_box.add_widget(self.filtered_label)

        image_layout.add_layout(original_box)
        image_layout.add_layout(filtered_box)

        main_layout.add_layout(image_layout)

        # ---------- Button layout ----------
        button_layout = QHBoxLayout()

        grayscale_btn = QPushButton("Grayscale")
        negative_btn = QPushButton("Negative")
        random_btn = QPushButton("Random")
        reset_btn = QPushButton("Reset")

        grayscale_btn.clicked.connect(self.apply_grayscale)
        negative_btn.clicked.connect(self.apply_negative)
        random_btn.clicked.connect(self.apply_random)
        reset_btn.clicked.connect(self.reset_clicked)

        button_layout.add_widget(grayscale_btn)
        button_layout.add_widget(negative_btn)
        button_layout.add_widget(random_btn)
        button_layout.add_widget(reset_btn)

        main_layout.add_layout(button_layout)

        self.set_layout(main_layout)
        self.resize(1000, 650)

        self.update_images()

        # Copies original.jpg into temp.jpg
    def reset_image(self):
        im = Image.open(self.original_path)
        im.save(self.temp_path)

        # Refreshes the QLabel image displays
    def update_images(self):
        original_pixmap = QPixmap(str(self.original_path))
        filtered_pixmap = QPixmap(str(self.temp_path))

        self.original_label.pixmap = original_pixmap.scaled(
            400,
            400,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        self.filtered_label.pixmap = filtered_pixmap.scaled(
            400,
            400,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        # Grayscale Image manipulation
    @Slot()
    def apply_grayscale(self):
        im = Image.open(self.temp_path).convert("RGB")

        new_list = [
            ((pixel[0] * 299 + pixel[1] * 587 + pixel[2] * 114) // 1000,) * 3
            for pixel in im.get_flattened_data()
        ]

        im.putdata(new_list)
        im.save(self.temp_path)

        self.filtered_title.text = "Grayscale"
        self.update_images()

        # Negative Image manipulation
    @Slot()
    def apply_negative(self):
        im = Image.open(self.temp_path).convert("RGB")

        new_list = [
            (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
            for pixel in im.get_flattened_data()
        ]

        im.putdata(new_list)
        im.save(self.temp_path)

        self.filtered_title.text = "Negative"
        self.update_images()

        # Random Image manipulation
    @Slot()
    def apply_random(self):
        im = Image.open(self.temp_path).convert("RGB")

        numR = random.uniform(0.2, 1)
        numG = random.uniform(0.2, 1)
        numB = random.uniform(0.2, 1)

        new_list = [
            (math.floor(numR * pixel[0]), math.floor(numG * pixel[1]), math.floor(numB * pixel[2]))
            for pixel in im.get_flattened_data()
        ]

        im.putdata(new_list)
        im.save(self.temp_path)

        self.filtered_title.text = "Random"
        self.update_images()

        # Revert Image manipulation to original
    @Slot()
    def reset_clicked(self):
        self.reset_image()
        self.filtered_title.text = "Filtered"
        self.update_images()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec())