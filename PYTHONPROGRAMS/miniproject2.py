#create student class
class student:
    def __init__(self,name,rollno,grade,age):
        self.name=name
        self.rollno=rollno
        self.grade=grade
        self.age=age
    def display_info(self):
        print(f"NAME:{self.name},ROLLNO:{self.rollno},GRADE:{self.grade},AGE:{self.age}")
#manage all students details
class manage_student_details:
    def __init__(self):
        self.studentlist=[]
    ##create
    def add_student(self,name,rollno,grade,age):
        std=student(name,rollno,grade,age)
        self.studentlist.append(std)
        print("student added!")
    #read/view
    def view_student(self):
        if not  self.studentlist:
            print("no details found")
        else:
            for std in self.studentlist:
                std.display_info()
    #update
    def update_student(self,rollno):
        for std in self.studentlist:
            if std.rollno==rollno:
                std.name=input("NEW NAME:")
                std.age=input("NEW AGE:")
                std.grade=input("NEW GRADE:")
                print("updated sucess!")
                return
        print("not found")
    #delete
    def delete_student(self,rollno):
        for std in self.studentlist:
            if std.rollno==rollno:
                self.studentlist.remove(std)
                print("deleted sucess!")
                return
        print("not found")
system=manage_student_details()
while True:
    print("\n 1.ADD 2.VIEW 3.UPDATE 4.DELETE 5.EXIT")
    choice=int(input("enter ur choice:"))
    if choice==1:
        name=input("NAME:")
        rollno=input("ROLLNO:")
        grade=input("GRADE:")
        age=input("AGE:")
        system.add_student(name,rollno,grade,age)
    elif choice==2:
        system.view_student()
    elif choice==3:
        rollno=input("rollno to update.")
        system.update_student(rollno)
    elif choice==4:
        rollno=input("rollno to delete.")
        system.delete_student(rollno)
    elif choice==5:
        break
    else:
        print("INVALID!")

    
