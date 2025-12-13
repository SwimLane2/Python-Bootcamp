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

choose_a_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock_paper_scissors = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print("Computer chose:")
print(rock_paper_scissors[computer_choice])

print("You chose:")
if choose_a_number >= 0 and choose_a_number < 3:
    print(rock_paper_scissors[choose_a_number])
else:
    print("Invalid input. You automatically lose.")

if choose_a_number == 0 and computer_choice == 2:
    print("You win!")
elif choose_a_number == 2 and computer_choice == 1:
    print("You win!")
elif choose_a_number == 1 and computer_choice == 0:
    print("You win!")
else:
    print("You lose!")
