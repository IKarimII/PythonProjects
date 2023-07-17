print("LOGO HERE")
bidding = True
bidders = []
while bidding:
    name = input("Who is the contestant?")
    bid = int(input("How much will you bid for the item?"))
    bidders.append({"name":name,"bid":bid})
    other_bidder = input("Does anyone else want to bid? Y/N")
    if other_bidder.upper() == 'Y':
        print("Clear SCREEN")
    else:
        print("Clear SCREEN")
        bidding = False

highest_bid = 0
for people in bidders:
     if people['bid'] > highest_bid:
         highest_bid = people["bid"]
         person = people["name"]

print(f"The Winner of the Secret Auction is {person} with a bid of ${highest_bid} ")

