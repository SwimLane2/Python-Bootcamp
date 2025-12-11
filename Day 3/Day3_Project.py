print('''

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      
      Welcome to Treasure Island.
Your mission is to find the treasure.
            
      ''')

first_choice = input('You\'re at a cross road.' 
                     'Where do you want to go? Type "left" or "right"\n').lower()
if first_choice == "left":
    second_choice = input("You\'ve come to a lake. There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors." 
                             "One red, one yellow and one blue.\n Which colour do you choose?\n").lower()
        if third_choice == "yellow":
            print("You found the treasure! You Win!")
        elif third_choice == "red":
            print("Burned by fire. Game Over.")
        elif third_choice == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("You\'ve chosen a door that doesn\'t exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")    
else:
    print("Fall into a hole. Game Over.")
