# start with list of 3 characters
# must able to add charater
# must able to delete a character <-----
# must exit when user enter quit

stars=['kylo ren','darth vader','luke skywalker']
print(stars)
user_answer=""
quitnow=""
while user_answer!='quit':
    user_answer=input("Do you want to add, delete or list the characters? : \n")
    if user_answer=='add':
        what_add=input("what character do you want to add?: \n")
        stars.append(what_add)
        print(stars)
    elif user_answer=='delete':
        what_del=input ("which one do you want to delete?: \n")
        stars.remove(what_del)
        print(stars)
    elif user_answer=='list':
        for name in stars:
            print(name)
    elif user_answer=='quit':
        break
    