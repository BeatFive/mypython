import random
quote01='''
adffd
'''

quote2="""
 _   _         _  _          _   __ _
| | | |  ___  | || |  ___   | | / /(_)  _     _
| |_| | / _ \ | || | / _ \  | |/ /  _ _| |_ _| |_  _  _
|  _  |/ /_\ \| || |/ / \ \ |   /  | |_   _|_   _|| |/ /
| | | |\ ,___/| || |\ \_/ / | |\ \ | | | |_  | |_ | / /
|_| |_| \___/ |_||_| \___/  |_| \_\|_| \___| \___||  /
                       _           _              / /
                      / \_______ /|_\             \/
                     /          /_/ \__
                    /             \_/ /
                  _|_              |/|_
                  _|_  O    _    O  _|_
                  _|_      (_)      _|_
                   \                 /
                    _\_____________/_
                   /  \/  (___)  \/  \\
                   \__(  o     o  )__/
"""
quote03= '''
  .--.            .--.
 ( (`\\."--``--".//`) )
  '-.   __   __    .-'
   /   /__\ /__\   \\
  |    \ 0/ \ 0/    |
  \     `/   \`     /
   `-.  /-"""-\  .-`
     /  '.___.'  \\
     \     I     /
      `;--'`'--;`
jgs     '.___.'
'''


#mylist=["can you repeat the question?", "Hmm, I think that is a stupid question","I just had a brain fart, I dont know"]
mylist=[quote01,quote2,quote03]
user=input("Ask me anything?:)")
myindex= random.randint(0,2)
print(mylist[myindex])