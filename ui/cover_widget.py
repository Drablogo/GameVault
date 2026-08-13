from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QPainter,
    QPainterPath,
    QPixmap,
    QImage
)
from PyQt6.QtWidgets import QLabel


class CoverWidget(QLabel):

    def __init__(self):
        super().__init__()

        self.setFixedSize(350, 580)

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.setStyleSheet("""
            QLabel {
                background-color: #333333;
                border-radius: 15px;
            }
        """)

    def set_cover(self, path: str):

        pixmap = QPixmap(path)

        if pixmap.isNull():

            self.setText("No Cover")
            self.setPixmap(QPixmap())

            return

        # =========================
        # REDIMENSIONAR
        # =========================

        pixmap = pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        # =========================
        # CRIAR IMAGEM TRANSPARENTE
        # =========================

        image = QImage(
            self.size(),
            QImage.Format.Format_ARGB32
        )

        image.fill(
            Qt.GlobalColor.transparent
        )

        # =========================
        # DESENHAR COM CANTOS
        # ARREDONDADOS
        # =========================

        painter = QPainter(image)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setRenderHint(
            QPainter.RenderHint.SmoothPixmapTransform
        )

        path = QPainterPath()

        path.addRoundedRect(
            0,
            0,
            self.width(),
            self.height(),
            15,
            15
        )

        painter.setClipPath(path)

        # =========================
        # CENTRALIZAR IMAGEM
        # =========================

        x = (
            pixmap.width() - self.width()
        ) // 2

        y = (
            pixmap.height() - self.height()
        ) // 2

        painter.drawPixmap(
            0,
            0,
            pixmap,
            x,
            y,
            self.width(),
            self.height()
        )

        painter.end()

        # =========================
        # MOSTRAR
        # =========================

        self.setText("")

        self.setPixmap(
            QPixmap.fromImage(image)
        )