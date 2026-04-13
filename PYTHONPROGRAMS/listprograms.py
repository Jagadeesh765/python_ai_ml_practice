#-----------------------
text=" welcome to the world "
text=text.strip()
words=text.split()
correct_text=" ".join(words)
correct_text=text.capitalize()
print(correct_text)
#------------------------------
####string manipulations:
str="python is easy to learn"
print(str.upper())
texts="AMMA"
print(texts.lower())
print(len(texts))
word=str.replace("python","java")
print(word)
res=str.split()
print(res)