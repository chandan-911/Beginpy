# a=10
# print(a)
# b=str(a)
# print(b)
# c=10
# print(b+c)

print("1.")
a="Chandan"
print(len(a))
# strings are immutable means these can't be changed
# write in uppercase
print("2.")
print(a.upper()) #make not copy of string a
print(a.lower()) 
print("3.")
b="!!Chandan Maurya!!!!!!!!"
print(b.rstrip("!")) #buit don't strip before string
print("4.")
print(a.replace("Chandan","Chandan Maurya"))
#split
print("5.")
c="This is Chandan's Thinkpad"
print(c.split(" "))

#capitalize like blog
print("6.")
d="introduction to pYthon PrOgramming"
print(d.capitalize()) #capitalize the first word and remaining will be lower case

# center method
print("7.")
e="introduction to pYthon PrOgramming"
print(len(e))
print(e.center(50))
print(len(e.center(50))) 

#count
print("8.")
s="chandan went to chandan's house and meet with chandan"
print(s.count("chandan"))

#endwith tells end with some data
print("9.")
b="!!Chandan Maurya!!!!!!!!"
print(b.endswith("!!!"))
print(b.endswith("an",4,6))

#find 
print("10.")
b="!!Chandan Maurya!!!!!!!!"
print(b.find("Ma"))
print(b.find("Madfr")) #if not match returns -1

#isalnum
print("11.")
t="WelcomeToTheConsole"
print(t.isalnum())

t="welcome3"
print(t.isalpha())

t="welcome"
print(t.isalpha())

t="welcome"
print(t.islower())

t="welcome"
print(t.isprintable())
t="welcome\n"
print(t.isprintable())

t="        "
print(t.isspace())

t="welcome"#tells capital is true otherwise false
print(t.istitle())

r="welcome to my code of python"
print(r.startswith("welcome"))

r="welcome to my code of python"
print(r.swapcase())

r="welcome to my code of python"
print(r.title())






