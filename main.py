from product import Product
from store import Store


product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Phone", 500, "Electronics")

store = Store("TechStore")
store.add_product(product1)
store.add_product(product2)

#store.inflation(0.1)

store.set_clearence("Electronics", 0.2)



