"""This is a test client of the code gamefunctions"""

import random
import sys

from gamefunctions import (
    print_welcome,
    bazaar_menu,
    purchase_item,
    random_monster,
    snapping_turtle_inn,
    enter_bazaar,
    items,
    inventory,
    equip_item
)




def main():

    name = input("Enter your name:")
    print(f"Greetings {name}! You are in Sneep kingdom. ")
    
    hp = 50
    power = random.randint(1,3)
    gold = 50    

    
    print(f"Current HP:{hp}, Current Gold:{gold}, Current Power:{power}")
    
    print("The Kingdom hums with activity. Where shall your curiosity lead you? ")

    adventuring = True
    
    while adventuring:
        path = input(
            " \nAdventure beyond the kingdoms walls(quest)."
            " \nRest at the Snapping Turtle Inn(rest)."
           " \nAquire wares at the bazaar(shop)."
           "\nCheck inventory(check) and equip items."
            "\nAbandon this adventure(quit).\n"
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
                  
                  for item in inventory:
                      if item['name'] == "phantasmaclasm":
                          print("Phantasmaclasm is a one use spell, it is now gone")
                          inventory.remove(item)
                          power = 2
                          break
                              
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
                
                  
              
        
        
        
        elif path == "rest":
            
            gold, hp = snapping_turtle_inn(gold, hp)
        
        elif path == "shop":
            enter_bazaar(items,gold)
        
        elif path == "check":
            checking = True
            while checking:
                print(f" Your inventory contians: {inventory}")
                print(f" Your current power:{power}")
                choice = input("\nWould you like to equip an item? (equip) or go back (back)").lower().strip()
                
                if choice == "equip":
                    
                    power = equip_item(items,power)
                elif choice == "back":
                    checking = False
                
                else:
                    print("Invalid input")
        
        elif path == "quit":
            print(f"Until next time, {name}!")
            print("The gates of Sneep Kingdom close behind you.")
            sys.exit()
        else:
            print("Invalid input...try again")
            

    
    
    
    
    
    
    

main()
  


if __name__ == "__main__":
    main()