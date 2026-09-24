# ByteBites core classes:
# Customer tracks a customer's name and purchase history.
# FoodItem represents one menu item with name, price, category, and popularity rating.
# Menu stores food items, filters by category, and sorts by popularity.
# Transaction stores selected items for a customer and calculates the total cost.

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)

    def get_purchase_history(self):
        return self.purchase_history


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

    def get_popularity_rating(self):
        return self.popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def get_items(self):
        return self.items

    def filter_by_category(self, category):
        """Return exact category matches without changing the menu."""
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        """Return items from highest to lowest popularity; keep menu order."""
        return sorted(
            self.items,
            key=lambda item: item.popularity_rating,
            reverse=True
        )


class Transaction:
    def __init__(self, customer):
        self.customer = customer
        self.selected_items = []

    def add_item(self, item):
        self.selected_items.append(item)

    def remove_item(self, item_name):
        self.selected_items = [
            item for item in self.selected_items if item.name != item_name
        ]

    def get_selected_items(self):
        return self.selected_items

    def calculate_total(self):
        """Sum current item prices, returning zero when no items are selected."""
        return sum(item.price for item in self.selected_items)


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    cookie = FoodItem("Chocolate Cookie", 3.00, "Desserts", 4.6)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cookie)

    print("All menu items:")
    for item in menu.get_items():
        print(f"- {item.name}: ${item.price:.2f}")

    print("\nDessert items:")
    for item in menu.filter_by_category("Desserts"):
        print(f"- {item.name}")

    print("\nItems sorted by popularity:")
    for item in menu.sort_by_popularity():
        print(f"- {item.name}: {item.popularity_rating}")

    customer = Customer("Alex")
    transaction = Transaction(customer)
    transaction.add_item(burger)
    transaction.add_item(soda)
    customer.add_purchase(transaction)

    print(f"\nOrder total: ${transaction.calculate_total():.2f}")
