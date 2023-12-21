import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''] 
word__list=["software", "hardware","keyboard","monkey","hamburger","backpack","computer","football","python","hangman"]
rand_word=random.choice(word__list)#we choice random word from word_list with random function

list=[]#we create a empty list
for i in range(len(rand_word)):
    list.append("-")#we appened the list up to length rand_word
lives=6#we have six lives in the game
end_of_game=False

while not end_of_game:
    print(f"{' '.join(list)}") #we cahge the list as a string
    guess=input("Please enter your guess>")
    if guess==rand_word:
        print("You win!")
        end_of_game=True
    for position in range(len(rand_word)):
        letter=rand_word[position]
        if letter==guess:
            list[position]=guess
    if guess not in rand_word:
        print(stages[lives])
        lives-=1
        if lives==-1:
            print("Game Over You Lost!")
            print(f"The word was {rand_word}")
            end_of_game=True
    if "-" not in list:
        print("You Win!")
        end_of_game=True
        
    