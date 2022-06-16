from product import Product

class ShoppingCart:
    
    def __init__(self):
        self.products = []
        # self.name_in_shopping_cart = name
        # self.price_in_shopping_cart = int(product_info.price)

    def add_product_to_cart(self, product):  
        self.products.append(product) 
    
    def calculate_total_cost(self):
        total_cost = int(0) 
        for product in self.products:
            total_cost = total_cost + product.price
            
        print(f'Your total cost is ${total_cost}')
 
    def empty_cart(self):
        self.products.clear()
        print(self.products)
