from datetime import datetime, timedelta


class WarehouseManager:
    def __init__(self, filename):
        self.warehouses = self._parse_file(filename)

    def _parse_date(self, date_str):
        formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"]
        for fmt in formats:
            return datetime.strptime(date_str,fmt)

    def _parse_file(self, filename):
        warehouses = {}
        current_warehouse = None

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    current_warehouse = line[1:-1]
                    warehouses[current_warehouse] = []
                else:
                    name, category, price, quantity, expiration = line.strip().split(",")
                    warehouses[current_warehouse].append({
                        "name": name,
                        "category": category,
                        "price": float(price),
                        "quantity": int(quantity),
                        "expiration": self._parse_date(expiration)
                    })
        return warehouses

    def total_value(self, warehouse):
        total = 0
        for item in self.warehouses[warehouse]:
            total += item["price"] * item["quantity"]
        return total

    def category_value(self, warehouse, category):
        total = 0
        for item in self.warehouses[warehouse]:
            if item["category"] == category:
                total += item["price"] * item["quantity"]

        return total

    def expiring_soon(self, warehouse, date):
        expiring_items = []
        for item in self.warehouses[warehouse]:
            if item["expiration"] <= date:
                expiring_items.append(item["name"])
        return expiring_items

    def most_stocked_items(self):
        max_item = None
        max_quantity = -1
        max_warehouse = None

        for warehouse, items in self.warehouses.items():
            for item in items:
                if item["quantity"] > max_quantity:
                    max_quantity = item["quantity"]
                    max_item = item
                    max_warehouse = warehouse

        return max_item, max_warehouse


