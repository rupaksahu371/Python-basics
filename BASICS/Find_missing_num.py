#Gauss code

def find_missing_num(a, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in range(n):
        actual_sum = actual_sum + a[num]
    return expected_sum - actual_sum

# Example usage
a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = 10
missing_num = find_missing_num(a, n)
print("The missing number is:", missing_num)


#xor method

def find_missing_num_xor(a, n):
    x1 = 0
    x2 = 0

    #calculate XOR of all the elements in the array
    for i in range(len(a)):
        x1 = x1 ^ a[i]

    #calculate XOR of all the numbers from 1 to n
    for i in range(1, n + 1):
        x2 = x2 ^ i

    # The missing number is the XOR of x1 and x2
    print("The missing number is:", x1 ^ x2)

# Example usage
a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = 10
find_missing_num_xor(a, n)