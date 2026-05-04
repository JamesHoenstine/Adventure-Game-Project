"""This program implements game functions, adding new functions regulary.

This code is constantly being worked on and added upon itself.
Each assignment will add new functions to this code.
Assignmnet 1 is about pruchasing power.Where you have a specfic
amount of money and want to purchase priced items.
Assignment 2 is a game where you encounter mythical beings!
Assignment 3 is a welcome to our game!
Assignment 4 is a menu for our shop.
These all show game functions and will have return values which 
repersent the data input.

"""


import random

import sys
import pygame
 
import json
from WanderingMonster import WanderingMonster


data = {
        "HP": 20,
        "Power": random.randint(1,3),
        "Gold": 25
        }





def explore_map(p, inventory, items,file_load,state): 
    
    

 pygame.init()

 screen_width = 520
 screen_height = 320
 map_width = 320

 screen = pygame.display.set_mode((screen_width,screen_height))
 text_font = pygame.font.SysFont("Arial", 18)
 text_image = text_font.render("Sneeps Map", True, (255,0,255))
 stats = text_font.render(f"STATS", True, (255,255,255))
 you = text_font.render(f"YOU", True, (255,255,255))
 mapp = text_font.render(f"Town", True, (0,255,0))
 monst = text_font.render(f"Monster", True, (255,0,0))
 cont = text_font.render(f"CONTROLS", True, (170,170,170))
 cont2 = text_font.render(f"Arrow keys to move", True, (170,170,170))

 player_x = 0
 player_y = 0
 
 tile = 32
 grid = 10

 town_x = 7 * tile
 town_y = 8 * tile

 monster_x = 1 * tile
 monster_y = 1 * tile

 run = True

 while run:
     stat = text_font.render(f"HP:  {p['HP']}", True, (255,255,255))
     stat2 = text_font.render(f"Power:  {p['Power']}", True, (255,255,255))
     stat3 = text_font.render(f"Gold:  {p['Gold']}", True, (255,255,255))
     
     screen.fill((0,0,0))
     
     pygame.draw.circle(screen, (0, 255, 0), (town_x + 16, town_y + 16), 16)
     pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, tile, tile))
     
     for monster in state["monsters"]:

         pygame.draw.circle(screen, (255, 0, 0), (monster.x * tile + 16, monster.y * tile + 16), 16)
     
     screen.blit(text_image, (map_width + 10, 10))
     pygame.draw.line(screen, (150,150,150), (map_width + 10, 35), (map_width + 190, 35), 1)
     screen.blit(stats, (map_width + 10, 35))
     screen.blit(stat, (map_width + 10, 60))
     screen.blit(stat2, (map_width + 10, 85))
     screen.blit(stat3, (map_width + 10, 110))
     pygame.draw.line(screen, (150,150,150), (map_width + 10, 140), (map_width + 190, 140), 1)
     screen.blit(you, (map_width + 10, 150))
     pygame.draw.rect(screen, (255, 255, 255), (map_width + 95, 155, 10,10))
     screen.blit(mapp, (map_width + 10, 175))
     pygame.draw.circle(screen, (0, 255, 0), (map_width+ 100, 185), 10)
     screen.blit(monst, (map_width + 10, 200))
     pygame.draw.circle(screen, (255, 0, 0), (map_width+ 100, 210), 10)
     pygame.draw.line(screen, (150,150,150), (map_width + 10, 225), (map_width + 190, 225), 1)
     screen.blit(cont, (map_width + 10, 230))
     screen.blit(cont2, (map_width + 10, 250))

     
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             run = False
              
        
         if event.type == pygame.KEYDOWN:
             
             if event.key == pygame.K_LEFT:
                 if player_x > 0:
                     player_x -= tile
                     for monster in state["monsters"]:
                         monster.x += random.choice([-1, 0 , 1])
                         monster.x = max(0, min(grid - 1, monster.x))
                         monster.y = max(0, min(grid - 1, monster.y))
                 print("You moved left")
             elif event.key == pygame.K_RIGHT:
                 if player_x < (grid - 1) * tile:
                     player_x += tile
                     for monster in state["monsters"]:
                         monster.x -= random.choice([-1, 0 , 1])
                         monster.x = max(0, min(grid - 1, monster.x))
                         monster.y = max(0, min(grid - 1, monster.y))
                 print("You moved right")
             elif event.key == pygame.K_UP:
                 if player_y > 0:
                     player_y -= tile
                     for monster in state["monsters"]:
                         monster.y -= random.choice([-1, 0 , 1])
                         monster.x = max(0, min(grid - 1, monster.x))
                         monster.y = max(0, min(grid - 1, monster.y))
                 print("You moved up")
             elif event.key == pygame.K_DOWN:
                 if player_y < (grid - 1) * tile:
                     player_y += tile
                     for monster in state["monsters"]:
                         monster.y += random.choice([-1, 0 , 1])
                         monster.x = max(0, min(grid - 1, monster.x))
                         monster.y = max(0, min(grid - 1, monster.y))
                 print("You moved down")
 
     for monster in state["monsters"]:
         if monster.x * tile == town_x and monster.y * tile == town_y:
             for monster in state["monsters"]:
                 monster.y += random.choice([-1, 0 , 1])
         if player_x == monster.x * tile and player_y == monster.y * tile:
             print(f"You have encounted a {monster.monster_type}!")
             print(f"The monster has HP: {state['monsters'][0].hp} and power: {state['monsters'][0].power}")
             print(f"Your HP is: {p['HP']} and power: {p['Power']}")
             
             monster.x != town_x and monster.y != town_y
         
             while p['HP'] > 0 and monster.hp > 0:
                a_f = input(f"You encountered a monster, do you attack (attack) or flee (flee)").lower().strip()
                 
                if a_f == "attack":
                    monster.hp -= p['Power']
                    p['HP'] -= monster.power
                    print(f" monster hp : {monster.hp} your hp:{p['HP']}")
                   
                    for item in inventory:
                      if item['name'] == "phantasmaclasm":
                           print("Phantasmaclasm is a one use spell, it is now gone")
                           inventory.remove(item)
                           p['Power'] = 2
                           break
                               
                      print(f"Monster health {monster.hp}, and your health {p['HP']}")
                elif a_f == "flee":
                   print("You have fleed!")
                   player_x += tile
                   pygame.display.update()
                   break
                 
                else:
                     print("Invalid input... try again")
                 
             if p['HP'] <= 0:
                 print("You have fallen to the monster")
                 print("GAME OVER")
                 run = False
                 sys.exit()
             
         
             elif monster.hp <= 0:
                 print("You have beat the monster!")
                 p['Gold'] += monster.money
                 print("Back to Exploration!")
                 state["monsters"].remove(monster)
                 
                 monster_type = [
                    {"name": "Witch", "color": "purple", "hp": 10, "power": 5,"money": 10},
                    {"name": "Bat", "color": "red", "hp": 4, "power": 2, "money": 4},
                    {"name": "Ghost", "color": "grey", "hp": 3, "power": 1, "money": 2},
                    ]
                 remaining = [i for i in monster_type if i["name"] != monster.monster_type]
                 chosen = random.choice(remaining)
                 state["monsters"].append(
                         WanderingMonster(
                             x=random.randint(0,9), 
                             y=random.randint(0,9),
                             monster_type = chosen["name"],
                             color = chosen["color"],
                             hp = chosen["hp"],
                             power = chosen["power"],
                             money = chosen["money"]
                             ))
                                          
                                        
                 
                 
                 player_x += tile
                 pygame.display.update()
                 break
              
     
         if player_x == town_x and player_y == town_y:    
           in_town = True
         
           while in_town:
              print("\nWelcome back to Sneep Kingdom!")
              path_2 = input(
              " \nExplore beyond the walls of Sneep Kingdom!(leave)."
              " \nRest at the Snapping Turtle Inn(rest)."
             " \nAquire wares at the bazaar(shop)."
             "\nCheck inventory(check) and equip items."
             "\nSave and Quit(quit)"
              "Input:"
              ).lower().strip()
             
           
              if path_2 == "rest":
                 
                  p['Gold'], p['HP'] = snapping_turtle_inn(p['Gold'], p['HP'])
             
              elif path_2 == "shop":
                 p['Gold'] = enter_bazaar(items,p['Gold'])
             
              elif path_2 == "check":
                 checking = True
                 while checking:
                     print(f" Your inventory contians: {inventory}")
                     print(f" Your current power:{p['Power']}")
                     choice = input("\nWould you like to equip an item? (equip) or go back (back)").lower().strip()
                     
                     if choice == "equip":
                         
                         p['Power'] = equip_item(items,p['Power'])
                     elif choice == "back":
                         checking = False
              elif path_2 == "leave":
                         print("You adventure back out!")
                         player_x -= tile
                         in_town = False
                     
              elif path_2 == "quit":
                print(f"Until next time!")
                print("The gates of Sneep Kingdom close behind you.")
                save_game(file_load, p)
                sys.exit()            
              else:
                print("Invalid input")
             
            
     
         
             
             
             
             
     
     pygame.display.update()
     
     
     
 pygame.display.quit()




















