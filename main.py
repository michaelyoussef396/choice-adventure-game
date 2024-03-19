name = input("What is your name? ")
print("Hello, " + name + "!")

answer = input(
    "You are driving on a dirt road and it has come to an end and you have to turn left or right. Which way do you turn? ").lower()


if answer == "left":
    awnser2 = input(
        "You come to a river, do you swim across or walk around? (walk/swim) ").lower()
    if awnser2 == "walk":
        print("you walked a while and ran out of food. You starved to death.")
    elif awnser2 == "swim":
        print("You swam across and got eaten by a hungry fish.")
    else:
        print("Invalid response. You Lose")

elif answer == "right":
    awnser2 = input(
        "You come to a bridge, do you cross it or turn around? (cross/turn) ").lower()
    if awnser2 == "cross":
        print("You crossed the bridge and found a treasure chest full of gold.")
    elif awnser2 == "turn":
        print("You turned around and got hit by a car.")
    else:
        print("Invalid response. You Lose")

else:
    print("That is not a valid direction. You lose")
