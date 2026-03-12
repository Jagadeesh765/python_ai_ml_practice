#--------------------
contacts={}
contacts["raj"]="6312144654"
contacts["ramu"]="631217685"
contacts["rajesh"]="6312165789"
print("contact list:")
for name,mobile in contacts.items():
    print(name,"->", mobile)
#-----------------------
contacts={"raj":"6312144654","ramu":"631217685","rajesh":"6312165789"}
name=str(input("enter name:"))
if name in contacts:
    print("phone number",contacts[name])
else:
    print("not found")
    

