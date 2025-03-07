class ShoppingList:
    def __init__(self):
        self.items = {}  # Skiftet fra en liste til en dictionary
        self.price_list = {
            "BOOST": "Booster",
            "BIGM": "Big Mac Menu",
            "APPL": "Apples",
            "BANA": "Bananas"
        }

    def add_item(self, item_id, quantity=1):
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity

    def remove_item(self, item_id, quantity=1):
        if item_id in self.items:
            self.items[item_id] -= quantity
            if self.items[item_id] <= 0:
                del self.items[item_id]

    def get_items(self):
        return {self.price_list[item_id]: qty for item_id, qty in self.items.items()}


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("APPL", 1)
    shopping_list.add_item("BANA", 2)
    shopping_list.add_item("BOOST", 2)  
    print("Efter tilføjelse(r):", shopping_list.get_items())
    shopping_list.remove_item("APPL")
    print("Fjernet æble(r):", shopping_list.get_items()) 
    shopping_list.remove_item("BANA", 1)
    print("Fjernet banan(er):", shopping_list.get_items())
    shopping_list.remove_item("BOOST", 2)
    print("Removed booster(s):", shopping_list.get_items())