def load_game(filename):
    '''
    

    Parameters
    ----------
    filename : TYPE
        This will allow you to reload from a json file.

    Returns
    -------
    TYPE
        player, hp , power, gold and inventory.

    '''
        
    if not filename.endswith(".json"):
            filename += ".json"
        
    try:
            
        with open(filename, 'r') as file:
            data = json.load(file)
            player = data['player']
            player['HP'] = player.get('HP') or 20
            player['Gold'] = player.get('Gold') or 25
            player['Power'] = player.get('Power') or 2
            return data
        
    except (FileNotFoundError, json.JSONDecodeError):
        
        print("Generating new file")
        return {
            "player": {
                "name": "Scholar",
                "HP": 20,
                "Power": 2,
                "Gold":25,
                "inventory":[]
                }
            }
                
            



def save_game(filename, player_dictionary):
    """
    

    Parameters
    ----------
    filename : TYPE
        This allows you to save the json file to reload later.
    

    Returns
    -------
    None.

    """
    
    data_save = {"player": player_dictionary}
    
    if not filename.endswith(".json"):
            filename += ".json"
        
    
    with open(filename, 'w') as file:
        json.dump(data_save, file, indent=4)
    print("Progress saved!")





items =[
    {"name": "sword", "type": "weapon", "power": 10, "integrity": 43, "price": 10},
    {"name": "stick", "type": "weapon", "power": 1, "integrity": 1, "price": 1},
    {"name": "phantasmaclasm", "type": "spell", "power": 1000, "life force":"half", "price": 25},
    {"name": "sneepers", "type": "pet", "power": 1, "health": 1000, "price": 5},
    {"name": "beans", "type": "Pinto", "price": 1}
    ]

