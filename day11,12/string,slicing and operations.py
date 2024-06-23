# sting method
name="chandan"
last_name="maurya"
print("Hello",name,last_name)
code="Hi,this is chandan's code"
print(code)
print("Hi,this is chandan's code")

# multiple lines string
course="""Hi
I am Chandan Maurya
currently i am doing btech
"""
print(course)

# another method
batch='''Hi
I am "Chandan Maurya"
currently i am doing btech'''
print(batch)
print(name[0])

# find length of string 
print(len(batch))

# slicing
#    array[start:end:step]
#    slice[star,end,slice]
print(name[1:3])

# negative / reverse indexing array
print(name[::-1])
print(name[-2:-7:-1])
print(name[::2])

# slice
print(name[slice(0,8,2)])

# print all elements of the character using for loop
print("\nLet's use for loop")
for character in name:
      print(character)

# quiz
nm="harry"
print(nm[-4:-2])