# 1 -- ++++++++++++++++++++++++++++++++++++
# check even or odd number
# problem -- given number (n)
# check if (n) is even or odd number

# Hint: use Modulus(%) for remainder
# if number devided by 2
# if number has 0 remainder
# the number is even

# Naive Approach - Finding the Remainder # O(1) Time and O(1) Space

def isEven(n):
    remainder_num = n % 2
    if remainder_num == 0:
        return True
    else:
        return False 

n = 9

if isEven(n):
    print("number is even")
else:
    print("number is false")



# 2 -- ++++++++++++++++++++++++++++++++++++
# check even or odd number
# Efficient Approach
# Bitwise AND Operator
# O(1) Time and O(1) Space

def isEven(n):
    # taking bitwise and of n with 1 
    if (n & 1) == 0:
        return True
    else:
        return False

n = 19

if isEven(n):
    print("true")
else:
    print("false")



# 3 -- ++++++++++++++++++++++++++++++++++++
# sum of natural numbers
# [Naive Approach] Loop 
# O(n) Time and O(1) Space

def findSum(n):
    sum = 0
    i = 1
    
    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum

n = 7

print(findSum(n))



# 4 -- ++++++++++++++++++++++++++++++++++++
# sum of natural numbers
# [Better Approach] Recursion 
# O(n) and O(n) Space

def findSum(n):
    
    # base condition
    if n == 1:
        return 1
    return n + findSum(n - 1)

n = 25

print(findSum(n))



# 5 -- ++++++++++++++++++++++++++++++++++++
# sum of natural numbers
# [Expected Approach] Formula Based Method
# O(1) Time and O(1) Space

def findSum(n):
    
    # Using mathematical formula to compute
    # sum of first n natural numbers
    return n * (n + 1) // 2
    
n = 5
print(findSum(n))



# 6 -- ++++++++++++++++++++++++++++++++++++
# closes to n and divisible by m
# [Naive Approach] Iterative Checking
# O(m) Time and O(1) Space

def closestNumber(n, m):
    closest = 0
    minDifference = float('inf')

    # Check numbers around n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)

            if (difference < minDifference or
                    (difference == minDifference and
                     abs(i) > abs(closest))):
                closest = i
                minDifference = difference

    return closest

n = 43
m = 8

print(closestNumber(n, m))



# 7 -- ++++++++++++++++++++++++++++++++++++
# closes to n and divisible by m
# [Expected Approach] Finding Quotient
# O(1) Time and O(1) Space

def closestNumber(n, m) :
    q = int(n / m)
    
    # 1st possible closest number
    n1 = m * q
    
    # 2nd possible closest number
    if((n * m) > 0) :
        n2 = (m * (q + 1)) 
    else :
        n2 = (m * (q - 1))
    
    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)) :
        return n1
    
    # else n2 is the required closest number 
    return n2
    
n = 33; 
m = 10
print(closestNumber(n, m))



# 8 -- ++++++++++++++++++++++++++++++++++++
# Express a number as sum of consecutive numbers
# [Naive Approach] Checking All Consecutive Sums
# (n2) Time O(1) Space

def isSumOfConsecutive(n):
    # Try every starting number
    for i in range(1, n):
        sum = 0
        # Generate consecutive sum
        for j in range(i, n):
            sum += j
            # If sum becomes equal to n
            # and at least two numbers are used
            if sum == n and j > i:
                return True
            # If sum exceeds n
            if sum > n:
                break
    return False

# Driver code
n = 12

if isSumOfConsecutive(n):
        print("true")
else:
        print("false")



# 9 -- ++++++++++++++++++++++++++++++++++++
# Express a number as sum of consecutive numbers
# [Expected Approach] Using Power of 2 Property
# O(1) Time O(1) Space

# Python3 program to check whether a number
# can be expressed as sum of consecutive numbers
def isSumOfConsecutive(n):
    
    # 1 cannot be represented
    if n == 1:
        return False

    # Check if n is power of 2
    if (n & (n - 1)) == 0:
        return False

    return True

# Driver code
n = 16

if isSumOfConsecutive(n):
        print("true")
else:
        print("false")