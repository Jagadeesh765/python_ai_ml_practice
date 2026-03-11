#-----------------------
marks=[100,60,70,55,40,95,75,85,55]
marks.sort()
print(marks)
if 55 in marks:
    print("yes")
else:
    print("no")
search_element=int(input("enter number:"))
if search_element in marks:
    print("found")
else:
    print("not found")
#--------------------------------------
marks=[50,70,85,66,67,93,42,55,53,70]
total_marks=sum(marks)
avg_marks=total_marks / len(marks)
if avg_marks>90:
    grade="A"
elif avg_marks>75:
    grade="B"
elif avg_marks>55:
    grade="C"
else:
    grade="fail"
print(len(marks))
print("total marks:",total_marks)
print("average marks:",avg_marks)
print("grade marks:",grade)
