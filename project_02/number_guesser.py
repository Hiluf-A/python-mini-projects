import random

top_of_range =  input("Type a number: ")

#Convert numberic strings only
if top_of_range.isdigit():
    top_of_range= int(top_of_range)

    if top_of_range <= 0:
        print("Plsease type a number larger athan 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randrange(0, top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You goit it!")
        break
    elif user_guess > random_number:
        print("Your guess is greater than the number!")
    else:
        print("Your guess is smaller than the number!")

 
print(f"You got it in {guesses} guesses")



