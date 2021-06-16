#Strin str
#constructor
print(str(100))
print(str(1.123e-10))

#String are sequence type
s = 'abcd'
print(s[1]) #this is string not char
print(type(s[2]))
path = r'C:\Desktop' #raw String no escape

help(str)

#String are unicode with UTF-8
print('\xe5')

#Bytes
a = b'abc'
print(a[0])
print(a.decode('utf8'))

#List
print([1, 2, 4])
print([1, 'abc', 1.3])

a = []
a.append(1)
print(a)

#dict

a = {'a': 1, 'b': 2}
print(a)
a['a'] = 10 # entry updated
print(a)
a['c'] = '12' # new entry created
print(a)

#For Loop

nums = [1,2,4,5,6]
for num in nums:
    print(num)

# get keys when iterating over dicts
for item in a:
    #String accepts multiple arguments
    print(item, a[item])