products={}
def add_product(name,price,quantity):
    if name in products:
        print("Already exist")
        return
    products[name]={"price":price,"quantity":quantity}
    print(f"{name} added.")
def update_product(name,price=None,quantity=None):
    if name not in products:
        print("product not found")
        return
    if price is not None:
        products[name]["price"]=price
    if quantity is not None:
        products[name]["quantity"]=quantity
def display_products():
    for name,details in products.items():
        print(f"{name} -> Price:{details['price']},Quantity:{details['quantity']}")
add_product("milk",45,50)
add_product("milk",35,35)
update_product("milk",price=49)
update_product("milk",quantity=19)
display_products()

