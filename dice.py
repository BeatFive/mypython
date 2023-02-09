import random
result=""
while result!="quit":
    
    #result=input("do you want to roll a number?(enter yes to play and quit to end the program) ")
    result=input("enter to roll dice or quit to exit ")
    dice= random.randint(1,6)
    print(f"dice: {dice}")
    if result.lower()=="quit":
        break
    #if result.lower() =="yes":
     #   print(f"you got number {dice}")

    