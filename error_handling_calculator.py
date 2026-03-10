while True:
    print("Menu Driven Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    try:
        choice=int(input("enter your choice:"))
    except ValueError:
        print("Invalid Input ! enter correct number ")
        continue
    if choice==5:
        print("calculator exit without any operation")
        break
    if choice not in [1,2,3,4]:
        print("Invalid choice please select correct option to perform calculation")
    x=float(input("enter number1:"))
    y=float(input("enter number2:"))
    if choice==1:
        print("add", x + y)
    elif choice==2:
        print("sub", x + y)
    elif choice==3:
        print("mul", x * y)
    elif choice==4:
        if y!=0:
            print("div", x / y)
        else:
            print("cannot perform division")