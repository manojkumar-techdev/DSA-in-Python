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