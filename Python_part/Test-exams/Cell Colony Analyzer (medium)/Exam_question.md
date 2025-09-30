# Question

### Colony Image Analysis

You are working with digital microscopy images of bacterial colonies that have been **converted into CSV-like text files**.  
Each pixel in the image is represented as an RGB triplet (`R,G,B`), separated by spaces within a row, and each row represents a horizontal line of the image.  

For example, the file `colonies.csv` 


---

## Your Task

Design two Python classes:

### 1. `ColonyAnalyser`
This class should:
- Read in the grid of RGB values from a file.  
- Provide the following methods:
  - `count_red_colonies(threshold=50)`: Counts the number of pixels where the red component is at least `threshold`, and also at least twice the green component, and greater than the blue component.  
  - `dominantly_color(color)`: Returns `True` if **at least half the pixels** are dominantly of the given color (`"red"`, `"green"`, or `"blue"`).  
  - `largest_red_block()`: Searches for the **first 2×2 block** where all pixels are strongly red (defined as `R ≥ 150`, `R ≥ 2*G`, and `R > B`). If found, return its top-left coordinate `(row, col)`; otherwise, return `None`.

### 2. `ColonyReport`
This class should:
- Be initialized with a `ColonyAnalyser` object.  
- Provide a method `generate_report()` that:  
  - Computes the total number of red colonies.  
  - Identifies the dominant color in the image.  
  - Finds the location of the largest red block.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code using the sample input file `colonies.csv`.  

---


