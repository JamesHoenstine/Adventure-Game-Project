"""This is a test client of the code gamefunctions"""

import random

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    random_monster,
    snapping_turtle_inn,
)




def main():

    name = input("Enter your name:")
    print(f"Greetings {name}! You are in Sneep kingdom. ")
    
    hp = 5
    power = random.randint(1,3)
    gold = 60    

    
    print(f"Current HP:{hp}, Current Gold:{gold}")
    
    print("The Kingdom hums with activity. Where shall your curiosity lead you? ")

    adventuring = True
    
    while adventuring:
        path = input(
            " \nAdventure beyond the kingdoms walls(quest)."
            " \nRest at the Snapping Turtle Inn(rest)."
            " \nAbandon this adventure(quit).\n"
            "Input:"
            ).lower().strip()
        
        if path == "quest":
            print(f"Your HP is: {hp} and power: {power}")
            monster = random_monster()
            while hp > 0 and monster['health'] > 0:
                a_f = input(f"You encountered a monster, do you attack (attack) or flee (flee)").lower().strip()
                
                if a_f == "attack":
                  monster['health'] -= power
                  hp -= monster['power']
                  print(f"Monster health {monster['health']}, and your health {hp}")
                elif a_f == "flee":
                  print("You have fleed!")
                  break
                
                else:
                    print("Invalid input... try again")
                
            if hp <= 0:
                print("You have fallen to the monster")
                break
            elif monster['health'] <= 0:
                print("You have beat the monster!")
                gold += monster['money']
                break
            
  #        hp, gold =  monster_quest(hp, power, gold)
         
        
        
        
        
        elif path == "rest":
            
            gold, hp = snapping_turtle_inn(gold, hp)
        
        elif path == "quit":
            print(f"Until next time, {name}!")
            print("The gates of Sneep Kingdom close behind you.")
            adventuring = False
        else:
            print("Invalid input...try again")
            
    
    

main()
  


if __name__ == "__main__":
    main()