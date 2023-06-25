from art import logo

print(logo)
print("Welcome to the secret auction program.")
bid_log = {}

letBidding = True
highest_bid = 0
highest_bidder = ""
while letBidding:
    name_of_bidder = input("What is your name?: ")
    bid_value = int(input("What is your bid?: $"))
    bid_log[name_of_bidder] = bid_value

    letBidding = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if letBidding == "no":
        for bidder in bid_log:
            if highest_bid < bid_log[bidder]:
                highest_bid = bid_log[bidder]
                highest_bidder = bidder
        print(f"The Winner is {highest_bidder} with a bid of ${highest_bid}")
        letBidding = False

# print(bid_log)
