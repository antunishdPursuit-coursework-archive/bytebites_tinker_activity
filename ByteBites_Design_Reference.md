# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
<!-- Write a short set of instructions guiding how your AI assistant should behave 
when helping with this project — for example, which classes to stay within, 
what complexity to avoid, or any preferences for how suggestions are structured. -->
- Keep only `Customer`, `FoodItem`, `Menu`, and `Transaction`.
- Use the specification and current Python implementation as context. Keep
  diagram attributes and methods consistent with the code.
- Use has-a relationships for the stored objects; do not add inheritance.
- Keep filtering and sorting on `Menu`, and purchase totals on `Transaction`.
- Allow empty menus and transactions. An empty transaction has a total of zero,
  including after its last item is removed.
- Preserve the original menu order when producing a sorted view.
- Prefer small, readable changes. Explain the behavior each proposed change
  affects, and verify it with an example or a behavior test.
- Ask before proposing new input rules or features beyond the specification.
