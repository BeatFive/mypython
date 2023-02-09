print("Welcome to my calculator user!")
name=input("What's your name user?:\n")
playornot=(f"Hello, {name}! Do you want to play this calculator?\nType yes to play and quit to exit the program :\n")
while playornot!="quit":
    (f"Hello, {name}! Do you want to play this calculator?\nType yes to play and quit to exit the program :\n")
    number1=input("Enter 1st number: ")
    number2=input("Enter 2st number: ")
    ops=input("Enter a operation(mul,div,sub,add:\n")
    if ops=='add':
        ans= int(number1)+int(number2)
        print(f'the answer is {ans}')
    elif ops=='sub':
        ans2 =int(number1)-int(number2)
        print(f'the answer is {ans2}')
    elif ops=='mul':
        ans3= int(number1)*int(number2)
        print(f'the answer is {ans3}')
    elif ops=='div':
       ans4= int(number1)/int(number2)
       print(f'the answer is {ans4}')
    elif playornot.loer()=='quit':
        break

