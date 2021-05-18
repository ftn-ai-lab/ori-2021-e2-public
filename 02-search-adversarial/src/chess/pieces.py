from abc import *


def valid_position(position, board):
    [row, col] = position
    return 0 <= row <= board.rows - 1 and 0 <= col <= board.cols - 1

opposite_size = {
    'b': 'w',
    'w': 'b'
}

class Piece(object):
    """
    Apstraktna klasa za sahovske figure.
    """
    def __init__(self, board, row, col, side):
        self.board = board
        self.row = row
        self.col = col
        self.side = side

    @abstractmethod
    def get_legal_moves(self):
        """
        Apstraktna metoda koja treba da za konkretnu figuru vrati moguce sledece poteze (pozicije).
        """
        pass

    def get_value(self):
        """
        Vrednost figure modifikovana u odnosu na igraca.
        Figure crnog (MAX igrac) imaju pozivitnu vrednost, a belog (MIN igrac) negativnu.
        :return: float
        """
        return self.get_value_() if self.side == 'b' else self.get_value_() * -1.

    @abstractmethod
    def get_value_(self):
        """
        Apstraktna metoda koja treba da vrati vrednost za konkretnu figuru.
        """
        pass


class Pawn(Piece):
    """
    Pijun
    """

    def get_legal_moves(self):
        row = self.row
        col = self.col
        side = self.side
        legal_moves = []
        d_rows = []
        d_cols = []

        if side == 'w':  # beli pijun
            # jedan unapred, ako je polje prazno
            if row > 0 and self.board.data[row-1][col] == '.':
                d_rows.append(-1)
                d_cols.append(0)
            # dva unapred, ako je pocetna pozicija i ako je polje prazno
            if row == self.board.rows - 2 and self.board.data[row-1][col] == '.' and self.board.data[row-2][col] == '.':
                d_rows.append(-2)
                d_cols.append(0)
            # ukoso levo, jede crnog
            if col > 0 and row > 0 and self.board.data[row-1][col-1].startswith('b'):
                d_rows.append(-1)
                d_cols.append(-1)
            # ukoso desno, jede crnog
            if col < self.board.cols - 1 and row > 0 and self.board.data[row-1][col+1].startswith('b'):
                d_rows.append(-1)
                d_cols.append(1)
        else:  # crni pijun
            # jedan unapred, ako je polje prazno
            if row < self.board.rows - 1 and self.board.data[row+1][col] == '.':
                d_rows.append(+1)
                d_cols.append(0)
            # dva unapred, ako je pocetna pozicija i ako je polje prazno
            if row ==  1 and self.board.data[row+1][col] == '.' and self.board.data[row + 2][col] == '.':
                d_rows.append(+2)
                d_cols.append(0)
            # ukoso levo, jede crnogç
            if col < self.board.cols - 1 and row < self.board.rows - 1 and self.board.data[row+1][col+1].startswith('w'):
                d_rows.append(+1)
                d_cols.append(+1)
            # ukoso desno, jede crnog
            if col > 0 and row < self.board.rows - 1 and self.board.data[row+1][col-1].startswith('w'):
                d_rows.append(+1)
                d_cols.append(-1)

        for d_row, d_col in zip(d_rows, d_cols):
                new_row = row + d_row
                new_col = col + d_col
                if 0 <= new_row < self.board.rows and 0 <= new_col < self.board.cols:
                    legal_moves.append((new_row, new_col))

        return legal_moves

    def get_value_(self):
        return 1.  # pijun ima vrednost 1


class Knight(Piece):
    """
    Konj
    """
    def get_legal_moves(self):
        row = self.row
        col = self.col
        side = self.side
        legal_moves = []

        steps = range(0, self.board.rows)
        directions = [(2,1), (2,-1), (-2, 1), (-2, -1), (1,2), (-1,2), (1, -2), (-1 ,-2)]

        for (d_row, d_col) in directions:
            cur_row = row + d_row
            cur_col = col + d_col
            temp_position = [cur_row, cur_col]
            if valid_position(temp_position, self.board):
                opposite_piece = self.board.data[cur_row][cur_col].startswith(opposite_size[side])
                blank_field = self.board.data[cur_row][cur_col] == '.'
                if opposite_piece or blank_field:
                    legal_moves.append((cur_row, cur_col))
        
        return legal_moves

    def get_value_(self):
        return 3


