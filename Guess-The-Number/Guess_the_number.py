import random
difficulty = input("Welcome to guess the number!!! Play 'easy' or 'hard'?").lower()
if difficulty == "easy": 
    lives = 10
elif difficulty == "hard": 
    lives = 5

list_of_numbers = []



for i in range(0,101):
    list_of_numbers.append(i)

to_guess = random.choice(list_of_numbers)
# print(to_guess)



while lives>0:

    guess = int(input("Make your guess :  "))
    print("\n"*20)
    print(f"Your guess {guess}")


    if guess>to_guess:
        print("**********Too High!")

    if guess<to_guess:
        print("**********Too Low!")    

    if guess== to_guess:
        print("**********Perfect!!!!!!!!!!")
        print("You win !!!!!!!")

        break
        

    lives = lives - 1
    print(f"Lives remain {lives}")


