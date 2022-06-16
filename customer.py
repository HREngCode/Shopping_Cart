from shopping_cart import ShoppingCart
from product import Product

cart = ShoppingCart()

class Customer:

    def __init__(self, name):
        self.customer_name = name
        self.cart_list = customer_cart.products

    def new_item_to_cart(self):
        cart.add_product_to_cart(Product("tire", 100, "Auto"))
        cart.add_product_to_cart(Product("wheels", 50, "Auto"))
        cart.add_product_to_cart(Product("valves", 10, "Auto"))
        cart.add_product_to_cart(Product("lug nuts", 5, "Auto"))
#         self.customer_name = name
#         self.cart_list = customer_cart.products
#         item_in_cart=ShoppingCart()
#         for product in self.cart_list:
#             print(item_in_cart.products[0].name)


    #     self.product_name = customer_cart.products
    #     self.product_price = customer_cart.products.price
    #     self.product_category = customer_cart.products.category
        # print(f'Customer:{self.name} has ordered a set of {self.product_name} for ${self.product_price} in the {self.product_category} department')


