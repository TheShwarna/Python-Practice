#Silent Auction
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction = True
bidding_dictionary = {}
while auction==True:
    name = input("What is your name? ")
    bid= int(input("What is your bid? $"))
    bidding_dictionary[name] = bid
    status= input("Do you want to continue? (y/n)")
    if status=="n":
        auction=False
    print("\n"*20)
highest_bid = 0
for i in bidding_dictionary:
    bid_amount = bidding_dictionary[i]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = i
print(f"The highest bid was made by {highest_bidder} for ${highest_bid}")
