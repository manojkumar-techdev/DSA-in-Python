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