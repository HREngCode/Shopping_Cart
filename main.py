from customer import Customer
from product import Product
from shopping_cart import ShoppingCart

print('Please type the customer name')
customer_one_info = Customer(input())

order_one = ShoppingCart()
order_one.add_product_to_cart()
item_cost_one = int(order_one.price_in_shopping_cart)
print(item_cost_one)

order_two = ShoppingCart()
order_two.add_product_to_cart()
item_cost_two = int(order_two.price_in_shopping_cart)
print(item_cost_two)

order_three = ShoppingCart()
order_three.add_product_to_cart()
item_cost_three = int(order_three.price_in_shopping_cart)
print(item_cost_three)

cart = ShoppingCart()
cart.add_product_to_cart(Product)

total_cost = (item_cost_one) + (item_cost_two) + (item_cost_three)
print(f'Your total cost is {total_cost}')

# price_total = ShoppingCart()
# total_cost = price_total.price_in_shopping_cart
# price_total.calculate_total()
# print(total_cost)

# print(f'The list consists of {add_new_order.in_shopping_cart}')
