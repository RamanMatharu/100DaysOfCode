import random
print("Who is gonna pay the bill today!")

list = input("Enter the names of friends:").split()

num_of_frnds = len(list)

# print(num_of_frnds)
random_choose = random.randint(0, num_of_frnds-1)
print(f"{list[random_choose]} is going to buy the meal today!")