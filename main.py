from customer import Customer
from product import Product
from shopping_cart import ShoppingCart

customer_one_info = Customer("Chad")

cart = ShoppingCart()
cart.add_product_to_cart(Product("tire", 100, "Auto"))
cart.add_product_to_cart(Product("wheels", 50, "Auto"))
cart.add_product_to_cart(Product("valves", 10, "Auto"))
cart.add_product_to_cart(Product("lug nuts", 5, "Auto"))

customer_one_info.new_item_to_cart("Chad")

total_in_cart = cart.calculate_total_cost()

# cart.products[0].name
# cart.products[0].price
# cart.products[0].category

print(cart.products[0].name)
print(cart.products[0].price)
print(cart.products[0].category)


# price_total = ShoppingCart()
# total_cost = price_total.price_in_shopping_cart
# price_total.calculate_total()
# print(total_cost)

# print(f'The list consists of {cart.shopping_cart_list}')
