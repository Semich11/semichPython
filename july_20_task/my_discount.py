

def my_discount(price, discount):


	discount_price = price / 100 * discount

	new_price = price - discount_price

	return new_price


print(my_discount(150, 15))