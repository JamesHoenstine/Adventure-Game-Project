"""This is a test client of the code gamefunctions"""

import random
import sys
import pygame

from gamefunctions import (
    print_welcome,
    bazaar_menu,
    purchase_item,
    random_monster,
    snapping_turtle_inn,
    enter_bazaar,
    items,
    inventory,
    equip_item,
    load_game,
    save_game,
    explore_map
)
 





def main():
    global data, p
    
    print("---- Sneep Kingdom Loader ----")
    print("File name is what your last save was under")
    file_load = input("Enter your file name or type 'new':")
    
    if file_load =="new":
        data= None
    else:
        if not file_load.endswith(".json"):
            file_load += ".json"
    

        data = load_game(file_load)
    
    if data:
        p = data['player']
        name = p.get('name')
        inventory.clear()
        inventory.extend(p.get('inventory',[]))
        
        print(f"Welcome back {name}!")
    else:
        print("Starting a new game")
        
    
        name = input("Enter your name:")
        file_load = name.lower() + ".json"
        print(f"Your file name is {name}")
        
        
        p = {
            "name": name,
            "HP": 20,
            "Power": 2,
            "Gold":25,
            "inventory":[]
            }
        print(f"Greetings {name}! You are in Sneep kingdom. ")
    
   
    
  
    
    print(f"Current HP:{p['HP']}, Current Gold:{p['Gold']}, Current Power:{p['Power']}")
    
    print("The Kingdom hums with activity. Where shall your curiosity lead you? ")

    adventuring = True
    
    while adventuring:
        path = input(
            " \nExplore beyond the walls of Sneep Kingdom!(explore)."
            " \nRest at the Snapping Turtle Inn(rest)."
           " \nAquire wares at the bazaar(shop)."
           "\nCheck inventory(check) and equip items."
            "\nSave and Abandon this adventure(quit).\n"
            "Input:"
            ).lower().strip()
        
        if path == "explore":
            print("This is the world map... many objects lay and wait")
            explore_map(p, inventory, items,file_load)

           
            
        
        elif path == "rest":
            
             p['Gold'], p['HP'] = snapping_turtle_inn(p['Gold'], p['HP'])
        
        elif path == "shop":
           p['Gold'] = enter_bazaar(items,p['Gold'])
        
        elif path == "check":
            checking = True
            while checking:
                print(f" Your inventory contians: {inventory}")
                print(f" Your current power:{p['Power']}")
                choice = input("\nWould you like to equip an item? (equip) or go back (back)").lower().strip()
                
                if choice == "equip":
                    
                    p['Power'] = equip_item(items,p['Power'])
                elif choice == "back":
                    checking = False
                
                else:
                    print("Invalid input")
        
        elif path == "quit":
            p['inventory'] = inventory
            print(f"Until next time, {name}!")
            print("The gates of Sneep Kingdom close behind you.")
            save_game(file_load, p)
            sys.exit()
        else:
            print("Invalid input...try again")
            
 
    
    
    
  
    


  


if __name__ == "__main__":
    main()