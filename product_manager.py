from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"Valoare totală a inventarului: {total} RON")

    def remove_product_by_name(self, name):
        self.products = [p for p in self.products if p.name != name]