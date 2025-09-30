# Question

### Forest Fire Detection Using Drone Imagery

You are given CSV-like image data representing forest areas.  
Each pixel is represented as an RGB triplet (`R,G,B`), separated by spaces in each row.  



---

## Your Task

Design two Python classes:

### 1. `ForestAnalyzer`
This class should:
- Read the pixel data from a CSV file.  
- Provide the following methods:
  - `is_dominantly_green()`: Returns `True` if **more than 60% of the pixels** have green as the dominant color (`G > R` and `G > B`).  
  - `is_fire_detected()`: Returns `True` if there exists at least one **3×3 block** where all pixels are strongly red (`R ≥ 200` and `R > G` and `R > B`).  

### 2. `Drone`
This class should:
- Be initialized with a `ForestAnalyzer` object.  
- Provide a method `analyze_and_act()` that:
  - Returns `"Alert: fire!!"` if fire is detected.  
  - Returns `"All clear"` if the forest is dominantly green.  
  - Returns `"Investigate further"` otherwise.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code using the following image files:
   - `forest_fire.csv` (contains red hotspots)  
   - `forest_green.csv` (predominantly green forest)  
   - `forest_mixed.csv` (mixed colors)  
3. Print the drone’s action for each image.  

---
