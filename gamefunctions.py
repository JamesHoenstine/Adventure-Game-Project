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




#Assignment 4 a menu for items with prices.
def print_shop_menu(item1,price1,item2,price2):
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
    price1 = f"${price1:.2f}"
    price2 = f"${price2:.2f}"
    
    print(f"//{'-'*21}\\")
    print(f"| {item1:<12}{price1:>8} |")
    print(f"| {item2:<12}{price2:>8} |")
    print(f"\\{'-'*21}//")
    



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
        my_monster["description"] = "This is an old lost soul who wanders the wastes.He pays attention to no one. He ignores you and lets you go."
        my_monster["health"] = random.randint(1,6)
        my_monster["power"] = random.randint(1,6)
        my_monster["money"] = " 5 sand dollars"
    elif odds == 2:
        my_monster["name"] = "Warewolf"
        my_monster["description"] = "AWOOOOOOOOOO!!! The moon shines bright tonight.Your hear the howl of this beast....run!"
        my_monster["health"] = random.randint(1,6)
        my_monster["power"] = random.randint(1,6)
        my_monster["money"] = "3 silver bullets"
    elif odds == 3:
        my_monster["name"] = "Wurm"
        my_monster["description"] = "Wiggle Wiggle Wiggle...JK its A GAINT WURM DESCENDED FROM DRAGONS.... Hide!"
        my_monster["health"] = random.randint(1,6)
        my_monster["power"] = random.randint(1,6)
        my_monster["money"] = " 1 dirt"
        


    
    print(f"A {my_monster['name']} appears!")
    print(f"{my_monster['description']}")
    print(f"The Health of the {my_monster['name']} is.... {my_monster['health']}")
    print(f"The Power of the {my_monster['name']} is.... {my_monster['power']}")
    print(f"The Wealth of the {my_monster['name']} is.... {my_monster['money']}")

    return my_monster


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
    

if __name__== "__main__":
    test_functions()

