# Question

### Shop Inventory Management

You are asked to manage a shop inventory using Python.  
The inventory data is stored in a CSV file with the following format:


For example, the file `inventory.csv`


---

## Your Task

Design two Python classes:

### 1. `Inventory`
This class should:
- Read inventory data from a CSV file.  
- Store items in a structured format.  
- Provide the following methods:
  - `total_value()`: Returns the total value of the inventory (quantity × price for all items).  
  - `most_expensive_item()`: Returns the name of the item with the highest unit price.  
  - `restock_item(name, amount)`: Increases the quantity of a given item by the specified amount.  
  - `sell_item(name, amount)`: Decreases the quantity of a given item by the specified amount, but not below 0.  

### 2. `Shop`
This class should:
- Be initialized with an `Inventory` object.  
- Provide a method `daily_report()` that prints:
  - Total inventory value  
  - The most expensive item  
  - Any items that are sold out (quantity = 0)  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code by:
   - Selling 10 bananas and 5 grapes  
   - Restocking 20 apples  
   - Printing the daily report  

---
