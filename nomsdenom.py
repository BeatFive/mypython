firstnom=input("Enter first nominator:\n")
firstdenom=input("Enter first denominator:\n")
secondnom=input("Enter second nominator:\n")
seconddenom=input("Enter second denominator:\n")


if firstdenom==seconddenom:
    print("can add")
    answer= int(firstnom) + int(secondnom)
    print(f"{firstnom}/{firstdenom}  +  {secondnom}/{seconddenom} = {answer}/{firstdenom}")
else:
    print(f"need to make {firstdenom} equals {seconddenom}")


