class Coffee:
    def __init__(self, name):
        if not isinstance (name, str) or not len(name) >= 3:
            raise ValueError("Coffee name must be a string at least 3 characters long")
        self.name = name

coffee = Coffee("Latte")
print(coffee.name)