print("fibbonacci series")
# Take user input for the number of terms
n = int(input("Enter the number of terms: "))

# Initialize first two Fibonacci numbers
a, b = 0, 1

# Check for valid input
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(a)
else:
    print("Fibonacci series:")
    count = 0
    while count < n:
        print(a, end=" ")
        # Update values for next iteration
        next_term = a + b
        a = b
        b = next_term
        count += 1   