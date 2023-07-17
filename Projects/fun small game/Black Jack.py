import random
import sys
def BlackJack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    print('''88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"          ''')
    play =input("\nWelcome to BlackJack!: Do you want to play? Y/N")



    if play.upper() == 'Y' or play.upper() == 'BLACKJACK':
        draw_first_user = random.choice(cards)
        draw_second_user = random.choice(cards)
        user_hand = [draw_first_user, draw_second_user]
        user_total = draw_first_user + draw_second_user
        print("Your Hand is: ", user_hand)

        if play.upper() == "BLACKJACK":
            user_total = 21
        if user_total == 21:
            print("BLACKJACK!")
            print("You Win!")
            play_again = input("Do You want to play again Y/N?")
            if play_again.upper() == 'Y':
                BlackJack()
            else:
                sys.exit()


        draw_first_bot = random.choice(cards)
        draw_second_bot = random.choice(cards)
        bot_hand = [draw_first_bot, draw_second_bot]
        print(f"Opponent hand is:[{draw_first_bot},?]")
        bot_total = draw_second_bot + draw_first_bot
        if bot_total <= 11:
            print("Your Opponent drew a card")
            extra_card = random.choice(cards)
            bot_hand.append(extra_card)
            bot_total += extra_card

        drawing = True

        while drawing:
            user_total = 0
            if user_total > 21 and 11 in user_hand:
                user_hand.remove(11)
                user_hand.append(1)
            for i in user_hand:
                user_total += i
            if user_total > 21:
                print("BUST!")
                play_again = input("Do you want to play again? Y/N")
                if play_again.upper() == 'Y':
                    BlackJack()
                else:
                    sys.exit()

            drawing = True

            another_card = input("Do you want to draw another card? Y/N")
            if another_card.upper() == 'Y':
                extra_card = random.choice(cards)
                user_hand.append(extra_card)
                print(f"You Drew {extra_card}")

            else:
                drawing = False

        print("The Cards are revealed:")
        print(bot_hand)
        if user_total > bot_total:
            print("YOU WIN")
            play_again = input("Do you want to play again? Y/N")
        elif user_total== bot_total:
            print("It's a Draw")
            play_again = input("Do you want to play again? Y/N")
        else:
            print("You Lose")
            play_again = input("Do you want to play again? Y/N")

        if play_again.upper() == 'Y':
            BlackJack()
        else:
            sys.exit()


BlackJack()
