class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError(
                "Name must be a string between 1 and 15 characters")
        self.name = name


customer = Customer(6)
print(customer.name)
