# Question

### Warehouse Inventory Management

You are tasked with managing inventory across multiple warehouses.  
Each warehouse is represented in a text file as a section with a header in square brackets `[Warehouse Name]` followed by item entries:


- Each line after the header has the format:  
  `<name>, <category>, <price>, <quantity>, <expiration_date>`  
- Dates may be in different formats: `"YYYY-MM-DD"`, `"DD/MM/YYYY"`, or `"YYYY/MM/DD"`.

---

## Your Task

Design a Python class `WarehouseManager` that:

1. Reads the file and stores all warehouses and their items in a structured format.  
2. Provides the following methods:
   - `total_value(warehouse)`: Returns the total value of all items in the given warehouse (`price × quantity`).  
   - `category_value(warehouse, category)`: Returns the total value of all items of a specific category in the given warehouse.  
   - `expiring_soon(warehouse, date)`: Returns a list of item names in the warehouse that expire **on or before** the given date.  
   - `most_stocked_items()`: Returns the item with the **highest quantity** across all warehouses and the warehouse it belongs to.  

---

## Tasks

1. Implement the `WarehouseManager` class.  
2. Demonstrate its functionality using the provided `warehouses.txt`.  
3. Show:
   - Total value of each warehouse  
   - Total value by category (e.g., `"Fruits"` in Warehouse A)  
   - Items expiring soon before a given date  
   - The most stocked item across all warehouses  

