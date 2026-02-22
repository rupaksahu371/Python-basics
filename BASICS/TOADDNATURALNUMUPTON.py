# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,

n=int(input("ENTER N="))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)