print("Chandan's calculotor")
a=int(input("enter value of a "))
b=int(input("enter value of b "))
g="""-----main manu-----
1.addition
2.subtraction
3.multiplication
4.division
5.modulus"""
print(g)
v=int(input("Enter Opertion no. "))
match v:
    case 1:
        print("addition of",a,"and",b,"is",a+b)
    case 2:
        print("subtraction of",a,"and",b,"is",a-b)
    case 3:
        print("multiplication of",a,"and",b,"is",a*b)
    case 4:
        print("division of",a,"and",b,"is",a/b)
    case 5:
        print("modulus of",a,"and",b,"is",a%b)
    case _:
        print("sorry input is invalid")  
        
h=int(input("enter 1 if you want to use another operation otherwise 0 "))
if(h==1):
        print(g)
        v=int(input("Enter Opertion no. "))
        match v:
           case 1:
                 print("addition of",a,"and",b,"is",a+b)
           case 2:
                 print("subtraction of",a,"and",b,"is",a-b)
           case 3:
                 print("multiplication of",a,"and",b,"is",a*b)
           case 4:
                 print("division of",a,"and",b,"is",a/b)
           case 5:
                 print("modulus of",a,"and",b,"is",a%b)
           case _:
                 print("sorry input is invalid")
else:
        print("Thanks for using our calculator")    