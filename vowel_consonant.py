name = input("Enter word: ").lower()

#if ["a", "e"] in name:
	#print("true")

vowel = ["a", "e", "i", "o", "u"]

consonant = 0
count = 0

all_char = []
all_vow = []

for character in name:	
	for letter in vowel:
		if character == letter:
			if character not in all_vow:
				all_vow.append(character)
				count += 1
		else:
			if character not in all_char:
				all_char.append(character)
				consonant += 1

ren = consonant - count		

print(f"there are {count} vowel and {ren} consonant")

