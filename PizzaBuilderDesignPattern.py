class Pizza:
    def __init__(self, size, cheese, pepperoni, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.bacon = bacon

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("Cheese")
        if self.pepperoni:
            ingredients.append("Pepperoni")
        if self.bacon:
            ingredients.append("Bacon")
        return f"Pizza (Size: {self.size}, Ingredients: {', '.join(ingredients)})"


class PizzaBuilder:
    def __init__(self):
        self.size = "Medium"
        self.cheese = False
        self.pepperoni = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.bacon)


class Director:
    def construct_custom_pizza(self, builder):
        size = input("Enter pizza size (Small, Medium, Large): ")
        builder.set_size(size)

        cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == 'yes':
            builder.add_cheese()

        pepperoni = input("Add pepperoni? (yes/no): ").strip().lower()
        if pepperoni == 'yes':
            builder.add_pepperoni()

        bacon = input("Add bacon? (yes/no): ").strip().lower()
        if bacon == 'yes':
            builder.add_bacon()

        return builder.build()


# Sample Execution
if __name__ == "__main__":
    director = Director()
    builder = PizzaBuilder()

    # Constructing a Custom Pizza with User Input
    print("Create your custom pizza!")
    custom_pizza = director.construct_custom_pizza(builder)
    print(custom_pizza)  # Output will vary based on user input
