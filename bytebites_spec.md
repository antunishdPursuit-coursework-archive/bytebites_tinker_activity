# ByteBites Spec

## Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## Candidate Classes

1. Customer
2. FoodItem
3. Menu
4. Transaction

## Transaction behavior clarification

A transaction may contain zero or more food items. Customers can start a
transaction before selecting anything.

- A new transaction starts with an empty item list and a total of $0.
- Adding or removing items changes the total to the sum of the remaining
  items' prices.
- Removing the last item leaves a valid empty transaction with a total of $0.

These rules describe item selection and total calculation. Checkout and
payment rules are outside this activity's scope.
