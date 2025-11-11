name = input("Type your name: ")
print()
print("============================================")
print(f" === Welcome {name} to this adventure ! ====")
print("============================================")
print()

answer = input( 
    "You are on a dirt road, it has come to an end and you can go left or right ! Which way would you like to go: "
    ).strip().lower()

if answer  == "left":
    answer = input( 
    "You come to a river, you can walk around it or swim accross ? Enter swim or walk:  "
    ).strip().lower()

    if answer == "swim":
        print("You swam accross and were eaten by alligator.")
    elif answer == "walk":
        print("You walked for miles, ran outf water and you lost the game")
    else:
        print("Enter valid task !")
     
elif answer == "right":
    answer  =input("You come to a bridge, it looks wobbly , do you want to crross it or head back (cross/back)? ")
    
    if answer == "back":
        print("You go back to the main road. And lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)")

        if answer == "yes":
            print("YOu talk to the stranger and you won!")
        elif answer == "no":
            print("You lost")
        else:
            print("Enter only yer or no.")
    else:
        print("Enter valid task !")
else:
    print("Enter valid direction !")