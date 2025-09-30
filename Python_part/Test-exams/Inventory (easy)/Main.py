class Inventory:
    def __init__(self, filename):
        self.items = []

        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                name = parts[0].strip()
                quantity  = int(parts[1].strip())
                price = float(parts[2].strip())

                entry = {
                    "name": name,
                    "quantity": quantity,
                    "price": price
                }

                self.items.append(entry)

    def total_value(self):
        total = 0.0
        for entry in self.items:
            total += entry["quantity"] * entry["price"]

        return total

    def most_expensive_item(self):
        max_price = None
        max_name = None

        for entry in self.items:
            if max_price is None or entry["price"] > max_price:
                max_price = entry["price"]
                max_name = entry["name"]

        return max_name

    def _find_item_index_by_name(self, name):
        target = name.strip().lower()

        for i in range(len(self.items)):
            if self.items[i]["name"] == target:
                return i
        return None

    def restock_item(self, name, amount):
        if amount <= 0:
            return
        idx = self._find_item_index_by_name(name)
        if idx is None:
            return

        self.items[idx]["quantity"] += amount

    def sell_item(self, name, amount):

        if amount <= 0:
            return

        idx = self._find_item_index_by_name(name)

        if idx is None:
            return

        current = self.items[idx]["quantity"]
        new_value = current - amount

        if new_value < 0:
            new_value = 0
        self.items[idx]["quantity"] = new_value


class Shop:
    def __init__(self, inventory):
        self.inventory = inventory

    def daily_report(self):

        total = self.inventory.total_value()
        print("Total inventory value:", total)

        most_expensive = self.inventory.most_expensive_item()
        if most_expensive is None:
            print("Most expensive item: None")
        else:
            print("Most expensive item:", most_expensive)
        sold_out = []

        for entry in self.inventory.items:
            if entry["quantity"] == 0:
                sold_out.append(entry["name"])

        if len(sold_out) == 0:
            print("Sold out items: None")
        else:
            print("Sold out items:")
            for name in sold_out:
                print("-", name)


filename = "inventory.csv"
inventory = Inventory(filename)
shop = Shop(inventory)

inventory.sell_item("bananas", 10)
inventory.sell_item("grapes", 5)

    # Restock 20 apples.
inventory.restock_item("apples", 20)

    # Print daily report.
shop.daily_report()