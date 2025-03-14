import csv
import os


class PriceList:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceList, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, filename="price_list.csv"):
        self.current_dir = os.path.dirname(__file__)
        self.pricelist = {}
        self.load_pricelist(filename)

    def load_pricelist(self, filename):
        
        with open(os.path.join(self.current_dir, filename), mode="r") as file:
            reader = csv.reader(file)
            for rows in reader:
                self.pricelist[rows[0]] = {'product': rows[1], 'price': float(rows[2])}

    def save_pricelist(self, filename):
        
        with open(os.path.join(self.current_dir, filename), mode="w", newline='') as file:
            writer = csv.writer(file)
            for key, data in self.pricelist.items():
                writer.writerow([key, data['product'], data['price']])

    def get_price(self, product):
        
        product_data = self.pricelist.get(product)
        return product_data['price'] if product_data else None

    def set_price(self, product, product_name, price):
        
        self.pricelist[product] = {'product': product_name, 'price': float(price)}

    def get_pricelist(self):
       
        return self.pricelist


# Example usage:
if __name__ == "__main__":
    price_list = PriceList()
    print(price_list.get_pricelist())
