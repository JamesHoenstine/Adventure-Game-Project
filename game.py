"""This is a test client of the code gamefunctions"""

import random
import sys
import pygame
from WanderingMonster import WanderingMonster

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
    
     monster_type = [
        {"name": "Witch", "color": "purple", "hp": 10, "power": 5,"money": 10 },
        {"name": "Bat", "color": "red", "hp": 4, "power": 2, "money": 4},
        {"name": "Ghost", "color": "grey", "hp": 3, "power": 1, "money": 2},
        ]
     chosen = random.choice(monster_type)
     state = {
         "monsters":[
             WanderingMonster(x=random.randint(0,9), y=random.randint(0,9),
                              monster_type = chosen["name"],
                              color = chosen["color"],
                              hp = chosen["hp"],
                              power = chosen["power"],
                              money = chosen["money"]
                              )
                              ]}
         

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
             explore_map(p, inventory, items,file_load,state)

            
             
         
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
             pygame.quit()
             sys.exit()
         else:
             print("Invalid input...try again")
             
 






pygame.init()

def main_menu():
    display = pygame.display.set_mode((520,320))
    pygame.display.set_caption("menu")
    
    pink = (255,160,250)
    
    text_font = pygame.font.SysFont("Arial", 50)
    text_image = text_font.render("SNEEPS KINGDOM", True, (0,0,0))
    text_image1 = text_font.render("PLAY", True, (0,0,0))
    text_image2 = text_font.render("QUIT", True, (0,0,0))
    text_image3 = text_font.render("ABOUT", True, (0,0,0))
    
    path = 'Sneep.png'
    back_drop = pygame.image.load(path)
    back_drop = pygame.transform.scale(back_drop, (520,320))
    
    button_play = pygame.Rect(165,75,230,60)
    button_quit = pygame.Rect(165,225,230,60)
    button_about = pygame.Rect(165,150,230,60)



    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                if button_play.collidepoint(event.pos):
                    pygame.quit()
                    main()
                
                elif button_about.collidepoint(event.pos):
                    print("\nThis is a game created for CSCI 150.")
                    print("The goal was to create new functions and definations each week.")
                    print("Each of these being features added to the game and exapnding the world.")
                    print("This game you will adventure in Sneep Kingdom and fight monsters.")
                    print("You will want to buy weapons and equip them in town.")
                    print("Explore Sneep Kingdom and see what it all has to offer.")
                    print("Have a grand adventure!")
                    print()
                
                elif button_quit.collidepoint(event.pos):
                    print("\nYou clicked QUIT!")
                    print("Fare well!")
                    pygame.quit()
                    sys.exit()
                    
                else:
                    print("\nMiss click, try again!")
    
    
        display.blit(back_drop, (0,0))
        pygame.draw.rect(display,pink,(30,10,460,60))
        display.blit(text_image,(30,10))
        
        pygame.draw.rect(display,pink,(165,75,230,60))
        display.blit(text_image1,(220,75))
        
        pygame.draw.rect(display,pink,(165,225,230,60))
        display.blit(text_image2,(220,225))
        
        pygame.draw.rect(display,pink,(165,150,230,60))
        display.blit(text_image3,(185,150))
     
        pygame.display.flip()
        
           
    pygame.quit()

main_menu()
    



  


if __name__ == "__main__":
    main()