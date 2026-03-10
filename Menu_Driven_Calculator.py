print("Menu Driven Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter your choice number: "))
x=float(input("enter number1:"))
y=float(input("enter number2:"))
if choice==1:
    print("add", x + y)
elif choice==2:
    print("sub", x + y)
elif choice==3:
    print("mul", x * y)
elif choice==1:
    print("div", x / y)
else:
    print("Invalid choice")