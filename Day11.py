# # blackJack
#
# from art import blackjack
# import os
# import random
# 
# print(blackjack)
# deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# def card_chooser(user):
#     for i in range(2):
#         random_cards = random.choice(deck_of_cards)
#         user.append(random_cards)
#     return user
#
#
# def total_sum_of_cards(list_of_cards):
#     total_sum = sum(list_of_cards)
#
#     if total_sum == 21 and len(list_of_cards) == 2:
#         return 0
#     elif 11 in list_of_cards and total_sum > 21:
#         list_of_cards.remove(11)
#         list_of_cards.append(1)
#         total_sum_of_cards(list_of_cards)
#         return total_sum
#     else:
#         return total_sum
#
#
# def blackjack():
#     player_generated_cards = []
#     computer_generated_card = []
#     is_game_over = False
#
#     while not is_game_over:
#         # player cards
#         player_cards = card_chooser(player_generated_cards)
#         sum_of_players_cards = total_sum_of_cards(player_cards)
#         print(f"Player cards: {player_cards} and your total: {sum_of_players_cards}")
#
#         # computer cards
#         computer_cards = card_chooser(computer_generated_card)
#         sum_of_computer_cards = total_sum_of_cards(computer_cards)
#         print(f"Computer cards: {computer_cards[0]}")
#
#         if sum_of_players_cards == 0 or sum_of_computer_cards == 0 or sum_of_players_cards > 21:
#             is_game_over = True
#         else:
#             want_to_pass_or_add = input("Do you want to pass or add:")
#             if want_to_pass_or_add == "add":
#                 player_cards.append(card_chooser(player_generated_cards))
#                 sum_of_players_cards = total_sum_of_cards(player_cards)
#                 if sum_of_players_cards == 0 or sum_of_players_cards > 21:
#                     is_game_over = True
#             elif want_to_pass_or_add == "pass":
#                 #                computer will play
#                 while sum_of_computer_cards != 0 or sum_of_computer_cards < 17:
#                     computer_cards = card_chooser(computer_generated_card)
#                     print(f"Computer cards: {computer_cards}")
#             else:
#                 is_game_over = True
#
#
# # starting game
#
# wantToPlay = input("Do you want to play BlackJack 'y' or 'n':").lower()
#
# if wantToPlay == 'y' or wantToPlay == "yes":
#     # os.system('cls')
#     print("Welcome to BlackJack!")
#     blackjack()
# else:
#     print("Bye!!We would love to play with you.")
#
# # def player_random_cards(count):
# #     random_number = random.choice(deck_of_cards)
# #     count += random_number
# #     random_generated_numbers.append(random_number)
# #
# #
# # def computer_random_cards(count):
# #     computer_random_card = random.choice(deck_of_cards)
# #     computer_card.append(computer_random_card)
# #     count += computer_random_card
