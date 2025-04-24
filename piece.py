# piece.py

class Piece:
    def __init__(self, color, type_):
        self.color = color  # 'white' ou 'black'
        self.type = type_   # Tipo de peça, por exemplo: 'pawn', 'rook', 'knight', 'queen', 'king', 'bishop'

    def __repr__(self):
        return f"{self.color} {self.type}"

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_symbol(self):
        """Retorna o símbolo da peça para exibição no tabuleiro"""
        piece_symbols = {
            'pawn': '♙' if self.color == 'white' else '♟',
            'rook': '♖' if self.color == 'white' else '♜',
            'knight': '♘' if self.color == 'white' else '♞',
            'bishop': '♗' if self.color == 'white' else '♝',
            'queen': '♕' if self.color == 'white' else '♛',
            'king': '♔' if self.color == 'white' else '♚',
        }
        return piece_symbols.get(self.type, '')
