import random;

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock_paper_scissors = [rock, paper, scissors]
computer_choice = random.randint(0, len(rock_paper_scissors) - 1)

print("Computer chose:")
print(rock_paper_scissors[computer_choice])

print("You chose:")
if 0 <= user_choice < 3:
    print(rock_paper_scissors[user_choice])
else:
    print("Invalid input. You automatically lose.")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You lose!")
