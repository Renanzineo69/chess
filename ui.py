# ui.py

from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from chessboard import ChessBoard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Xadrez - Jogo")
        self.setFixedSize(600, 600)

        self.chessboard = ChessBoard()
        self.setCentralWidget(self.chessboard)

        self.center()

    def center(self):
        """Centraliza a janela na tela"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show(self):
        super().show()

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()