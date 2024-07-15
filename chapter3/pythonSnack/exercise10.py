principal = 1000
annual_rate = 7/100
number_of_years = 10



for year in range(1,31):
	amount_on_deposit= principal * (1 + annual_rate)**year

	#print('Uptimised')
	print(f'for year {year}, the amount on deposit is ',amount_on_deposit)
