# ByteBites

A small Python model for a campus food-ordering app, built for the
[AI110 Week 3 ByteBites Tinker](https://courses.codepath.org/courses/ai110/unit/3#!tinker).
It connects a feature request to a Mermaid class diagram, four Python classes,
and tests of their observable behavior.

## Review the four Tinker parts

| Part | Evidence | What to check |
| --- | --- | --- |
| 1. System design | [Spec](bytebites_spec.md), [AI reference](ByteBites_Design_Reference.md), [initial diagram](draft_from_copilot.mmd), [final diagram](bytebites_design.mmd), and [rendered preview](bytebites_design.md) | Four classes with clear responsibilities and has-a relationships; the final design removes the initial draft's unsupported user-verification method. |
| 2. Class implementation | [models.py](models.py) | `Customer`, `FoodItem`, `Menu`, and `Transaction` match the final diagram's attributes and methods. |
| 3. Algorithms | [models.py](models.py), including its runnable example | Filter categories, sort popularity from highest to lowest, and sum the prices in one transaction. |
| 4. Testing | [test_bytebites.py](test_bytebites.py) | Twelve tests cover normal behavior, empty states, changing selections, and independent customer/transaction data. |

## Run locally

Requires Python 3. From the project folder in PowerShell, create an isolated
Python environment and install pytest:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -B models.py
.\.venv\Scripts\python.exe -B -m pytest -p no:cacheprovider -q
```

If Python and pytest are already available in your active environment:

```text
python -B models.py
python -B -m pytest -p no:cacheprovider -q
```

The demo prints the menu, filters Desserts to Chocolate Cookie, sorts popularity
scores as 4.8, 4.6, 4.2, and prints `Order total: $11.00`.

Verified on September 23, 2026 with Python 3.14.5 and pytest 9.1.0:
**12 tests passed**. Both Mermaid sources were rendered during the preceding
diagram review; their contents are unchanged by the algorithm/test refinement.

## Behavior and test coverage

- Category filtering returns exact matches and returns an empty list when no
  items match or the menu is empty.
- Popularity sorting returns a new list in descending order, preserving the
  original menu order. Sorting an empty menu returns an empty list.
- A transaction starts empty and totals zero. Its total follows the current
  items as they are added or removed; removing the last item restores zero.
- Transactions keep separate item lists, even when they belong to the same
  customer. Customers keep separate purchase histories.

The tests check behavior rather than how a loop or conditional is written.
These checks cover the activity's required behaviors and selected edge cases;
they do not establish production payment processing or input validation.

## Explanation checkpoints

- **Why these classes?** Each owns a responsibility named in the request:
  customer history, individual food data, the menu catalog, or one purchase.
- **What changed after review?** The final diagram excludes `isVerifiedUser()`,
  uses Python's actual member names, includes popularity sorting, and allows
  zero selected items. The original draft stays available for comparison.
- **Why does total calculation belong on Transaction?** It knows one customer's
  selected items. Menu represents the full catalog, not one purchase.
- **Which test protects the empty-transaction decision?**
  `test_removing_last_item_leaves_zero_total` checks the transition from one
  selected item back to an empty list and zero total. The original
  `test_order_total_is_zero_when_empty` checks a newly created transaction.

## Scope

Use only the four classes in the spec. Authentication, databases, checkout,
payments, and additional application features are outside this Tinker.
