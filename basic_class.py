class Product:
    # Attribute
    def __init__(self, name="water", quantity=3, price=15):
        self.name = name
        self.quantity = quantity
        self.price = price


    def hello(self):
        print("Hello, customer, Here are the water shop.")


class Customer(Product):
    def __init__(self, fullname, money, name="รถยนต์", quantity=1, price=20000):
        super().__init__(name, quantity, price)
        self.fullname = fullname
        self.money = money

    # Method
    def calculate(self):
        self.total = self.quantity * self.price
        self.money -= self.total
        print("คุณเหลือเงิน %d บาท" % self.money)




customer01 = Customer('uncle enginerr', 500, 'watch', 1, 400)
print(customer01.fullname)
print(customer01.name)
customer01.calculate()