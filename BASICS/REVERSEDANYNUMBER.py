a=int(input("ENTER ANY NUMBER:"))

print(str(a)[::-1])
#Using the string slicing concept, you can get reverse the string. ::-1 corresponds
#to start:stop:step. When you pass -1 as step, the start point goes to the end and stop at the front.