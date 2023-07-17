import sys

import logo
import random
from gamedata import data

print(logo.logo)
print("\nYou Will be presented with 2 influencers guess which one has more followers")

print("Who has more followers:\n")
score = 0
def influencer_picker(score,name):
    if score <= 0:
        first_influencer = random.choice(data)
    else:
        first_influencer = name
    print(f"\n{first_influencer['name']} who is a {first_influencer['description']} from {first_influencer['country']} ")
    print(logo.vs)
    second_influencer = random.choice(data)
    print(f"\n{second_influencer['name']} who is a {second_influencer['description']} from {second_influencer['country']} \n")
    if compare(first_influencer, second_influencer, user_input(first_influencer)) == True:
        score+= 1
        print(f"Correct\nCurrent score:{score}")
        influencer_picker(score,first_influencer)
    else:
        print(f"Wrong\nFinal score:{score}")
        again = input("Do You Want to Play Again? Y/N").upper()
        if again == 'Y':
            influencer_picker(0,first_influencer)
        else:
            sys.exit()



def user_input(first_influencer):
    choice = input(f"Do you think {first_influencer['name']} has MORE OR LESS followers, type 'higher' or 'lower' ")
    return choice

def compare(first_influencer,second_influencer,choice):
    if first_influencer['follower_count'] > second_influencer['follower_count']:
        return choice.upper() == 'HIGHER'

    else:
        return choice.upper() == 'LOWER'



influencer_picker(score,'NIGGERS')