def attack(weapon):
    weapon["integrity"] -= 10
    if weapon["integrity"] <= 20:
        print(f"Waring: Your{weapon['name']} is about to break!")
    elif weapon["integrity"] <=0:
        print(f"Your {weapon['name']} shattered!")
        




#Assignment 4 a menu for items with prices.
def bazaar_menu(items,gold):
    """

    Parameters
    ----------
    item1 : (str)
        The item that is first.
    price1 : (float)
        The price of the first item.
    item2 : (str)
        The item that is second.
    price2 : (float)
        The price of the second item.

    Returns
    -------
    None.
    
    """
    print(f"//{'-'*25}\\")
    for item in items:
       
        name = item["name"]
        price = item["price"]
        
        print(f"| {name:<14}{price:>9} |")
    
    print(f"\\{'-'*25}//")

inventory = [ 
    {"name": "Water", "type": "drink"},

  
    
    ]

def enter_bazaar(items,gold):
    print("WELCOME TO THE BAZAAR")
    print("Sneepers the pet chirps at you from the shelf.")
    print("You interupt the shop keeper while he is having his lunch.")
    print("Hello traveler! My name is Mordecai, everyhting is for sale... even my lunch.")
    
    
    shopping = True
    while shopping:
        bazaar_menu(items,gold)
    
        purchase = input("What would you like to buy? If nothing type'exit'.")
    
        if purchase == "exit":
            shopping = False
            print("You have left the Bazaar.")
        
        else:
            item_purchased = False
        
            for item in items:
            
                if purchase == item["name"].lower():
                    item_purchased = True
            
                    if gold >= item["price"]:
                        gold -= item["price"]
                        inventory.append(item)
                        print(f"You have aquired {item['name']} for {item['price']} gold.")
                        print(f"You have {gold} gold pieces left")
            
                    else:
                        print(f"Mordecai: 'You are short on coin, traveler.'")
                    break
            if not item_purchased:
                print(f"Mordecai: 'Werid I have never heard of such a thing!'")
   
    return gold
   
    
