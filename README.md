# Coffee Shop — Object-Oriented Programming Project

This project models a simple Coffee Shop domain using Python and Object-Oriented Programming principles.
It demonstrates class design, data validation, object relationships, aggregation, and class methods.

The three core entities in this domain are:

Customer

Coffee

Order

Together, these classes model how customers order different types of coffee and how relationships between these objects are managed.

## 1. Setup and Preparation
Create Project Directory
mkdir coffee_shop
cd coffee_shop

Initialize Virtual Environment

Using pipenv:

pipenv install
pipenv shell

Install Test Dependencies
pipenv install pytest


You are now ready to start building your domain model.

## 2. Domain Model Design

Before writing any code, the relationships between the classes were sketched and designed.

Main Classes

Customer

Coffee

Order

#### Relationships

A Customer can have many Orders.

A Coffee can have many Orders.

An Order belongs to one Customer and one Coffee.

This creates a many-to-many relationship between Customer and Coffee through Orders.

Single Source of Truth

Each class keeps track of all its instances in a class-level list.
Orders serve as the central link between customers and coffees.

## 3. Project Structure

Inside the coffee_shop directory, create the following files:

customer.py
coffee.py
order.py


Each file contains one class matching the file name.

## 4. Initializers and Properties

* Customer (customer.py)
Initialized with: name
Validation rules:
Must be a string
Length between 1 and 15 characters
Has a property name with getter and setter validation

* Coffee (coffee.py)
Initialized with: name
Validation rules:
Must be a string
Must be at least 3 characters long
Has a property name with validation in the setter

* Order (order.py)
Initialized with:
Customer instance
Coffee instance
price between 1.0 and 10.0 (float)

Properties:
customer
coffee
price

Validation ensures:
Correct data types
Allowed ranges

## 5. Object Relationship Methods and Properties
Order

customer → returns the Customer instance

coffee → returns the Coffee instance

Coffee

orders() → returns all Order instances linked to this coffee

customers() → returns a unique list of Customers who ordered the coffee

Customer

orders() → returns all Order instances for this customer

coffees() → returns a unique list of Coffees the customer has ordered

## 6. Aggregate and Association Methods
Customer
create_order(coffee, price)

Creates a new Order

Automatically associates:

This Customer

The provided Coffee

The price

Coffee
num_orders()

Returns total number of orders for a coffee

average_price()

Returns the average price of all orders for this coffee

## 7. Customer Class Method — most_aficionado
Customer.most_aficionado(coffee)

Receives a Coffee object

Determines which Customer has spent the most money on that coffee

Returns:

The Customer instance

Or None if no orders exist

This method uses:

Orders linked to the coffee

Total price spent by each customer

A max calculation to determine the most dedicated customer