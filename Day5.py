# Password Generator

import string
import random

Letters = list(string.ascii_letters)
# Lower_case = list(string.ascii_lowercase)
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password Generator!!🔐")

nr_letters = int(input("How many letters do you want in your password: "))
nr_numbers = int(input("How many numbers do you want in your password: "))
nr_symbols = int(input("How many symbols do you want in your password: "))

# ch_letters = ""
# ch_numbers = ""
# ch_symbols = ""

password = []

for letters in range(0, nr_letters):
    password += random.choice(Letters)

for numbers in range(0, nr_numbers):
    password += random.choice(Numbers)

for symbols in range(0, nr_symbols):
    password += random.choice(Symbols)

random.shuffle(password)

passcode = ""
for char in password:
    passcode += char

print(f"Your password is {passcode}")
