from scipy.interpolate import griddata


class SudokuManager:
    def __init__(self, filename):
        self.board = []

        with open(filename, "r") as file:

            for line in file:
                line = line.strip()
                parts = line.split()

                row = []
                for p in parts:
                    value = int(p)
                    row.append(value)
                self.board.append(row)

    def count_empty(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    count += 1
        return count

    def row_sum(self, row):
        total = 0
        for value in self.board[row]:
            total += value
        return total

    def is_valid_row(self, row):
        if row < 0 or row > 8:
            raise IndexError("Row index out of range")

        seen = set()
        for value in self.board[row]:
            if value == 0:
                continue
            elif value < 1 or value > 9:
                return False
            elif value in seen:
                return False
            else:
                seen.add(value)
        return True

    def column_values(self, col):
        if col < 0 or col > 8:
            raise IndexError
        values = set()
        for i in range(9):
            values.add(self.board[i][col])
        return values

    def find_max_in_subgrid(self, row, col):
        if row not in (0,3,6) or col not in (0,3,6):
            raise IndexError

        max_val = -1
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                val = self.board[i][j]
                if val > max_val:
                    max_val = val
        return max_val

class ReportGenerator:
    def __init__(self, manager):
        self.manager = manager

    def generate_report(self):
        print("===== SUDOKU REPORT =====")

        empty = self.manager.count_empty()
        print("Empty cells:", empty)

        # Print sums for row 0 and row 1
        sum0 = self.manager.row_sum(0)
        sum1 = self.manager.row_sum(1)
        print("Row 0 sum:", sum0)
        print("Row 1 sum:", sum1)

        # Row validity
        print("Row validity:")
        for r in range(9):
            valid = self.manager.is_valid_row(r)
            status = "valid" if valid else "invalid"
            print(f"  Row {r}: {status}")

        # Column 0 values
        col0_vals = self.manager.column_values(0)
        print("Column 0 values:", col0_vals)

        # Max in top-left subgrid (0,0)
        max_sub = self.manager.find_max_in_subgrid(0, 0)
        print("Max in subgrid (0,0):", max_sub)

        print("=========================")


manager = SudokuManager("sudoku.txt")
reporter = ReportGenerator(manager)
reporter.generate_report()








