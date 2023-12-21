import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user=input("Please enter your username>>")

user_score=0
computer_score=0

while True:
    user_choice=int(input("Please enter the choice type 0:Rock type 1 Paper type 2 =scissors>>"))
    computer_choice=random.randint(0,2)
    list=[rock,paper,scissors]
    print(f"Computer Choice:\n{list[computer_choice]}")
    print(f"{user} Choice:\n{list[user_choice]}")

    if computer_choice==2 and user_choice==0:
        print(f"{user} Win!")
        user_score+=1
    elif user_choice==2 and computer_choice==0:
        print("Computer Win!")
        computer_score+=1
    elif computer_choice>user_choice:
        print("Computer Win!")
        computer_score+=1
    elif user_choice>computer_choice:
        print(f"{user} Win!")
        user_score+=1
    else:
        print("Draw!")
    print(f"User Score:{user_score}\t Computer Score:{computer_score}")
    if user_score==3:
        print(f"{user} Win The Game!")
        break
    if computer_score==3:
        print(f"Computer Win The Game!")
        break