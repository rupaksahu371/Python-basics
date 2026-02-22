print("fibbonacci series")

n =int(input("enter term"))
k=2
a=1
b=2

print(a," ",b)
while (k<=n):
    

    c= a+b
    a = b
    b = c
    print(" ",c)
    k=k+1

