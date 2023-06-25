# Hangman project

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# DAY 7 - HANGMAN(28-may-2023)
list_of_words = ["java", "baboon", "camel", "java", "python", "android", "javascript", "networking", "linux"]
chosen_word = random.choice(list_of_words)
# print(f"Word is {chosen_word}")

len_of_ch_word = len(chosen_word)
display = []
for ch in chosen_word:
    display.append("_")
# print(display)
guessed_letters = []
# guess part
lives = 6
flag = True
while flag:
    guess = input("Guess a letter: ").lower()

    for position in range(len_of_ch_word):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    if guess not in chosen_word:
        if guess in guessed_letters:
            print(f"You have already guessed this letter {guess}")
        else:
            lives = lives - 1
            print(f"You guessed {guess} which is not in the word")
            print(stages[lives])
            if lives == 0:
                print(stages[lives])
                print("You lose!")
                flag = False
        print(f"{' '.join(display)}")

        if "_" not in display:
            flag = False
            print("You Won!")

    guessed_letters.append(guess)
