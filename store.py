from product import Product

class Store:
    def __init__(self, name):
        self.list_of_products = []
        self.name = name

    def add_product(self, new_product):
        self.list_of_products.append(new_product)

    def sell_product(self, id):
        if 0<= id < len(self.list_of_products):
            self.list_of_products.pop(id)
            print(f"The poduct with index {id} is sold")
        else:
            print(f"Invalid product index {id}.")

    def inflation(self, percent_increase):
        for product in self.list_of_products:
            product.update_price(percent_increase, is_increased=True)
            print(f"Updated price for {product.name}: {product.price}")


    def set_clearence(self, category, percent_discount):
        for i in self.list_of_products:
            i.update_price(percent_discount, is_increased=False)
            print(f"Updated price for {i.name}: {i.price}")








