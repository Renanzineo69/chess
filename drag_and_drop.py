# drag_and_drop.py

from PyQt5.QtCore import Qt

class DragAndDrop:
    def __init__(self, game_controller, board, squares):
        self.game_controller = game_controller
        self.board = board
        self.squares = squares
        self.selected_piece = None  # A peça que está sendo arrastada
        self.selected_square = None  # A casa que foi clicada para a peça
        self.valid_moves = []  # Casas válidas onde a peça pode se mover
        self.game_controller = game_controller  # Controlador do jogo (responsável pela alternância entre jogadores)

    def mousePressEvent(self, event):
        """Inicia o drag-and-drop de uma peça"""
        if event.button() == Qt.LeftButton:
            for i in range(8):
                for j in range(8):
                    label = self.squares[i][j]
                    if label.geometry().contains(event.pos()):
                        piece = self.board[i][j]
                        if piece and piece.get_color() == self.game_controller.turn:
                            self.selected_piece = piece
                            self.selected_square = (i, j)
                            self.show_valid_moves(i, j)  # Exibe as casas válidas para a peça
                            break

    def mouseMoveEvent(self, event):
        """Movimenta a peça enquanto ela é arrastada"""
        if self.selected_piece is not None:
            # Aqui, você pode adicionar lógica para mover visualmente a peça durante o arraste.
            # Usando QPixmap para a peça.
            pass

    def mouseReleaseEvent(self, event):
        """Libera a peça no tabuleiro após o movimento"""
        if self.selected_piece is not None:
            for i in range(8):
                for j in range(8):
                    if self.squares[i][j].geometry().contains(event.pos()):
                        if (i, j) in self.valid_moves:
                            self.move_piece(i, j)
            self.clear_highlights()

    def show_valid_moves(self, i, j):
        """Exibe as casas válidas para onde a peça pode ir"""
        self.valid_moves.clear()  # Limpa as casas válidas anteriores
        # Lógica simples para o peão, você pode expandir para as outras peças
        if self.selected_piece.get_type() == 'pawn':
            direction = 1 if self.selected_piece.get_color() == 'white' else -1
            if 0 <= i + direction < 8:
                if not self.board[i + direction][j]:
                    self.valid_moves.append((i + direction, j))

    def move_piece(self, i, j):
        """Movimenta a peça para a casa selecionada"""
        if self.selected_square:
            x, y = self.selected_square
            self.board[i][j] = self.selected_piece
            self.board[x][y] = None
            self.selected_piece = None
            self.selected_square = None
            self.game_controller.update_display()
            self.game_controller.switch_turn()  # Alterna o turno