name = input("What is your name? ")
print("Hello, " + name + "!")

answer = input(
    "You are driving on a dirt road and it has come to an end and you have to turn left or right. Which way do you turn? ").lower()


if answer == "left":
    awnser2 = input(
        "You come to a river, do you swim across or walk around? (walk/swim) ").lower()
elif answer == "right":
    print("")
else:
    print("That is not a valid direction. You lose")
