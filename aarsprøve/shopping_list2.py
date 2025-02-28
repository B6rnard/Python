class ShoppingList:
    """
    A class to represent a shopping list.

    Attributes
    ----------
    items : dict
        A dictionary to store shopping items and their quantities.

    Methods
    -------
    add_item(item, quantity=1):
        Adds an item to the shopping list with a specified quantity.
    
    remove_item(item, quantity=1):
        Removes a specified quantity of an item from the shopping list if it exists.
    
    get_items():
        Returns the dictionary of shopping items and their quantities.
    """
    def __init__(self):
        self.items = {}  # Skiftet fra en liste til en dictionary

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def get_items(self):
        return self.items


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("Apples", 1)
    shopping_list.add_item("Bananas", 2)
    shopping_list.add_item("Boosters", 2)  
    print("Efter tilføjelser:", shopping_list.get_items())
    
    shopping_list.remove_item("Apples")
    print("fjernet æble(r):", shopping_list.get_items())
    
    shopping_list.remove_item("Bananas", 1)
    print("fjernet banan(er):", shopping_list.get_items())
    
    shopping_list.remove_item("Boosters", 2)
    print("removed booster(s):", shopping_list.get_items())
