#includes the is_divisible function from Section 6.4 of the textbook
def is_divisible(a,b):
    if a%b==0:
        return a%b==0
    else:
        return False

def is_power(a,b):
    if a==b:
        return  a==b
#is_power function includes code for the base case of the second argument being "1"
#is_power function calls is_divisible
    if b==1:
        return False
    elif a%b!=0:
        return False
#is_power function calls itself recursively
    return is_power(a/b,b)

#includes correct output for the five test cases
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))   
print("is_divisible(10, 2) returns: ", is_divisible(10, 2))
print("is_divisible(27, 3) returns: ", is_divisible(27, 3))
print("is_divisible(1, 1) returns: ", is_divisible(1, 1))
print("is_divisible(10, 1) returns: ", is_divisible(10, 1))
print("is_divisible(3, 3) returns: ", is_divisible(3, 3))   
            