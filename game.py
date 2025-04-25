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

    def switch_turn(self):
        """Troca o turno entre as cores."""
        self.turn = 'black' if self.turn == 'white' else 'white'

    def is_valid_move(self, i, j, piece):
        """Verifica se o movimento é válido."""
        if not (0 <= i < 8 and 0 <= j < 8):  # Verifica se está dentro do tabuleiro
            return False
        if self.board[i][j] is None:  # Se a casa estiver vazia, é um movimento válido
            return True
        if self.board[i][j].color != piece.color:  # Se a casa estiver ocupada por uma peça adversária
            return True
        return False

    def move_piece(self, i, j):
        """Move a peça e captura, se necessário."""
        if self.selected_piece:
            current_x, current_y = self.selected_piece.position
            if self.is_valid_move(i, j, self.selected_piece):
                # Captura a peça adversária
                if self.board[i][j] is not None and self.board[i][j].color != self.selected_piece.color:
                    self.board[i][j] = None  # Remove a peça adversária

                # Move a peça para a nova casa
                self.board[i][j] = self.selected_piece
                self.board[current_x][current_y] = None
                self.selected_piece.position = (i, j)  # Atualiza a posição da peça

                self.switch_turn()  # Troca o turno após a jogada
                self.selected_piece = None  # Reseta a peça selecionada
                return True
        return False
    def get_valid_moves(self, i, j):
        piece = self.board[i][j]  # Assuming this is how you get the piece from the board
        if piece is None:  # Check if the piece exists
            return []  # Return an empty list or whatever is appropriate for no piece
        if piece.get_type() == 'pawn':
            valid_moves = self.get_pawn_moves(i, j, piece)
        elif piece.get_type() == 'rook':
            valid_moves = self.get_rook_moves(i, j, piece)
        elif piece.get_type() == 'knight':
            valid_moves = self.get_knight_moves(i, j, piece)
        elif piece.get_type() == 'bishop':
            valid_moves = self.get_bishop_moves(i, j, piece)
        elif piece.get_type() == 'queen':
            valid_moves = self.get_queen_moves(i, j, piece)
        elif piece.get_type() == 'king':
            valid_moves = self.get_king_moves(i, j, piece)
        return valid_moves

    def get_pawn_moves(self, i, j, piece):
        """Calcula os movimentos do peão."""
        direction = 1 if piece.color == 'white' else -1
        moves = []
        # Movimento para frente
        if 0 <= i + direction < 8 and self.board[i + direction][j] is None:
            moves.append((i + direction, j))
        # Captura na diagonal
        if 0 <= i + direction < 8:
            if 0 <= j + 1 < 8 and self.board[i + direction][j + 1] and self.board[i + direction][j + 1].color != piece.color:
                moves.append((i + direction, j + 1))
            if 0 <= j - 1 < 8 and self.board[i + direction][j - 1] and self.board[i + direction][j - 1].color != piece.color:
                moves.append((i + direction, j - 1))
        return moves

    def get_rook_moves(self, i, j, piece):
        """Obtém os movimentos válidos para a torre."""
        moves = []
        for x in range(i + 1, 8):  # Movimento para baixo
            if self.board[x][j] is None:
                moves.append((x, j))
            else:
                if self.board[x][j].color != piece.color:
                    moves.append((x, j))  # Come a peça adversária
                break
        for x in range(i - 1, -1, -1):  # Movimento para cima
            if self.board[x][j] is None:
                moves.append((x, j))
            else:
                if self.board[x][j].color != piece.color:
                    moves.append((x, j))  # Come a peça adversária
                break
        for y in range(j + 1, 8):  # Movimento para a direita
            if self.board[i][y] is None:
                moves.append((i, y))
            else:
                if self.board[i][y].color != piece.color:
                    moves.append((i, y))  # Come a peça adversária
                break
        for y in range(j - 1, -1, -1):  # Movimento para a esquerda
            if self.board[i][y] is None:
                moves.append((i, y))
            else:
                if self.board[i][y].color != piece.color:
                    moves.append((i, y))  # Come a peça adversária
                break
        return moves

    def get_knight_moves(self, i, j, piece):
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
                if self.board[x][y] is None or self.board[x][y].color != piece.color:
                    valid_moves.append((x, y))
        return valid_moves

    def get_bishop_moves(self, i, j, piece):
        """Obtém os movimentos válidos para o bispo."""
        moves = []
        # Movimento diagonal para baixo à direita
        for x, y in zip(range(i + 1, 8), range(j + 1, 8)):
            if self.board[x][y] is None:
                moves.append((x, y))
            elif self.board[x][y].color != piece.color:
                moves.append((x, y))  # Come a peça adversária
                break
            else:
                break
        # Movimento diagonal para baixo à esquerda
        for x, y in zip(range(i + 1, 8), range(j - 1, -1, -1)):
            if self.board[x][y] is None:
                moves.append((x, y))
            elif self.board[x][y].color != piece.color:
                moves.append((x, y))  # Come a peça adversária
                break
            else:
                break
        # Movimento diagonal para cima à direita
        for x, y in zip(range(i - 1, -1, -1), range(j + 1, 8)):
            if self.board[x][y] is None:
                moves.append((x, y))
            elif self.board[x][y].color != piece.color:
                moves.append((x, y))  # Come a peça adversária
                break
            else:
                break
        # Movimento diagonal para cima à esquerda
        for x, y in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
            if self.board[x][y] is None:
                moves.append((x, y))
            elif self.board[x][y].color != piece.color:
                moves.append((x, y))  # Come a peça adversária
                break
            else:
                break
        return moves

    def get_queen_moves(self, i, j, piece):
        """Obtém os movimentos válidos para a rainha."""
        return self.get_rook_moves(i, j, piece) + self.get_bishop_moves(i, j, piece)

    def get_king_moves(self, i, j, piece):
        """Obtém os movimentos válidos para o rei."""
        moves = [
            (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)
        ]
        valid_moves = []
        for x, y in moves:
            if 0 <= x < 8 and 0 <= y < 8:
                if self.board[x][y] is None or self.board[x][y].color != piece.color:
                    valid_moves.append((x, y))
        return valid_moves
