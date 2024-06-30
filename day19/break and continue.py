print("Break staement")
a=input("enter table you want to print")
x=int(a)
for i in range(1,12):
    if (i==11):
        break
    print(f"{x} x",i, " = ", x*i)  
print("break executed")     

print("\ncontinue statement")
# a=input("enter table you want to print")
# x=int(a)
for i in range(1,12):
    if (i==10):
        print("iteration skipped")
        continue
    print(f"{x} x",i, " = ", x*i)  
