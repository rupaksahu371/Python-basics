a=int(input("enter first person age: "))
b=int(input("enter second person age: "))
c=int(input("enter third person age: "))
if a<b and a<c:
    print("youngest age is a")
if b<a and b<c:
    print("youngest age is b")
if c<a and c<b:
    print("youngest age is c")
