print("""         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|""")

print("Welcome To Treasure Island\nYour Mission Is To Find Treasure")

choice1=input("You Are A Crossroad Where Do You Go? (L/R)>>").lower()
if choice1=="l":
    choice2=input("You've Come to a lake.There is an island in the middle of the lake. Type 'w' to wait for a boat.  Type 's' to swim across>>")
    if choice2=="w":
        choice3=input("You arrive at the island unharmed.There is a house with 3 doors.One red,one yellow and one blue which color do you choose(y,r,b)? >>")
        if choice3=="y":
            print("You Found The Treasure! You Win!")
        elif choice3=="r":
            print("Burned by fire.Game Over.")
        elif choice3=="b":
            print("Eaten by beasts.Game Over.")
        else:
            print("You Lose!")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")
