#using exception handling concept to create,write and read the file,if file exist it print if not exception checks correctly
try:
    with open("f1.txt","w") as file:
        file.write("hi iam jagadeesh")
    with open("f1.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("No File found")
except PermissionError:
    print("permission need to open a file")
finally:
    print("DONE!")


#create a student marks program with validation like non numeric,negative marks,marks <100 only and display grade if valid
try:
    marks=input("enter marks:")
    if not marks.isdigit():
        print("marks should be in numbers.")
    marks=int(marks)
    if marks<0 or marks>100:
        print("the marks should lies between 0 to 100 only.")
    if marks>=90:
        grade="A"
    elif marks>=75:
        grade="B"
    elif marks>=65:
        grade="C"
    elif marks>=55:
        grade="D"
    else:
        grade="fail"
    print("GRADE",grade)
except ValueError as e:
    print("error occured")
finally:
    print("Done!")    