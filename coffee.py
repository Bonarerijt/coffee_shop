from order import Order
from customer import Customer

class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance (name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be a string, at least 3 characters long")
        
    def orders(self):
        return [order for order in Order.orders if order.coffee == self]
    
    def customer(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
    
        
coffee = Coffee("Latte")
print(coffee.name)