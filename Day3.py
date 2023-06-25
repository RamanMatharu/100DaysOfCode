# Love Calculator

print("Welcome to ❤ Calculator!!😉")

ur_name = input("Enter your name:").lower()
partner_name = input("Enter your partner's name:").lower()

combined_name = ur_name + partner_name
true = 0
love = 0
for letter in "true":
    true += combined_name.count(letter)
true = str(true)

for letter in "love":
    love += combined_name.count(letter)
love = str(love)

true_love = int(true+love)

if true_love < 10 or true_love > 80:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")