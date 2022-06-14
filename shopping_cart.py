
shopping_cart_list = []


class ShoppingCart:
    
    def __init__(self):
        from product import Product
        product_info = Product()
        self.in_shopping_cart = product_info.name
        self.price_in_shopping_cart = int(product_info.price)

    def add_product_to_cart(self):     
        shopping_cart_list = []
        item_name = self.in_shopping_cart
        shopping_cart_list.append(item_name)
        item_price = self.price_in_shopping_cart
        print(shopping_cart_list)   

#     # def calculate_total_cost(self):

#     def empty_cart(self):
#         shopping_cart_list.clear()
#         print(shopping_cart_list)
