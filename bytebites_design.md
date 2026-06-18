# ByteBites UML Class Diagram

This draft follows `ByteBites_Design_Reference.md`: keep the design limited to
the four candidate classes and do not add authentication, database, or unrelated
backend features.

```mermaid
classDiagram
    class Customer {
        -String name
        -List~Transaction~ purchaseHistory
        +Customer(name)
        +addPurchase(transaction)
        +getPurchaseHistory()
    }

    class FoodItem {
        -String name
        -double price
        -String category
        -double popularityRating
        +FoodItem(name, price, category, popularityRating)
        +getName()
        +getPrice()
        +getCategory()
        +getPopularityRating()
    }

    class Menu {
        -List~FoodItem~ items
        +addItem(item)
        +removeItem(itemName)
        +getItems()
        +filterByCategory(category) List~FoodItem~
    }

    class Transaction {
        -Customer customer
        -List~FoodItem~ selectedItems
        +Transaction(customer)
        +addItem(item)
        +removeItem(itemName)
        +getSelectedItems()
        +calculateTotal() double
    }

    Customer "1" --> "0..*" Transaction : purchaseHistory
    Menu "1" --> "0..*" FoodItem : contains
    Transaction "1" --> "1" Customer : belongs to
    Transaction "1" --> "1..*" FoodItem : includes
```

## Class Summary

| Class | Responsibility |
| --- | --- |
| `Customer` | Stores a customer's name and past purchase history. |
| `FoodItem` | Represents one menu item with name, price, category, and popularity rating. |
| `Menu` | Manages the collection of available food items and supports category filtering. |
| `Transaction` | Groups selected food items for a customer and calculates the total cost. |

## Design Boundaries

- Use only `Customer`, `FoodItem`, `Menu`, and `Transaction`.
- Keep verification implied by purchase history; do not add authentication logic.
- Do not add database, payment, account, or ordering features outside the spec.
