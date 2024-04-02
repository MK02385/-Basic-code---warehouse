class Variable:
    def __init__(self):
        pass

    def enter_id(self):
        id_ = input("Enter the item code: ")
        return id_

    def enter_name(self):
        name = input("Enter the name of the item: ")
        return name

    def enter_quantity(self):
        quantity = int(input("Enter the quantity of the item: "))
        return quantity

    def enter_unit(self):
        unit = input("Enter the unit of the item: ")
        return unit

    def enter_price(self):
        price = float(input("Enter the price of the item: "))
        return price

