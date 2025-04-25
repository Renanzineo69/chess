# chessboard.py

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from game import Game
class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabuleiro de Xadrez")
        self.setGeometry(100, 100, 600, 600)
        self.layout = QGridLayout(self)

        self.board = [[None for _ in range(8)] for _ in range(8)]  # Tabuleiro de 8x8
        self.squares = [[None for _ in range(8)] for _ in range(8)]  # Rótulos para as casas
        self.selected_piece = None  # A peça selecionada
        self.selected_square = None  # A casa selecionada
        self.turn = 'white'  # Turno inicial: branco começa
        self.valid_moves = []  # Listar movimentos válidos para a peça selecionada
        self.init_board()  # Inicializa o tabuleiro
        self.update_display()  # Atualiza o display com as peças

    def init_board(self):
        """Inicializa o tabuleiro com peças nas posições iniciais."""
        for i in range(8):
            for j in range(8):
                square = QLabel(self)
                square.setStyleSheet(f"background-color: {'#f0d9b5' if (i + j) % 2 == 0 else '#b58863'}")
                square.setAlignment(Qt.AlignCenter)
                square.setFixedSize(70, 70)
                square.mousePressEvent = lambda event, i=i, j=j: self.square_clicked(i, j, event)
                self.layout.addWidget(square, i, j)
                self.squares[i][j] = square

        Game.set_pieces(self)  # Coloca as peças no tabuleiro

    def update_display(self):
        """Atualiza o display do tabuleiro com as peças"""
        for i in range(8):
            for j in range(8):
                label = self.squares[i][j]
                piece = self.board[i][j]
                if piece:
                    icon_path = os.path.join("icons", f"{piece.color}_{piece.type}.png")
                    pixmap = QPixmap(icon_path).scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    label.setPixmap(pixmap)
                else:
                    label.clear()

    def square_clicked(self, i, j, event):
        """Aciona quando uma casa do tabuleiro é clicada."""
        piece = self.board[i][j]
        
        # Se a peça não estiver no turno do jogador atual, não faz nada
        if piece and piece.color != self.turn:
            return

        if self.selected_piece is None:  # Se nenhuma peça foi selecionada
            if piece:  # Se existe uma peça na casa
                self.selected_piece = piece
                self.selected_square = (i, j)
                self.show_valid_moves(i, j)  # Exibe movimentos válidos para a peça
        else:
            if (i, j) in self.valid_moves:  # Se o clique é uma casa válida para a peça
                self.move_piece(i, j)  # Move a peça
                self.switch_turn()  # Troca o turno após a jogada

        self.clear_highlights()  # Limpa os destaques após a jogada

    def show_valid_moves(self, i, j):
        """Exibe as casas válidas onde a peça pode se mover."""
        self.valid_moves = []  # Limpa as casas válidas
        piece = self.selected_piece
        if piece.get_type() == 'pawn':
            direction = 1 if piece.get_color() == 'white' else -1
            if 0 <= i + direction < 8:
                if not self.board[i + direction][j]:
                    self.valid_moves.append((i + direction, j))

        elif piece.get_type() == 'rook':
            self.valid_moves = self.get_rook_moves(i, j)

        elif piece.get_type() == 'knight':
            self.valid_moves = self.get_knight_moves(i, j)

        elif piece.get_type() == 'bishop':
            self.valid_moves = self.get_bishop_moves(i, j)

        elif piece.get_type() == 'queen':
            self.valid_moves = self.get_queen_moves(i, j)

        elif piece.get_type() == 'king':
            self.valid_moves = self.get_king_moves(i, j)

        # Destaca as casas válidas
        for move in self.valid_moves:
            x, y = move
            self.squares[x][y].setStyleSheet("background-color: yellow")  # Destaque em amarelo

    def get_rook_moves(self, i, j):
        """Obtém os movimentos válidos para a torre."""
        moves = []
        for x in range(i + 1, 8):  # Movimento para baixo
            if self.board[x][j] is None:
                moves.append((x, j))
            else:
                break
        for x in range(i - 1, -1, -1):  # Movimento para cima
            if self.board[x][j] is None:
                moves.append((x, j))
            else:
                break
        for y in range(j + 1, 8):  # Movimento para a direita
            if self.board[i][y] is None:
                moves.append((i, y))
            else:
                break
        for y in range(j - 1, -1, -1):  # Movimento para a esquerda
            if self.board[i][y] is None:
                moves.append((i, y))
            else:
                break
        return moves

    def get_knight_moves(self, i, j):
        """Obtém os movimentos válidos para o cavalo."""
        moves = [
            (i + 2, j + 1), (i + 2, j - 1),
            (i - 2, j + 1), (i - 2, j - 1),
            (i + 1, j + 2), (i + 1, j - 2),
            (i - 1, j + 2), (i - 1, j - 2)
        ]
        valid_moves = []
        for x, y in moves:
            if 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
        return valid_moves

    def get_bishop_moves(self, i, j):
        """Obtém os movimentos válidos para o bispo."""
        moves = []
        for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x_temp, y_temp = i, j
            while True:
                x_temp += x
                y_temp += y
                if 0 <= x_temp < 8 and 0 <= y_temp < 8:
                    if self.board[x_temp][y_temp] is None:
                        moves.append((x_temp, y_temp))
                    else:
                        break
                else:
                    break
        return moves

    def get_queen_moves(self, i, j):
        """Obtém os movimentos válidos para a rainha (combinação de torre e bispo)."""
        return self.get_rook_moves(i, j) + self.get_bishop_moves(i, j)

    def get_king_moves(self, i, j):
        """Obtém os movimentos válidos para o rei (movimento de uma casa ao redor)."""
        moves = [
            (i + 1, j), (i - 1, j),
            (i, j + 1), (i, j - 1),
            (i + 1, j + 1), (i + 1, j - 1),
            (i - 1, j + 1), (i - 1, j - 1)
        ]
        valid_moves = []
        for x, y in moves:
            if 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
        return valid_moves

    def move_piece(self, i, j):
        """Move a peça selecionada para a casa clicada."""
        if self.selected_square:
            x, y = self.selected_square
            # Atualiza o tabuleiro
            self.board[i][j] = self.selected_piece
            self.board[x][y] = None

            # Atualiza a exibição das peças
            self.update_display()

            # Limpa a peça selecionada e os destaques
            self.selected_piece = None
            self.selected_square = None
            self.clear_highlights()

    def clear_highlights(self):
        """Limpa os destaques de movimento válidos."""
        for i in range(8):
            for j in range(8):
                self.squares[i][j].setStyleSheet(f"background-color: {'#f0d9b5' if (i + j) % 2 == 0 else '#b58863'}")

    def switch_turn(self):
        """Alterna o turno entre os jogadores."""
        self.turn = 'black' if self.turn == 'white' else 'white'