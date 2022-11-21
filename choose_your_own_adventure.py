name = input("Type your name: ")
print("Welcome", name)

answer = input("You are on a dirt road, it has come to an end and you can go left (type left) or right (type right). Where are you going? ").lower()

if answer == "left":
    answer = input("You come to a river, are you going around it (type walk), or through it (type swim): ")

    if answer == "swim":
        print("You swam across the river and were eaten by a crocodile. You lose.")
    elif answer == "walk":
        print("You walked for many miles before reaching a cliff-edge. No way over! You lose. ")
    else: 
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it (type cross), or head back (type back)? ")
    
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (type yes or no) ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("The stranger is offended. You lose")            
        else: 
            print("Not a valid option. You lose.")

    elif answer == "back":
        print("Giving up is boring. You lose.")
    else: 
        print("Not a valid option. You lose.")

else: 
    print("Not a valid option. You lose.")

print("Thank you for playing, ", name)