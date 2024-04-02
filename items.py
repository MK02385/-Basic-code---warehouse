class Items:
    def __init__(self, id_: str, name: str, unit: str, quantity: int, price: float) -> tuple:
        self.id_ = id_
        self.name = name
        self.unit = unit
        self.quantity = quantity
        self.price = price
        self.item_list = []

    def enter_item(self, id_, name, unit, quantity, price):
        item = Items(id_, name, unit, quantity, price)
        self.item_list.append(item)

    def id_adding_quantity(self, item_id, addition):
        for item in self.item_list:
            if item.id_ == item_id:
                quantity = item.quantity + addition
                item.quantity = quantity

    def name_adding_quantity(self, item_name, addition):
        for item in self.item_list:
            if item.name == item_name:
                quantity = item.quantity + addition
                item.quantity = quantity

    def id_change_price(self, item_id, new_price):
        for item in self.item_list:
            if item.id_ == item_id:
                item.price = new_price

    def name_change_price(self, item_name, new_price):
        for item in self.item_list:
            if item.name == item_name:
                item.price = new_price

    def display_item(self):
        for item in self.item_list:
            return f"\n\n{item.id_}. {item.name} - {item.quantity} {item.unit} - {item.price:.2f} $"

    def check_id(self, item_id):
        for item in self.item_list:
            if item.id_ == item_id:
                return True

    def check_name(self, item_name):
        for item in self.item_list:
            if item.name == item_name:
                return True


