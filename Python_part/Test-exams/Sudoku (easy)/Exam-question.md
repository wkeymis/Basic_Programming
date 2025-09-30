# Question

### Sudoku Board Analysis

You are asked to manage and analyze a 9×9 Sudoku board stored in a text file.  
The board uses `0` to represent empty cells. For example, `sudoku.txt`.


---

## Your Task

Design two Python classes:

### 1. `SudokuManager`
This class should:
- Read the Sudoku board from the file.  
- Provide the following methods:
  - `count_empty()`: Returns the number of empty cells (`0`).  
  - `row_sum(row)`: Returns the sum of the values in the specified row.  
  - `is_valid_row(row)`: Returns `True` if the row contains no duplicates (ignoring zeros) and all numbers are 1–9.  
  - `column_values(col)`: Returns a set of all values in the specified column.  
  - `find_max_in_subgrid(row, col)`: Returns the maximum value in the 3×3 subgrid starting at `(row, col)`; only valid for `(0,0)`, `(0,3)`, `(0,6)`, `(3,0)`, etc.

### 2. `ReportGenerator`
This class should:
- Be initialized with a `SudokuManager` object.  
- Provide a method `generate_report()` that:
  - Prints the number of empty cells.  
  - Prints the sums of row 0 and row 1.  
  - Prints the validity status of each row.  
  - Prints all values in column 0.  
  - Prints the maximum value in the top-left subgrid `(0,0)`.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate the code using the provided `sudoku.txt`.  
3. Generate a report showing:
   - Number of empty cells  
   - Row sums  
   - Row validity  
   - Column values  
   - Maximum value in subgrid  

---
