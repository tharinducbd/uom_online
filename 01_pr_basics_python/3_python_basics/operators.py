# Basic arithmetic operators: + - * / 
# Other arithmetic operators: modulus %     Exponentiation **   Floor-division //
x, y = 21, 5
print("21 % 5: ", x % y) # remainder
print("21 // 5: ", x // y) # decimal part of the answer is truncated to return an integer

# Assignment operators:
# =  +=  -+  *=  /*  %=  //%  **=  &=  |=  ^=  >>=  <<=

# Comparison operators: return a boolean value
# >  <  ==  !=  <=  >==

# Logical operators: return a boolean value
# and   or  not 
x = True
y = 8
print(x and y >= 3)
print(x and y)
print(x + y)

# Identity operators:       is    is not      (function id() does the same thing)
x = ["a", "b"]
y = ["a", "b"]
print(x is y, id(x), id(y))
z = x
print(x is z, id(x), id(z))

# Membership operators:     in      not in

# Bitwise operators: perform bit-by-bit operations on binary numbers
# &  |  ~  ^  >>  <<
x = 5   # 5 is '101' in binary
y = 7   # 7 is '111' in binary
print(x & y)    # AND
print(x | y)    # OR
print(~x)       # NOT
print(x ^ y)    # XOR
print(x >> 2)   # Bitwise right shift by '2' bits
print(x << 2)   # Bitwise left shift by '2' bits

