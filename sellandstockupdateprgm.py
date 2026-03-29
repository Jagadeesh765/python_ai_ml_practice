stock=10
def sell_product(stock,quantity):
    if quantity > stock:
        print("stock not aviable")
        return stock
    else:
        stock-=quantity
        print("sell succesfully")
        print("current stock:",stock)
        return stock
stock=sell_product(stock,3)
stock=sell_product(stock,6)
stock=sell_product(stock,5)
