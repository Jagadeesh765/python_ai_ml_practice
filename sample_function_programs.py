#------------------
def fact(n):
    fact=1
    for i in range(1,n + 1):
        fact*=i
    return fact
num=int(input("enter a number:"))
print("Factorial Number is:",fact(num))
#-----------------------------
def even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
num=int(input("enter a number:"))
print("the given number is:", even_or_odd(num))
#----------------------------------
def area_of_circle(r):
    return 3.14 * r * r
radius=int(input("enter radius:"))
print("area of circle:",area_of_circle(radius))
#-----------------------------
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
text=str(input("enter the string:"))
print("the given string is:",palindrome(text))
#---------------------------------------
def SI(p,t,r):
    return (p * t * r) / 100
p=float(input("enter the  principal amount:"))
t=float(input("enter the time:"))
r=float(input("enter the rate of interest:"))
print("THE SIMPLE INTEREST IS:",SI(p,t,r))
#---------------------------------------------
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b!=0:
        return a / b
    else:
        return "not possible"
a=int(input("enter number1:"))
b=int(input("enter number2:"))
print("addition:",add(a,b))
print("subtraction:",sub(a,b))
print("multplication:",mul(a,b))
print("division:",div(a,b))
#--------------------------------------


