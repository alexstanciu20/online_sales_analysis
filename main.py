from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 3000, 5)
p2 = Product("Mouse", 100, 20)
p3 = Product("Căști", 150, 10)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.show_products()
manager.total_inventory_value()
