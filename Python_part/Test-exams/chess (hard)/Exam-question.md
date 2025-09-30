# Question

### Chessboard Analysis

You are given a text file representation of a chessboard, where each row contains 8 space-separated characters.  
- Uppercase letters (`KQRBNP`) represent **white pieces**.  
- Lowercase letters (`kqrbnp`) represent **black pieces**.  
- A dot (`.`) represents an empty square.  

For example, the file `chess.txt` 


---

## Your Task

Design two Python classes:

### 1. `ChessBoardManager`
This class should:
- Load the chessboard from a text file and ensure it is **8×8**.  
- Provide the following methods:
  - `count_pieces(color)`: Returns the total number of pieces for `"white"` or `"black"`.  
  - `piece_positions(piece)`: Returns the coordinates `(row, col)` of all occurrences of a given piece.  
  - `is_square_attacked(row, col, color)`: Returns `True` if the given square is attacked by the specified color.  
  - `king_in_check(color)`: Returns `True` if the king of the given color is in check.  
  - `material_balance()`: Computes the difference in material values (using standard piece values: pawn=1, knight=3, bishop=3, rook=5, queen=9). Kings are excluded from scoring.  
    - A positive score means White is ahead.  
    - A negative score means Black is ahead.  

### 2. `ReportGenerator`
This class should:
- Be initialized with a `ChessBoardManager` object.  
- Provide a method `generate_report()` that prints:  
  - The number of white and black pieces.  
  - The positions of both kings.  
  - Whether each king is in check.  
  - The material balance.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code using the provided `chess.txt` starting position.  


---
