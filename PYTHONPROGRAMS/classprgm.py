#--------------------------------------------------------
##STUDENT DETAILS
class STUDENT():
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def display_details(self):
        print("ID:",self.id)
        print("NAME:",self.name)
        print("MARKS:",self.marks)
student1=STUDENT("13","sai ram","100")
student2=STUDENT("14","ram","99")
student3=STUDENT("15","laxmi","98")
student1.display_details()
student2.display_details()
student3.display_details()
#-------------------------------------------------------------------------------------------------------
##PERSON DETAILS
class PERSON():
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display_PROFILE(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("CITY:",self.city)
person1=PERSON("sai ram","23","khammam")
person2=PERSON("ram","19","hyderabad")
person3=PERSON("laxmi","24","sathupally")
person1.display_PROFILE()
person2.display_PROFILE()
person3.display_PROFILE()
#------------------------------------------------------------------------------------


