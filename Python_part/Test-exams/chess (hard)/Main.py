class ChessBoardManager:
    def __init__(self, filename):
        self.board = []
        with open(filename, "r") as f:
            for line in f:
                row = line.strip().split()
                if len(row) == 8:
                    self.board.append(row)
        if len(self.board) != 8:
            raise ValueError("Board must be 8x8")

    def count_pieces(self, color):
        white = "KQRBNP"
        black = "kqrbnp"
        total = 0
        for r in self.board:
            for c in r:
                if color == "white" and c in white:
                    total += 1
                if color == "black" and c in black:
                    total += 1
        return total

    def piece_positions(self, piece):
        positions = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == piece:
                    positions.append((i, j))
        return positions

    def is_square_attacked(self, row, col, color):
        white = color == "white"
        pawns = ["P", "p"]
        knights = ["N", "n"]
        bishops = ["B", "b"]
        rooks = ["R", "r"]
        queens = ["Q", "q"]
        kings = ["K", "k"]

        attackers = []
        if white:
            attackers = ["P", "N", "B", "R", "Q", "K"]
        else:
            attackers = ["p", "n", "b", "r", "q", "k"]

        # Pawn attacks
        if white and row > 0:
            if col > 0 and self.board[row-1][col-1] == "P": return True
            if col < 7 and self.board[row-1][col+1] == "P": return True
        if not white and row < 7:
            if col > 0 and self.board[row+1][col-1] == "p": return True
            if col < 7 and self.board[row+1][col+1] == "p": return True

        # Knight moves
        knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for dr, dc in knight_moves:
            r, c = row+dr, col+dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] in attackers and self.board[r][c].lower() == "n":
                return True

        # Directions for rooks/queens
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            r, c = row+dr, col+dc
            while 0 <= r < 8 and 0 <= c < 8:
                piece = self.board[r][c]
                if piece != ".":
                    if piece in attackers and (piece.lower()=="r" or piece.lower()=="q"):
                        return True
                    break
                r += dr
                c += dc

        # Directions for bishops/queens
        for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            r, c = row+dr, col+dc
            while 0 <= r < 8 and 0 <= c < 8:
                piece = self.board[r][c]
                if piece != ".":
                    if piece in attackers and (piece.lower()=="b" or piece.lower()=="q"):
                        return True
                    break
                r += dr
                c += dc

        # King (1 square)
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row+dr, col+dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] in attackers and self.board[r][c].lower()=="k":
                        return True

        return False

    def king_in_check(self, color):
        king_symbol = "K" if color=="white" else "k"
        king_pos = self.piece_positions(king_symbol)
        if not king_pos:
            return False
        row, col = king_pos[0]
        opponent = "black" if color=="white" else "white"
        return self.is_square_attacked(row, col, opponent)

    def material_balance(self):
        values = {"p":1,"n":3,"b":3,"r":5,"q":9}
        score = 0
        for row in self.board:
            for piece in row:
                if piece == "." or piece.lower()=="k":
                    continue
                val = values[piece.lower()]
                if piece.isupper():
                    score += val
                else:
                    score -= val
        return score


class ReportGenerator:
    def __init__(self, manager):
        self.manager = manager

    def generate_report(self):
        print("===== CHESS REPORT =====")
        print("White pieces:", self.manager.count_pieces("white"))
        print("Black pieces:", self.manager.count_pieces("black"))
        print("White king position:", self.manager.piece_positions("K"))
        print("Black king position:", self.manager.piece_positions("k"))
        print("White king in check:", self.manager.king_in_check("white"))
        print("Black king in check:", self.manager.king_in_check("black"))
        print("Material balance (positive = White ahead):", self.manager.material_balance())
        print("========================")


if __name__ == "__main__":
    manager = ChessBoardManager("chess.txt")
    reporter = ReportGenerator(manager)
    reporter.generate_report()