class Bishop(Piece):
    """
    Lovac
    """
    def get_legal_moves(self):
        row = self.row
        col = self.col
        side = self.side
        legal_moves = []

        steps = range(0, self.board.rows)
        directions = [(1,1), (-1,-1), (1, -1), (-1, 1)]

        for (d_row, d_col) in directions:
            cur_row = row
            cur_col = col
            for step in steps:
                cur_row += d_row
                cur_col += d_col
                temp_position = [cur_row, cur_col]
                if valid_position(temp_position, self.board):
                    opposite_piece = self.board.data[cur_row][cur_col].startswith(opposite_size[side])
                    blank_field = self.board.data[cur_row][cur_col] == '.'
                    if opposite_piece or blank_field:
                        legal_moves.append((cur_row, cur_col))
                    if opposite_piece:
                        break
                    if self.board.data[cur_row][cur_col].startswith(side):
                        break
                else:
                    break
        
        return legal_moves

    def get_value_(self):
        return 3


class Rook(Piece):
    """
    Top
    """
    def get_legal_moves(self):
        row = self.row
        col = self.col
        side = self.side
        legal_moves = []

        steps = range(0, self.board.rows)
        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        for (d_row, d_col) in directions:
            cur_row = row
            cur_col = col
            for step in steps:
                cur_row += d_row
                cur_col += d_col
                temp_position = [cur_row, cur_col]
                if valid_position(temp_position, self.board):
                    opposite_piece = self.board.data[cur_row][cur_col].startswith(opposite_size[side])
                    blank_field = self.board.data[cur_row][cur_col] == '.'
                    if opposite_piece or blank_field:
                        legal_moves.append((cur_row, cur_col))
                    if opposite_piece:
                        break
                    if self.board.data[cur_row][cur_col].startswith(side):
                        break
                else:
                    break
        
        return legal_moves

    def get_value_(self):
        return 5


class Queen(Piece):
    """
    Kraljica
    """
    def get_legal_moves(self):
        row = self.row
        col = self.col
        side = self.side
        legal_moves = []

        steps = range(0, self.board.rows)
        directions = [(1,0), (0,1), (-1,0), (0, -1), (1,1), (-1,-1), (1, -1), (-1, 1)]

        for (d_row, d_col) in directions:
            cur_row = row
            cur_col = col
            for step in steps:
                cur_row += d_row
                cur_col += d_col
                temp_position = [cur_row, cur_col]
                if valid_position(temp_position, self.board):
                    opposite_piece = self.board.data[cur_row][cur_col].startswith(opposite_size[side])
                    blank_field = self.board.data[cur_row][cur_col] == '.'
                    if opposite_piece or blank_field:
                        legal_moves.append((cur_row, cur_col))
                    if opposite_piece:
                        break
                    if self.board.data[cur_row][cur_col].startswith(side):
                        break
                else:
                    break
        
        return legal_moves


    def get_value_(self):
        return 9


class King(Piece):
    """
    Kralj
    """
    def get_legal_moves(self):
        row = self.row
        col = self.col
        side = self.side
        legal_moves = []
        directions = [(1,1), (1,0), (0,1), (-1, -1), (0,-1), (-1, 0),(-1, 1), (1, -1)]
        
        for (d_row, d_col) in directions:
            cur_row = row + d_row
            cur_col = col + d_col
            temp_position = [cur_row, cur_col]
            if valid_position(temp_position, self.board):
                opposite_piece = self.board.data[cur_row][cur_col].startswith(opposite_size[side])
                blank_field = self.board.data[cur_row][cur_col] == '.'
                if opposite_piece or blank_field:
                    legal_moves.append((cur_row, cur_col))
                if opposite_piece:
                    break
        
        return legal_moves

    def get_value_(self):
        return 1000
