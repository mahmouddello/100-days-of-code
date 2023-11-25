print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road, Where do you want to go? Type "'"left"'" or "'"right"'" ")
if direction == "left":
    decision = input(
        "You come to a lake, There is an island in the middle of the leak. Type "'"swim"'" or "'"wait"'"to swim across ")
    if decision == "wait":
        pick_door = input(
            "You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
            "Which color do you choose?")
        if pick_door == "yellow":
            print("You Win!")
        elif pick_door == "blue":
            print("Eaten by beasts\nGame Over.")
        elif pick_door == "red":
            print("Burned by fire\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout\nGame Over.")
else:
    print("Fall into a hole\nGame Over.")
