import random
number= random.randint(1,10)
guess= input("guess the number: ")
if int(guess) == number:
    print("You are some lucky kid")
elif int(guess)<number:
    print("too low")
elif int(guess)>number:
    print("too high")
else:
    print(f"The magic number is{number}")
print(f"the number is {number}")