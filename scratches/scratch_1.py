import math
a = 'My name is {0} and I am {1} years old'
print(a)
a = a.format('Dhruv', 24)
print(a)
str
tuple = (1,2,4,5)
str_b = f'kjsdnskand {tuple[0]}'
print(str_b)
q, _, r = (str_b.partition(' '))
print(q)
print(r)
print(" ".join([q, r, 'q']))
for i in range(10,2):
    print()
for i, v in enumerate(tuple):
    print(f'index = {i} value = {v}')
    a, b, c, d = tuple
    print(f'{a},{b},{c},{d}')

