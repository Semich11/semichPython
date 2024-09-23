import random
import string

def generate_password(length):

    all_character = string.ascii_letters + string.digits + string.punctuation

    generated_password = "".join(random.choice(all_character) for i in range(length))

    return generated_password

print(generate_password(16))