

def my_discount(price, discount):


	dicounted = price / 100 * 15

	new_price = price - dicounted

	return new_price


print(my_discount(150, 15))