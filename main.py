# print("Accc")

class Account:
	acc_num = 0
	def __init__(self, f_n):
		self.name = f_n
		print(self.acc_num)
		self.acc_num += 1
		count = self.acc_num
		self.number = count
		print(count)

ayo = Account(88)
aye = Account(1)

print(ayo.number)
print(aye.number)