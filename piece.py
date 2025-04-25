# piece.py

class Piece:
    def __init__(self, color, type_):
        self.color = color
        self.type = type_

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type