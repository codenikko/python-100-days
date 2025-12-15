import random
from hangman_art import stages, logo
from word_list import word_list

print(logo)

chosen_word = random.choice(word_list)  #word of the game

# to print the initial blanks
for i in range(0, len(chosen_word)): 
    print("_", end="", )
print("\n")

# counts the number of lives remaining
lives = 6

war = False

correct_letters = []

game_over = False

while not game_over:


    # gameplay
    guess = input("Guess a letter :").lower()
    
    guess = guess[0]
    
    display ="" #to show the progress
    
    
    if guess in correct_letters:
        war = True
    # decide whether to print blank or letter
    for letter in chosen_word:
        if letter == guess: 
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
# hangman drawing progress
    
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
    else:
        print(stages[lives])
    
    if lives == 0:
        print("***************YOU LOSE***************", "\n***************lives left : ", lives, "***************")
        break
    print(display)
    
    
    
    if war == True:
        print("****************You've already guessed that****************")
    war=False
    print("***************lives left : ", lives,"***************")
    
    
    # NO MORE BLANKS
    if "_" not in display:
        print("***************YOU WIN!!***************")
        game_over = True










    






