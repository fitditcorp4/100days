rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#print(rock)
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

import random
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
rock_paper_scissors = ['rock', 'paper', 'scissors']
computer_choice = random.randint(0, 2)

if user_input == 0:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print('The game is a draw')
    elif computer_choice == 1:
        print(paper)
        print('You lost')
    else:
        print (scissors)
        print('You won')


elif user_input == 1:
    print(paper)
    if computer_choice == 1:
        print(paper)
        print('The game is a draw')
    elif computer_choice == 0:
        print(rock)
        print('You won')
    else:
        print(scissors)
        print('You lost')

else:
    print(scissors)
    if computer_choice == 1:
        print(paper)
        print("You won")
    elif computer_choice == 0:
        print(rock)
        print('You lost')
    else:
        print(scissors)
        print('The game is a draw')

#if computer_choice == 0:
    #print(rock)
#elif computer_choice == 1:
    #print(paper)
#else:
    #print(scissors)
