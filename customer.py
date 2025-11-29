from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError ("Name must be a string between 1 and 15 characters.")
        

    def orders(self):
        return [order for order in Order.orders if order.coffee == self]
    
    def coffee(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self,coffee, price )

    @classmethod
    def most_aficionado(cls, coffee):
              
        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be a Coffee object.")
        
        spending_by_customer = {}
        relevant_orders = [order for order in Order.all if order.coffee is coffee]
        
        if not relevant_orders:
            return None
        
        for order in relevant_orders:
            customer = order.customer
            price = order.price
            if customer not in spending_by_customer:
                spending_by_customer[customer] = 0
            spending_by_customer[customer] += price
        
        return max(spending_by_customer, key=lambda cust: spending_by_customer[cust])


customer = Customer("Judy")
print(customer.name)
