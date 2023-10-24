import random
import string

def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

random_code = generate_random_code(10)
print(random_code)