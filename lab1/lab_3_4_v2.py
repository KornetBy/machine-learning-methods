"""
Придумать класс самостоятельно, реализовать в нем методы экземпляра
класса, статические, методы, методы класса
"""

class Inventory:
    total_sales = 0


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Inventory.total_sales += quantity 


    def add_stock(self, amount):
        self.quantity += amount
        Inventory.total_sales += amount
        print(f"Добавлено {amount} шт. товара '{self.name}'. Текущее количество: {self.quantity}")


    def sell(self, amount):
        if amount > self.quantity:
            print(f"Недостаточно товара '{self.name}' на складе.")
        else:
            self.quantity -= amount
            Inventory.total_sales -= amount
            print(f"Продано {amount} шт. товара '{self.name}'. Остаток: {self.quantity}")


    def update_price(self, new_price):
        self.price = new_price
        print(f"Новая цена товара '{self.name}': {self.price} руб.")

    @classmethod
    def show_total_sales(cls):
        print(f"Общее количество всех товаров на складе: {cls.total_sales} шт.")

    @staticmethod
    def calculate_total_cost(price, quantity, tax_rate=0.2):
        total = price * quantity
        total_with_tax = total * (1 + tax_rate)
        return round(total_with_tax, 2)

    def show_total_value(self):
        total_value = Inventory.calculate_total_cost(self.price, self.quantity)
        print(f"Стоимость всех '{self.name}' с учетом налога: {total_value} руб.")


item1 = Inventory("Ноутбук", 50000, 10)
item2 = Inventory("Смартфон", 20000, 20)


item1.add_stock(5)                 
item1.sell(3)                      
item1.update_price(52000)          
item1.show_total_value()          

print()

item2.sell(5)                     
item2.show_total_value()         

Inventory.show_total_sales()       
