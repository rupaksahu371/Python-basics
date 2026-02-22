a=str(input("ENTER YOUR GENDER: "))
b=int(input("ENTER YOUR AGE: "))
c=int(input("ENTER YOUR INCOME: "))

if a=="male" or a=="MALE" or a=="Male" and b>21 and c>25000:
    print(" person is insured")
elif a=="female" or a=="Female" or a=="FEMALE" and b>18 and c>40000:
    print("person is insured")
else:
    print("person is not insured")
    
