#Online store system
class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity

    def get_info(self):
        return f"{self.name}: ${self.price}, Stock: {self.stock_quantity}"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        print(f"Order placed by {self.name}: {order.get_summary()}")

    def get_order_history(self):
        return [order.get_summary() for order in self.orders]

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products  # List of Product objects
        self.total_price = sum(product.price for product in products)

    def get_summary(self):
        product_names = ", ".join([product.name for product in self.products])
        return f"Customer: {self.customer.name}, Products: {product_names}, Total Price: ${self.total_price}"

product1=Product('Telivision',10000,5)
product2=Product('Iphone',50000,1)
product3=Product('Washing Machine',15000,4)
''
customer1=Customer('yash','yash@gmail.com')

order1=Order(customer1,[product1,product2])
order2=Order(customer1,[product3])

customer1.place_order(order1)
customer1.place_order(order2)

summary=customer1.get_order_history()

print(f"the order summary is {summary}")