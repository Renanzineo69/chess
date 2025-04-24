# ui.py

from PyQt5.QtWidgets import QMainWindow, QApplication
from chessboard import ChessBoard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Xadrez - Jogo")
        self.setGeometry(100, 100, 600, 600)

        self.chessboard = ChessBoard()
        self.setCentralWidget(self.chessboard)

    def show(self):
        super().show()

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
