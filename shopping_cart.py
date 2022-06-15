from product import Product

class ShoppingCart:
    
    def __init__(self):
        self.shopping_cart_list = []
#         self.in_shopping_cart = product_info.name
#         self.price_in_shopping_cart = int(product_info.price)

    def add_product_to_cart(self, product):     
        self.shopping_cart_list.append(product)
#         item_name = self.in_shopping_cart
#         shopping_cart_list.append(item_name)
#         item_price = self.price_in_shopping_cart
#     def print(shopping_cart_list) 
#         pass         

#     # def calculate_total_cost(self):

#     def empty_cart(self):
#         shopping_cart_list.clear()
#         print(shopping_cart_list)
