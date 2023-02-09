stars=['kylo ren','darth vader','luke skywalker']
print(stars)
user_answer=""
quitnow=""
while user_answer!='quit':
    user_answer=input("Enter a character name or enter quit: ")
    #stars.append(user_answer)
    stars.insert(1,user_answer)
    print(stars)
    if user_answer.lower=='quit':
        break
print("you have quit:)")
    
    

