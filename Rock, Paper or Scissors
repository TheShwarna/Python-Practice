#Random module notes
import random
#To generate whole numbers within a range
random_integer=random.randint(1,10)
print(random_integer)

#To generate numbers between 0 and 1 [not including 1]
random_number_0_to_1=random.random()
print(random_number_0_to_1)

#To generate float numbers within a range
random_float= random.uniform(1,100)
print(random_float)

#Heads or Tails
random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==1:
    print("Heads")
else:
    print("Tails")

#Who will pay the bill?
friends=['alice','bruce','charlie','dave','eva']
# #Option 1
print(friends[random.randint(0,4)])
# #Option 2
print(random.choice(friends))

#Rock, Paper or Scissors game
move1= int(input("Welcome to Rock, Paper or Scissors game!\nPlease enter 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if move1==0:
    print(rock)
elif move1==1:
    print(paper)
elif move1==2:
    print(scissors)
else:
    print("Wrong Input, Try Again!")

list=[rock,paper,scissors]
move2 = random.choice(list)
if move1==0:
    if move2==rock:
        print("Computer chose:"+move2+"\nGame Tied!")
    elif move2==paper:
        print("Computer chose:"+move2+"\nYou Lose!")
    else:
        print("Computer chose:"+move2+"\nYou Win!")
elif move1==1:
    if move2==paper:
        print("Computer chose:"+move2+"\nGame Tied!")
    elif move2==rock:
        print("Computer chose:"+move2+"\nYou Win!")
    else:
        print("Computer chose:"+move2+"\nYou Lose!")
elif move1==2:
    if move2==scissors:
        print("Computer chose:"+move2+"\nGame Tied!")
    elif move2==paper:
        print("Computer chose:"+move2+"\nYou Win!")
    else:
        print("Computer chose:"+move2+"\nYou Lose!")
else:
    print("Wrong Input, Try Again!")
