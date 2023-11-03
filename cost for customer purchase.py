
item_prices = [2.99, 1.99, 4.99, 3.49]
item_quantities = [3, 2, 1, 4]
discount_rate = 10
tax_rate = 7.5
total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
discount = (discount_rate / 100) * total_cost_before_discount
total_cost_after_discount = total_cost_before_discount - discount
tax = (tax_rate / 100) * total_cost_after_discount
total_cost = total_cost_after_discount + tax
print("Total cost with discount and tax: $", total_cost)
