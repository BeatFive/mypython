import random
#number= random.randint(1,3)
number=3
guess= input("guess the number: ")
if int(guess) == number:
    print("You are some lucky kid")
else:
    print("Sorry you missed it")
    print(f"i was thinking of the number {number} and you guess {guess}")