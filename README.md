import random
from art import logo

def user_deck():

    game_over = True
    while game_over:

        print(f"Your cards: {user_card}, current score: {sum(user_card)}\n"
              f"Computer's first card: {com_score1}")

        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")

        if continue_game == 'y':
            user_card.append(random.choice(card))

            if sum(user_card) > 21:

                if user_card[-1] == 11:
                    user_card[-1] = 1

                else:
                    game_over = False

        else:
            game_over = False

def com_deck():

    while sum(com_card) < 17:
        com_card.append(random.choice(card))


        if sum(com_card) > 21:

            if com_card[-1] == 11:
                com_card[-1] = 1

            else:
                break

    print(f"Your card: {user_card}, total score: {sum(user_card)}\n"
          f"Computer's card: {com_card}, total score: {sum(com_card)}")

def comparing ():
    user_total = sum(user_card)
    com_total = sum(com_card)

    if user_total > 21:
        print("You're busted!, You Lose...")

    elif com_total > 21:
        print("Computer is busted!, You Win!")

    elif user_total == com_total:
        print("You draw!")

    elif user_total > com_total:
        print("You Win!")

    else:
        print("You Lose...")

# -------------- Process of Black Jack --------------
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
print(logo)
starting_game = input("Do you want to play 'Black Jack'? (y/n): ")
if starting_game == 'y':

    continuing_game = True
    while continuing_game:

        user_score1 = random.choice(card)
        user_score2 = random.choice(card)
        com_score1 = random.choice(card)

        user_card = [user_score1, user_score2]
        com_card = [com_score1]

        user_deck()
        com_deck()
        comparing()
        choice = input("Do you want to play again? (y/n) : ")

        if choice == 'n':
            print("\nGoodbye.")
            continuing_game = False

        else:
            print("\n"*25)

else:
    print("You cannot play this game.")
