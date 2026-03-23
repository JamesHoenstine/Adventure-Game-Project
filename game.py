"""This is a test client of the code gamefunctions"""



from gamefunctions import(
    print_welcome,
    print_shop_menu,
    purchase_item,
    random_monster
    )


def main():

    name = input("Enter your name:")
    print(print_welcome(name, 40))
    print()
    
    print("Greetings!")
    print("This is the magic shop")
    print_shop_menu("frog",6, "wand", 40)
    print()
    
    print("What do you want to purchase:")
    item = float(input(("Enter Item price: ")))
    money = float(input(("Enter starting money: ")))
    quantity = int(input(("Enter quantity you want: ")))
   
    purchase_item (item, money, quantity)
    
    print()
    
    print("Watch out !")
    monster = random_monster()


if __name__ == "__main__":
    main()