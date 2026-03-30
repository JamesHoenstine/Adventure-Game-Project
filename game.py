"""This is a test client of the code gamefunctions"""

import random

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    random_monster,
    snapping_turtle_inn
)




def main():

    name = input("Enter your name:")
    print(f"Greetings {name}! You are in Sneep kingdom. ")
    
    hp = 30
    power = random.randint(1,3)
    gold = 60    

    
    print(f"Current HP:{hp}, Current Gold:{gold}")
    
    print("The Kingdom hums with activity. Where shall your curiosity lead you? ")

    adventuring = True
    
    while adventuring:
        path = input(
            " \n Adventure beyond the kingdoms walls(quest)."
            " \n Rest at the Snapping Turtle Inn(rest)."
            " \n Abandon this adventure(quit).\n"
            "Input:"
            ).lower().strip()
        
        if path == "quest":
            monster = random_monster()
            print("A battle occurs!!")
            hp -= monster["power"]
            monster['health'] -= power
            print(f"The {monster['name']} attacks you and your health goes down to {hp}")
            print(f"You attack back and the {monster['name']}'s health goes down to {monster['health']} ")
            choice = input(
                "\nDo you continue this fight?"
                "\nYes or No"
                "\nInput:"
                ).lower().strip()
            if choice == "yes":
                while hp > 0 and   monster['health'] > 0:
                    hp -= monster['power']
                    monster['health'] -= power
                    gold +=  monster['money']
                    
                    if monster['health'] > hp:
                        run = input(
                        "\nDo you flee or keep fighting?"
                        "\nYes or No"
                        "\n Input:"
                        ).lower().strip()
                    elif monster['health'] < 0:
                        break
                        print("You have slayed the monster! You have been awared with the wealth that the monster possed.")
                        print(f"Your HP:{hp} and power:{power}, The {monster['name']} HP: {monster['health']} and power: {monster['power']}")
                        print(f"Total gold:{gold}")
                    elif hp < 0:
                        break
                        print("The monster has got the best of you... YIKES!!!")
            else:
                print("Retreat!!!!!!")
        
        elif path == "rest":
            
            gold, hp = snapping_turtle_inn(gold, hp)
        
        elif path == "quit":
            print(f"Until next time, {name}!")
            print("The gates of Sneep Kingdom close behind you.")
            adventuring = False
            
    

main()
  


if __name__ == "__main__":
    main()