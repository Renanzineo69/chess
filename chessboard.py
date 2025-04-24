# chessboard.py

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from piece import Piece

class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabuleiro de Xadrez")
        self.setGeometry(100, 100, 600, 600)
        self.layout = QGridLayout(self)

        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.init_board()

    def init_board(self):
        """Inicializa o tabuleiro de xadrez com peças no lugar correto"""
        for i in range(8):
            for j in range(8):
                square = QLabel(self)
                square.setStyleSheet(f"background-color: {'white' if (i + j) % 2 == 0 else 'black'}")
                square.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(square, i, j)

        self.set_pieces()

    def set_pieces(self):
        """Coloca as peças no tabuleiro"""
        # Peças brancas
        for i in range(8):
            self.board[1][i] = Piece('white', 'pawn')
        self.board[0][0] = Piece('white', 'rook')
        self.board[0][7] = Piece('white', 'rook')
        self.board[0][1] = Piece('white', 'knight')
        self.board[0][6] = Piece('white', 'knight')
        self.board[0][2] = Piece('white', 'bishop')
        self.board[0][5] = Piece('white', 'bishop')
        self.board[0][3] = Piece('white', 'queen')
        self.board[0][4] = Piece('white', 'king')

        # Peças pretas
        for i in range(8):
            self.board[6][i] = Piece('black', 'pawn')
        self.board[7][0] = Piece('black', 'rook')
        self.board[7][7] = Piece('black', 'rook')
        self.board[7][1] = Piece('black', 'knight')
        self.board[7][6] = Piece('black', 'knight')
        self.board[7][2] = Piece('black', 'bishop')
        self.board[7][5] = Piece('black', 'bishop')
        self.board[7][3] = Piece('black', 'queen')
        self.board[7][4] = Piece('black', 'king')

        # Atualiza os rótulos para mostrar as peças
        self.update_display()

    def update_display(self):
        """Atualiza os rótulos com os símbolos das peças"""
        for i in range(8):
            for j in range(8):
                square = self.layout.itemAtPosition(i, j).widget()
                piece = self.board[i][j]
                if piece:
                    square.setText(piece.get_symbol())
                else:
                    square.setText("")
