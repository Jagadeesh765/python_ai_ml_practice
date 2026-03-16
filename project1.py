contacts={}
while True:
    print("*********CONTACT FORM*********")
    print("1.ADD CONTACTS")
    print("2.VIEW CONTACTS")
    print("3.UPDATE CONTACTS")
    print("4.DELETE CONTACTS")
    print("5.EXIT")
    choice=input("enter your choice:")
    if choice=="1":
        name=input("enter name:")
        phone_number=input("enter mobile number:")
        contacts[name]=phone_number
        print("contact added succesfully.")
    elif choice=="2":
        if len(contacts)==0:
            print("No contacts found.")
        else:
            print("saved contacts are.")
            for name,phone_number in contacts.items():
                print(name,":",phone_number)
    elif choice=="3":
        name=input("enter to update contact:")
        if name in contacts:
            print("a.update contact name:")
            print("b.update phone number:")
            option=input("enter your option:")
            if option=="a":
                new_name=input("enter new name to update:")
                phone_number=contacts[name]
                del contacts[name]
                contacts[new_name]=phone_number
                print("contact name updated successfully.")
            elif option=="b":
                new_phone=input("enter new phone number:")
                contacts[name]=new_phone
                print("phone number updated.")
        else:
            print("contact not found")
    elif choice=="4":
        name=input("enter contact name:")
        if name in contacts:
            del contacts[name]
            print("contact deleted")
        else:
            print("no contact found.")
    elif choice=="5":
        print("existing contact book")
        break
    else:
        print("Invalid ! ")



    
    