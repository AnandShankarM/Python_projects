#Mini project 9

import random

# ---------- DEAL CARD ----------
def deck_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# ---------- CALCULATE SCORE ----------
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# ---------- COMPARE RESULTS ----------
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Computer has Blackjack. You lose"
    elif u_score == 0:
        return "User has Blackjack. You win"
    elif u_score > 21:
        return "User busts. Computer wins"
    elif c_score > 21:
        return "Computer busts. User wins"
    elif u_score > c_score:
        return "User wins"
    else:
        return "Computer wins"

# ---------- MAIN GAME ----------
def play_game():
    users = []
    computer = []

    for _ in range(2):
        users.append(deck_cards())
        computer.append(deck_cards())

    is_game_over = False

    while not is_game_over:
        u_score = calculate_score(users)
        c_score = calculate_score(computer)

        print("Users:", users, "Score:", u_score)
        print("Computer:", [computer[0]])

        if u_score == 0 or c_score == 0 or u_score > 21:
            is_game_over = True
        else:
            choice = input("Do you want to draw a card: 'y' or 'n': ").lower()
            if choice == 'y':
                users.append(deck_cards())
            else:
                is_game_over = True

    while c_score != 0 and c_score < 17:
        computer.append(deck_cards())
        c_score = calculate_score(computer)

    print("\nFinal Result")
    print("Users:", users, "Score:", u_score)
    print("Computer:", computer, "Score:", c_score)
    print(compare(u_score, c_score))


play_game()
