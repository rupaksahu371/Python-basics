F =int(input("ENTER DAY OF RETURN: "))
A =(F-15)*5
B =(F-15)*100
if F<=15:
    print("NO FINE")
elif F>15 and F<=50:
    print("FINE=",A)
else:
    print("FINE=",B)

