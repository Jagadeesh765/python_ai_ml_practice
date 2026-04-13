#SIMPLE PATTERN PROGRAMS

#star Triangle 
n=int(input("enter the value:"))
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()



#Inverted star pattern
n=int(input("enter the value:"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#number pattern
n=int(input("enter the value:"))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#same number pattern
n=int(input("enter the value:"))
for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print()
