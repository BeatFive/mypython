#Name: ZARA ALWEENA BINTI MOHAMMAD JEFFRY
#Date:2/9/2022
#About: This is a simple calculator that I made for this particular competition,
#       the calculator is to make a basic calculator for people to use.


print("Greetings! Welcome to my calculator")
name=input("What's your name?:\n")
print(f"Hello, {name}! Let's calculate,\n  enter quit anytime to exit the program :\n")
playornot=''
while playornot!="quit":
    number1=input("Enter 1st number: ")
    if number1=='quit':
        break
    if not number1.isdigit():
        print(f'{number1} is not a number')
        continue

    number2=input("Enter 2st number: ")
    if not number1.isdigit():
        print(f'{number1} is not a number')
        continue
    if number2=='quit':
        break

    ops=input("Enter a operation(mul,div,sub,add):\n")
    if ops!= ['mul','div','add','sub']:
        print(f'{ops} is not an operation')
        continue

    if ops=='add':
        print(f'the answer is {ans}')
    if number2=='':
        ans= int(number1)+int(number2)
        if ans=='quit':
            break


    elif ops=='sub':
        ans2 =int(number1)-int(number2)
        print(f'the answer is {ans2}')
        if ans2=='quit':
            break



    elif ops=='mul':
        ans3= int(number1)*int(number2)
        print(f'the answer is {ans3}')
        if ans3=='quit':
            break



    elif ops=='div':
       ans4= int(number1)//int(number2)
       remainder=int(number1)%int(number2)
       if remainder==0:
        print(f'the answer is {ans4}')
       else:
        print(f'the answer is {ans4} with remainder of {remainder}')
       if ans4=='quit':
            break


print("you have ended the program")
      

