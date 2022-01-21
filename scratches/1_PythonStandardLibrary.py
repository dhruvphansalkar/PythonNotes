import math
from math import factorial

from math import sqrt as s

print(math.sqrt(81))
print(factorial(5))
print(s(9))


# returns decimal
print( 5 / 3)

# return integer
print(5//3)

# raise to the power
print(2**5)

# No large number error in python
print(factorial(23))

# Scalar data types python
# int, float, none, bool

# int
int(3.5)
int(-3.5)
print(int(float("1234.5")))
# binary int
print(0b11)

# octal int
print(0o70)

# hexa int
print(0x90)

# FLOAT
#constructor
print(float(3))
print(float("nan"))
print(float("inf"))
print(float("-inf"))

print(3.5)
# Speed of light
print(3e10)
#Planks constant
print(1.616e-35 * 1e22)

#None
print(None)
print(None is None)

#Bool (True/False)
print(bool(0))
print(bool(23))
print(bool(-3))

#empty string/collection is false others are true

#Relational Operators
#same as java  ==, !=, >, <

#Contol flow

#if statement
a = 10
b = 20
if a == b:
    print('true')
else:
    print('not true')

if a>b:
    print('g')
elif a<b:
    print('l')
elif a==b:
    print('same')


#While loops

c = 5
while c!=0:
    print(c)
    c-=1

c=5

#same as above as bool(0) == false
while c:
    print(c)
    c -= 1

while True:
    response = input()
    if int(response) % 7 == 0:
        break
    print('cntrl + c to exit')