def equip_item(items,power):
    
    item_found = False
    
    print("Equiping an item which has power stats increases your own power!")
    
        
    equip_items = input("Which item would you like to equip?").lower().strip()
        
    for item in inventory:
        if equip_items == item["name"].lower():
            item_found = True
            
            if "power" in item:
                power += item["power"]
                print(f"You have equipped {item["name"]} and your power is now {power}")
            else:
                print("That item has no power")
            
            
            break
            
    if not item_found:
        print("You dont own that item.")
            
    
    
    return power

    
       
    
   
    






#Assignment 3 a welcome greeting.
def print_welcome(name,width):
    """
    Prints a greeting to the player.

    Parameters
    ----------
    name : (str)
        Name of the player.
    width : (int)
        The width of the discription.

    Returns
    -------
    str
        A greeting.

    """
    return f"{'Hello, ' + name + '!':^{width}}"



    



# Assignmnet 1 Purchasing Power og items

def purchase_item(item_price,starting_money,quantity_to_purchase):
   """
    

    Parameters
    ----------
    item_price : (float)
        Price of the item.
    starting_money : (float)
       The amount of money initially.
    quantity_to_purchase : (int)
        The amount you wish to purchase.

    Returns
    -------
    None.

    """
   if quantity_to_purchase <= starting_money / item_price:
        purchased_quantity = quantity_to_purchase
   else:
        purchased_quantity = starting_money // item_price
    
        
   left_over_money = starting_money - ( purchased_quantity * item_price)

   print(f"Number of items Purchased:{purchased_quantity}")
   print(f"Amount of money remaining:{left_over_money}")
    

    
   
    
#   item_price = int(input("Enter Item Price:"))
#   starting_money = int(input("Enter Starting Money:"))
#   quantity_to_purchase =int(input("Enter Quantity You Wish To Purchase:"))
#   purchase_item(item_price,starting_money,quantity_to_purchase)




# Assignment 2 A monster will appear and you will learn about it.


def random_monster():
    """
    Parameters
    ----------
    None.

    Returns
    -------
    my_monster : (dict)
    - name (str): The monsters name.
    - description (str): Describes the monster.
    - health (int): The health of the monster.
    - power(int): The power of the monster.
    - money(int): The amount of money the monster has.
        

    """
    odds = random.randint(1,3)
    my_monster = {}
    
    if odds == 1:
        my_monster["name"] = "Ghoul"
        my_monster["description"] = "This is an old lost soul who wanders the wastes.He pays attention to you and you fight!."
        my_monster["health"] = random.randint(1,6)
        my_monster["power"] = random.randint(2,8)
        my_monster["money"] = 5
    elif odds == 2:
        my_monster["name"] = "Warewolf"
        my_monster["description"] = "AWOOOOOOOOOO!!! The moon shines bright tonight.Your hear the howl of this beast... and he attacks!"
        my_monster["health"] = random.randint(1,6)
        my_monster["power"] = random.randint(3,6)
        my_monster["money"] = 3
    elif odds == 3:
        my_monster["name"] = "Wurm"
        my_monster["description"] = "Wiggle Wiggle Wiggle...JK its A GAINT WURM DESCENDED FROM DRAGONS....you fight!"
        my_monster["health"] = random.randint(1,6)
        my_monster["power"] = random.randint(3,6)
        my_monster["money"] = 1
        


    
    print(f"A {my_monster['name']} appears!")
    print(f"{my_monster['description']}")
    print(f"The Health of the {my_monster['name']} is:{my_monster['health']}")
    print(f"The Power of the {my_monster['name']} is:{my_monster['power']}")
    print(f"The Wealth of the {my_monster['name']} is:{my_monster['money']}")

    return my_monster

