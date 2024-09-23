def add_ce(word):
    list_word = list(word)
    ce_to_list = list("ce")
    if len(word) % 2 == 0:
        list_word[len(word // 2)] = ce_to_list
    result = word + "ce"
    return result
print(add_ce("joy"))