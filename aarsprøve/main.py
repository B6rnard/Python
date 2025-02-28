from shopping_list2 import ShoppingList
from price_list import PriceList

shopping_list = ShoppingList()
shopping_list.add_item("Apples",2)
shopping_list.add_item("Bananas")
print(shopping_list.get_items())
shopping_list.remove_item("Apples")
print(shopping_list.get_items())

price_list = PriceList()
print(price_list.get_price("Booster"))
#get