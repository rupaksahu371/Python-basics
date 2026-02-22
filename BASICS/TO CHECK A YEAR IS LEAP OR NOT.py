y=int(input("ENTER A YEAR:"))

if y%4==0 or y%400==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