#monster = random_monster()

 
def test_functions():
    """
    Runs a test for the functions created in the code.

    Returns
    -------
    None.

    """
    print("Welcome test:")
    print(print_welcome("James", 30))
    print()
    
    print("Shop Menu Test")
    print_shop_menu("frog", 6, "wand", 50)
    print()
    
    print("Item purchase test")
    purchase_item(10, 100, 5)
    print()
    
    print("Monster test")
    monster = random_monster()
    print("Dictionary returned:",monster)
    
    
    
def snapping_turtle_inn(gold,hp):
    """
    

    Parameters
    ----------
    gold : int
        The amount of money you have.
    hp : int
        Your health.

    Returns
    -------
    gold : int
        The amount of money you have.
    hp : int
        Your health.

    """
    print("Welcome to the Inn, we have many beds available.")
    print("The cost for a night is 5 gold and the sleep is so good it will restore your HP by 10 points!")
    print("Would you like to stay? ")
    
    y_n = input("Yes or No").lower().strip()
   
    if y_n == "yes":
        if gold >= 5:
            hp +=10
            gold -=5
            print("You sleep like a rock")
            print(f"Gold reamining {gold},Health {hp}")
    elif y_n =="no":
        print("Sleep is overrated anyways.")
    else:
        print("Invalid input...try agian")
    return gold, hp   


'''
def char_stats(gold,hp,power):
    hp = hp 


def monster_stats(gold,hp,power):

    print(f"The Health of the {monster['name']} is:{monster['health']}")
    print(f"The Power of the {monster['name']} is:{monster['power']}")
    print(f"The Wealth of the {monster['name']} is:{monster['money']}")
    
    

def monsterquest(hp, power, gold, monster_stats):
    monster = random_monster()
  
    print(f"Your HP:{hp} Your power:{power}")
    print(f"Monster HP:{monster['health']},Monster power:{monster['power']}")
    print("Do you continue to attack? (attack) or flee? (flee)")

    choice = input("")
    return choice
 '''   
  


"""

def monster_quest(hp, power, gold):
    
    monster = random_monster()
    print("A battle occurs!!")
    
    hp -= monster["power"]
    monster['health'] -= power
    
    print(f"The {monster['name']} attacks you and your health goes down to {hp}")
    print(f"You attack back and the {monster['name']}'s health goes down to {monster['health']} ")  
    return hp, gold

    if hp <= 0:
        print("The monster has got the best of you... YIKES!!!")
      
    

    if monster['health'] <= 0:
        gold +=  monster['money']
        print("You have slayed the monster! You have been awared with the wealth that the monster possed.")
        print(f"Your HP:{hp} and power:{power}, The {monster['name']} HP: {monster['health']} and power: {monster['power']}")
        print(f"Total gold:{gold}")
        return hp, gold
        

    else:
        choice = input(
        "\nDo you continue this fight?"
        "\nYes or No"
        "\nInput:"
        ).lower().strip()
    
    if choice == "yes":
        while hp > 0 and   monster['health'] > 0:
            hp -= monster['power']
            monster['health'] -= power
          
            if hp <= 0:
                print("The monster has got the best of you... YIKES!!!")
                break
            
            
            if monster['health'] <= 0:
                gold +=  monster['money']
                print("You have slayed the monster! You have been awared with the wealth that the monster possed.")
                print(f"Your HP:{hp} and power:{power}, The {monster['name']} HP: {monster['health']} and power: {monster['power']}")
                print(f"Total gold:{gold}")
                break
            
            if monster['health'] > hp:
                run = input(
                "\nDo you flee or keep fighting?"
                "\nYes or No"
                "\n Input:"
                ).lower().strip()
                if run == "yes":
                    print("Smart choice!")
                    break
            if hp < 5:
                flee = input(f"You are near death..Flee!?(yes/no):").lower().strip()
                if flee == "yes":
                    print("Great call! You flee back to the kingdom")

"""







if __name__== "__main__":
    test_functions()

