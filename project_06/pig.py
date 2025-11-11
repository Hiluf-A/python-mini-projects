import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    s = input("Enter the number of players (2–4): ").strip()
    try:
        players = int(s)
    except ValueError:
        print("Invalid input! Enter a whole number.")
        continue

    if 2 <= players <= 4:
        break
    else:
        print("Enter a number between 2 and 4.")

max_score = 50
player_score = [0 for _ in range(players)]
current_score = 0

while max(player_score) < max_score:
    
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!") 
        print("Your total sore",player_score[player_idx]) 
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y) ")
            if should_roll.strip().lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f"Your score is: {current_score}")

        player_score[player_idx] = current_score
        print(f"Your total score is: {player_score[player_idx]}")