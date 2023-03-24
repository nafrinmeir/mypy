rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

man = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors "))
#print(man)

print("man choose")

if man == 0:
    print(rock)
elif man == 1:
    print(paper)
elif man == 2:
    print(scissors)
else:
    print("error")


#rock = 0
#paper = 1
#scissors = 2


import random
pc = [ 0, 1, 2]
#print (a)
for i in range(1):
    pc_choose = random.choice(pc)

print("pc choose")

if pc_choose == 0:
    print(rock)
elif pc_choose == 1:
    print(paper)
elif pc_choose == 2:
    print(scissors)
else:
    print("error")

if man == pc_choose:
    print("it a drow")

elif man == 0 and pc_choose == 1:
    print("PC WIN")
elif man == 0 and pc_choose == 2:
    print("MAN WIN") 

elif man == 1 and pc_choose == 2:
    print("PC WIN")
elif man == 1 and pc_choose == 0:
    print("MAN WIN")

elif man == 2 and pc_choose == 0:
    print("PC WIN")
elif man == 2 and pc_choose == 1:
    print("MAN WIN")

else:
    print("Error")

