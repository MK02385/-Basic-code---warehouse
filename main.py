from items import Items
from variable import Variable
from menu import *

item = Items(None, None, None, 0, 0)
v = Variable()

while True:
    main_choice = input(main_menu)
    if main_choice == "1":
        while True:
            choice = input(item_menu)

            if choice == "1":
                item.enter_item(
                    id_=v.enter_id(),
                    name=v.enter_name(),
                    unit=v.enter_unit(),
                    quantity=v.enter_quantity(),
                    price=v.enter_price()
                )

            elif choice == "2":
                add_choice = input(add_menu)
                if add_choice == "1":
                    id_ = v.enter_id()
                    while not item.check_id(id_):
                        print("The entered id do not exist.")
                        break
                    else:
                        addition = v.enter_quantity()
                        item.id_adding_quantity(id_, addition)
                elif add_choice == "2":
                    name = v.enter_name()
                    while not item.check_name(name):
                        print("The entered name do not exist.")
                        break
                    else:
                        addition = v.enter_quantity()
                        item.name_adding_quantity(name, addition)

            elif choice == "3":
                price_choice = input(price_menu)
                if price_choice == "1":
                    id_ = v.enter_id()
                    while not item.check_id(id_):
                        print("The entered id do not exist.")
                        break
                    else:
                        new_price = v.enter_price()
                        item.id_change_price(id_, new_price)
                elif price_choice == "2":
                    name = v.enter_name()
                    while not item.check_name(name):
                        print("The entered name do not exist.")
                        break
                    else:
                        new_price = v.enter_price()
                        item.name_change_price(name, new_price)

            elif choice == "4":
                print(item.display_item())

            elif choice == "5":
                print("")
                break
            else:
                print("Unknown command...\nPlease try again.")
    elif main_choice == "2":
        print("The program has been shut down...")
        break
    else:
        print("Unknown command...\nPlease try again.")