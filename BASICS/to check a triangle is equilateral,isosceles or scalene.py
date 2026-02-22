a =int(input("ENTER FIRST SIDE OF A TRIANGLE:"))
b =int(input("ENTER SECOND SIDE OF A TRIANGLE:"))
c =int(input("ENTER THIRD SIDE OF A TRIANGLE:"))

if a==b==c:
    print("TRIANBGLE IS EQUILATARAL")
elif a==b!=c or a!=b==c or a==c!=b:
    print("TRIANGLE IS ISOSCELES")
else:
    print("TRAIANGLE IS SCALENE")
