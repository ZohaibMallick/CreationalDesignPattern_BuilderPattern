# CreationalDesignPattern_BuilderPattern
**This project implements a Pizza Ordering System using the Builder Pattern, a creational design pattern that allows the construction of complex objects step-by-step.**
#### The Builder Pattern is like a step-by-step recipe for making something complicated. It breaks down the process into smaller, manageable steps, so we can easily build different versions of that thing. This is helpful when there are many options or parts to choose from.


![PizaaOrderUML_Diagram](https://github.com/user-attachments/assets/b22c6f54-c829-4ee3-9654-7f8c20b257a6)
### UML Diagram Explanation
  - Pizza: The complex object to be created with various ingredients and sizes.
  - PizzaBuilder: This is the builder class that allows step-by-step construction of a pizza object by setting the desired properties (size, cheese, pepperoni, bacon).
  - Director: This class is optional in the builder pattern and is used here to construct pre-defined types of pizzas (e.g., Margherita, Pepperoni) using the builder.

### How Code Works
  - User Input for Size: Prompts the user to enter the size of the pizza (small, medium, or large).
  - Adding Ingredients: Asks the user if they want to add cheese, pepperoni, and bacon. The input is processed to add ingredients based on the user's response.
  - Building the Pizza: Uses the input to customize the pizza's size and ingredients, then creates the pizza using the build() method.

### Sample Execution:
```bash 
Create your custom pizza!
Enter pizza size (Small, Medium, Large): Large
Add cheese? (yes/no): yes
Add pepperoni? (yes/no): no
Add bacon? (yes/no): yes
Pizza (Size: Large, Ingredients: Cheese, Bacon)
```
 
