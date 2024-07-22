



def equal_strings(word1, word2):

	new_word1 = "".join(sorted(word1.lower()))
	
	new_word2 = "".join(sorted(word2.lower()))

	if new_word1 == new_word2:
		return "True"
	else: return "False"



print(equal_strings("LOVE", "evol"))
