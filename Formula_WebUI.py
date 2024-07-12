import sys
import fitz
import pytesseract
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QEvent, QBuffer, QRect
from PyQt5.QtGui import QPixmap, QImage, QGuiApplication, QPalette, QColor, QPainter, QPen
from io import BytesIO
from PIL import Image
from pix2tex.cli import LatexOCR


class CustomLabel(QLabel):
    def __init__(self, parent=None, main_window=None):
        super(CustomLabel, self).__init__(parent)
        self.main_window = main_window
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.clear_rect_requested = False

    def mousePressEvent(self, event):
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseMoveEvent(self, event):
        if self.start_x is not None and self.start_y is not None:
            self.end_x = event.x()
            self.end_y = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        self.end_x = event.x()
        self.end_y = event.y()
        if self.main_window:
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        
        if self.start_x is not None and self.start_y is not None and self.end_x is not None and self.end_y is not None:
            if self.clear_rect_requested:
                self.clear_drawn_rect(painter)  
            else:
                self.drawrect(painter) 

    def drawrect(self, painter):
        painter.setPen(QPen(Qt.red, 1))
        painter.drawRect(QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y))

    def clear_drawn_rect(self, painter):
        painter.setPen(QPen(Qt.white, 3))
        painter.drawRect(QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y))
        self.clear_rect_requested = False

    def clear_rect(self):
        self.clear_rect_requested = True
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 3))
        painter.drawRect(QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y))
        self.update()

    def clear_xy(self):
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.update()


class PDFToImageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_page = 0
        self.images = []
        self.scale_factor = 0.5
        self.start_pos = None
        self.end_pos = None
        self.model = LatexOCR()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PDF to Image Converter')
        self.setGeometry(300, 300, 1000, 900)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.scroll_area = QScrollArea(self)
        self.central_widget.setLayout(QVBoxLayout())
        self.central_widget.layout().addWidget(self.scroll_area)

        self.image_label = CustomLabel(self.scroll_area, self)
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setWidgetResizable(True)

        self.prev_button = QPushButton('Previous', self)
        self.next_button = QPushButton('Next', self)
        self.zoom_in_button = QPushButton('Zoom In', self)
        self.zoom_out_button = QPushButton('Zoom Out', self)
        self.copy_button = QPushButton('Copy Text', self)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        button_layout.addWidget(self.zoom_in_button)
        button_layout.addWidget(self.zoom_out_button)
        button_layout.addWidget(self.copy_button)

        self.central_widget.layout().addLayout(button_layout)

        self.prev_button.clicked.connect(self.previous_page)
        self.next_button.clicked.connect(self.next_page)
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.copy_button.clicked.connect(self.copy_text)

        self.result_label = QLabel(self)
        self.central_widget.layout().addWidget(self.result_label)

        self.setAcceptDrops(True)
        self.image_label.installEventFilter(self)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.image_label.setPalette(palette)
        self.image_label.setAutoFillBackground(True)

    def convert_pdf_to_images(self, pdf_path):
        images = []
        pdf_document = fitz.open(pdf_path)
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            image = page.get_pixmap(matrix=fitz.Matrix(3, 3))
            images.append(image)
        pdf_document.close()
        return images

    def display_page(self, page_number):
        if 0 <= page_number < len(self.images):
            image = self.images[page_number]
            qimage = QImage(image.samples, image.width, image.height, image.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            scaled_pixmap = pixmap.scaled(
                int(pixmap.width() * self.scale_factor),
                int(pixmap.height() * self.scale_factor),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def process_ocr(self, image_data):
        image = Image.open(BytesIO(image_data))
        ocr_text = self.model(image) 
        self.result_label.setWordWrap(True)
        self.result_label.setText(ocr_text)

    def copy_text(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.result_label.text())

    def previous_page(self):
        self.current_page -= 1
        if self.current_page < 0:
            self.current_page = 0
        self.display_page(self.current_page)

    def next_page(self):
        self.current_page += 1
        if self.current_page >= len(self.images):
            self.current_page = len(self.images) - 1
        self.display_page(self.current_page)

    def zoom_in(self):
        self.scale_factor += 0.1
        self.display_page(self.current_page)

    def zoom_out(self):
        self.scale_factor -= 0.1
        if self.scale_factor < 0.1:
            self.scale_factor = 0.1
        self.display_page(self.current_page)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith('.pdf'):
                self.images = self.convert_pdf_to_images(file_path)
                if self.images:
                    self.display_page(self.current_page)

    def eventFilter(self, obj, event):
        if obj is self.image_label:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.start_pos = event.pos()
            elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.end_pos = event.pos()
                self.capture_area()
        return super().eventFilter(obj, event)
    
    def clear_rect(self):
        self.image_label.clear_rect()
        self.image_label.clear_xy()
        self.update()


    def capture_area(self):
        if self.images and 0 <= self.current_page < len(self.images) and self.start_pos and self.end_pos:
            x = min(self.start_pos.x(), self.end_pos.x()) + 1
            y = min(self.start_pos.y(), self.end_pos.y()) + 1
            width = abs(self.start_pos.x() - self.end_pos.x()) - 1
            height = abs(self.start_pos.y() - self.end_pos.y()) - 1

            self.clear_rect() 

            screenshot = QApplication.primaryScreen().grabWindow(self.image_label.winId())
            screenshot = screenshot.copy(x, y, width, height)
            screenshot = screenshot.toImage()

            buffer = QBuffer()
            buffer.open(QBuffer.ReadWrite)
            screenshot.save(buffer, "PNG")
            image_data = buffer.data()

            self.process_ocr(image_data)

            self.start_pos = None
            self.end_pos = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_to_image_app = PDFToImageApp()
    pdf_to_image_app.show()
    sys.exit(app.exec_())
