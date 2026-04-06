import json
inventory={}
def add_product():
    name=input("enter product name:")
    price=float(input("enter price:"))
    quant=float(input("enter quantity:"))
    inventory[name]={"price":price,"quantity":quant}
    print("product added successfully")
def update_product():
    name=input("enter name to update:")
    if name in inventory:
        price=float(input("enter new price:"))
        quant=float(input("enter new quantity:"))
        inventory[name]["price"]=price
        inventory[name]["quantity"]=quant
        print("product updated")
    else:
        print("not found")
def sell_product():
    name=input("enter product name:")
    if name in inventory:
        quant=int(input("enter quantity to sell:"))
        if inventory[name]["quantity"]>=quant:
            inventory[name]["quantity"]-=quant
            print("the product selled")
            print("remaing quantity:",inventory[name]["quantity"])
        else:
            print("out of stock")
    else:
        print("not found")
def view_stock():
    if not inventory:
        print("no products")
    else:
        for name,details in inventory.items():
            print(f"{name} -> Price:{details['price']},Quantity:{details['quantity']}")
def save_to_file():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
    print("data saved.")
def load_from_file():
    global inventory
    try:
        with open("inventory.json","r") as file:
            inventory=json.load(file)
        print("data loaded")
    except:
        print("no file founded.")
def menu():
    while True:
        print("1.ADD \n 2.UPDATE \n 3.SELL \n 4.VIEW \n 5.SAVE \n 6.LOAD \n .EXIT")
        choice=int(input("enter ur choice:"))
        if choice==1:
            add_product()
        elif choice==2:
            update_product()
        elif choice==3:
            sell_product()
        elif choice==4:
            view_stock()
        elif choice==5:
            save_to_file()
        elif choice==6:
            load_from_file()
        elif choice==7:
            print("exit")
            break
        else:
            print("invalid choice.")
menu()
    
    


    