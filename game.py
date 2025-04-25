from piece import Piece

class Game:
    def __init__(self):
        self.turn = 'white'  # Turno inicial
        self.board = [[None for _ in range(8)] for _ in range(8)]  # Tabuleiro 8x8
        self.selected_piece = None
        self.valid_moves = []  # Movimentos válidos da peça selecionada

    def set_pieces(self):
        """Define as peças nas suas posições iniciais no tabuleiro."""
        # Peças brancas
        for i in range(8):
            for j in range(8):
                if i == 1:
                    self.board[i][j] = Piece('white', 'pawn')
                if i == 0:
                    if j == 0 or j == 7:
                        self.board[i][j] = Piece('white', 'rook')
                    if j == 1 or j == 6:
                        self.board[i][j] = Piece('white', 'knight')
                    if j == 2 or j == 5:
                        self.board[i][j] = Piece('white', 'bishop')
                    if j == 3:
                        self.board[i][j] = Piece('white', 'queen')
                    if j == 4:
                        self.board[i][j] = Piece('white', 'king')

        # Peças pretas
        for i in range(8):
            for j in range(8):
                if i == 6:
                    self.board[i][j] = Piece('black', 'pawn')
                if i == 7:
                    if j == 0 or j == 7:
                        self.board[i][j] = Piece('black', 'rook')
                    if j == 1 or j == 6:
                        self.board[i][j] = Piece('black', 'knight')
                    if j == 2 or j == 5:
                        self.board[i][j] = Piece('black', 'bishop')
                    if j == 3:
                        self.board[i][j] = Piece('black', 'queen')
                    if j == 4:
                        self.board[i][j] = Piece('black', 'king')