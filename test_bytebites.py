from models import Customer, FoodItem, Menu, Transaction


def test_filter_by_category_returns_only_matching_items():
    menu = Menu()
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    lemonade = FoodItem("Lemonade", 3.00, "Drinks", 4.5)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(lemonade)

    filtered_items = menu.filter_by_category("Drinks")

    assert [item.get_name() for item in filtered_items] == ["Large Soda", "Lemonade"]
    assert all(item.get_category() == "Drinks" for item in filtered_items)


def test_filter_by_category_returns_empty_list_when_no_items_match():
    menu = Menu()
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)

    menu.add_item(burger)

    assert menu.filter_by_category("Desserts") == []


def test_sort_by_popularity_returns_items_highest_to_lowest():
    menu = Menu()
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    cookie = FoodItem("Chocolate Cookie", 3.00, "Desserts", 4.6)

    menu.add_item(soda)
    menu.add_item(cookie)
    menu.add_item(burger)

    sorted_items = menu.sort_by_popularity()

    assert [item.get_name() for item in sorted_items] == [
        "Spicy Burger",
        "Chocolate Cookie",
        "Large Soda",
    ]
    assert [item.get_popularity_rating() for item in sorted_items] == [4.8, 4.6, 4.2]


def test_sort_by_popularity_returns_empty_list_when_menu_is_empty():
    menu = Menu()

    assert menu.sort_by_popularity() == []


def test_calculate_total_with_multiple_items():
    customer = Customer("Alex")
    burger = FoodItem("Spicy Burger", 10.00, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)
    transaction = Transaction(customer)

    transaction.add_item(burger)
    transaction.add_item(soda)

    assert transaction.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    customer = Customer("Alex")
    transaction = Transaction(customer)

    assert transaction.calculate_total() == 0


def test_filter_by_category_returns_empty_list_when_menu_is_empty():
    """Filtering an empty catalog returns no items without an error."""
    menu = Menu()

    assert menu.filter_by_category("Drinks") == []


def test_sort_by_popularity_preserves_original_menu_order():
    """A sorted view does not reorder the catalog used by other operations."""
    menu = Menu()
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)
    cookie = FoodItem("Chocolate Cookie", 3.00, "Desserts", 4.6)
    menu.add_item(soda)
    menu.add_item(burger)
    menu.add_item(cookie)

    sorted_items = menu.sort_by_popularity()

    assert sorted_items == [burger, cookie, soda]
    assert menu.get_items() == [soda, burger, cookie]


def test_total_updates_after_adding_and_removing_items():
    """The total always reflects the items currently selected."""
    transaction = Transaction(Customer("Alex"))
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)

    transaction.add_item(burger)
    assert transaction.calculate_total() == 8.50

    transaction.add_item(soda)
    assert transaction.calculate_total() == 11.00

    transaction.remove_item("Spicy Burger")
    assert transaction.get_selected_items() == [soda]
    assert transaction.calculate_total() == 2.50


def test_removing_last_item_leaves_zero_total():
    """Removing the final selection restores a valid empty transaction."""
    transaction = Transaction(Customer("Alex"))
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.2)
    transaction.add_item(soda)

    transaction.remove_item("Large Soda")

    assert transaction.get_selected_items() == []
    assert transaction.calculate_total() == 0


def test_transactions_keep_separate_item_lists():
    """Adding to one transaction leaves another transaction empty."""
    customer = Customer("Alex")
    first_transaction = Transaction(customer)
    second_transaction = Transaction(customer)
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)

    first_transaction.add_item(burger)

    assert first_transaction.get_selected_items() == [burger]
    assert first_transaction.calculate_total() == 8.50
    assert second_transaction.get_selected_items() == []
    assert second_transaction.calculate_total() == 0


def test_purchase_history_belongs_to_each_customer():
    """Recording one customer's purchase does not change another's history."""
    first_customer = Customer("Alex")
    second_customer = Customer("Sam")
    transaction = Transaction(first_customer)
    transaction.add_item(FoodItem("Large Soda", 2.50, "Drinks", 4.2))

    first_customer.add_purchase(transaction)

    assert first_customer.get_purchase_history() == [transaction]
    assert second_customer.get_purchase_history() == []
