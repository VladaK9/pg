from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšáka (pouze pohyb vpřed bez braní).
        Bílý postupuje vpřed (row + 1), černý proti němu (row - 1).
        """
        row, col = self.position
        moves = []

        if self.color == 'white':
            moves.append((row + 1, col))
        elif self.color == 'black':
            moves.append((row - 1, col))

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce (diagonálně po celé šachovnici).
        """
        row, col = self.position
        moves = []
        # 4 diagonální směry: (změna řádku, změna sloupce)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            for step in range(1, 8):
                new_pos = (row + dr * step, col + dc * step)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže (horizontálně a vertikálně po celé šachovnici).
        """
        row, col = self.position
        moves = []
        # 4 ortogonální směry: nahoru, dolů, doprava, doleva
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for step in range(1, 8):
                new_pos = (row + dr * step, col + dc * step)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy (kombinace pohybů věže a střelce).
        """
        row, col = self.position
        moves = []
        # Všech 8 směrů (ortogonální i diagonální)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            for step in range(1, 8):
                new_pos = (row + dr * step, col + dc * step)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále (o 1 pole do všech 8 směrů).
        """
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Ukázka testování jednotlivých figurek
    pieces = [
        Pawn("white", (1, 2)),
        Pawn("black", (5, 4)),
        Knight("black", (1, 2)),
        Bishop("white", (4, 4)),
        Rook("black", (1, 1)),
        Queen("white", (4, 4)),
        King("black", (8, 8))
    ]

    for piece in pieces:
        print(piece)
        print("Možné tahy:", piece.possible_moves())
        print("-" * 40)