





car_price = int(input("What is the price of your car?"))


if car_price > 5000000:
	road_tax = car_price / 25
	print(road_tax)
elif car_price >= 3000000 and car_price <= 5000000:
	road_tax = car_price / 20
	print(road_tax)
elif car_price >= 1000000 and car_price <= 3000000:
	road_tax = car_price / 15
	print(road_tax)
else:
	road_tax = car_price / 10
	print(road_tax)