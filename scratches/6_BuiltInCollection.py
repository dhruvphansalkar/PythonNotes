#Tuple - Immutable
t = ('Anc', 6, 7)
print(t)
print(t[0])

for item in t:
    print(item)

print(t + (3,4)) #only appends the collections does not change the value

print(t * 3) #repeats the values of the tuple thrice

a= ((1,1),(2,2),(3,3)) #nested tuple
print(a)
print(a[0][1])

a = (1,) # Single element tuple requires a trailing comma seperator, otherwise its read as int
print(a)
a = () #empty tuple
print(a)

a = 1,2,3,4,5 #alternate tuple declaration
print(a)

def min_max(items):
    return min(items), max(items) #return multiple values as a tuple

print(min_max((1,2,4,56,0)))

#tuple unpacking
lower, upper = min_max((1,2,3,4,6)) #assign values in the same sequence as tuple
print(lower, upper)

(a,(b,c)) = (1,(2,3)) #assignment same as indexing
print(a, b, c)

a = 'jelly'
b = 'bean'
print(a, b)
a,b = b,a #swapping values using tuple unpacking
print(a, b)

tuple([1,3,5,7]) #tuple constructor to convert list to tuple
b = tuple("123") #tuple constructor to convert string to tuple
print(b)

print(5 in (1,3,5,6)) #containment operator
print(5 not in (1,3,5,6)) #containment operator

# STRINGS
# Concatenation done same way as java '+' but inefficient.
colors = ';'.join(['Red', 'Green', 'Blue'])
print(colors)
colors = colors.split(';')
print(colors)

#Best way to concatenate is to use empty string
print(''.join(['high', 'way', 'man']))

# partition separator
print('highwayman'.partition('way')) #returns a tuple

origin,_, destination = 'Mumbai->Delhi'.partition('->') #underscore is to be ignored
print(origin,destination)

#format - replacements fields are placeholders with values taken up by function parameters
a = "My name is {0}".format('Dhruv')
print(a)

a = '{} is {} years old'.format('Dhruv', 25) #follow sequence if no numbers
print(a)

a = '{name} is {age} years old'.format(name = 'Dhruv',age = 25) #specify by function parameters
print(a)

a = '{name[0]} is {name[1]} years old'.format(name = ('Dhruv', 10)) #specify by function parameters
print(a)

import math
a = 'pi is {m.pi} and e is {m.e}'.format(m = math)
print(a)

#F string - allow interpolation using minimum syntax
a = f'one plus onr = {1 + 1}'
print(a)

import math as m
a = f'pi is {m.pi:.3f} and e is {m.e:.3f}' # :.3f is the float point specifier
print(a)

from datetime import datetime as d
a = f'the time right now is {d.now().isoformat()}'
print(a)


#Range
a = range(5)
print(a)

#For loop using range
for i in a:
    print(i)

a = (5, 10) # both start and end index present in the range
print(list(range(5,10))) #Converting range to list

a = (0, 10, 2) # range using step arguments
print(list(range(0, 10, 2)))

# Dont use range when object like list is given use Enumerate
t = [6,54,56,12,33]
for p in enumerate(t):
    print(p)

for i, v in enumerate(t):
    print(f'i = {i}, v = {v}')






#List details
# can access list from end using negetive index;
t = [6,54,56,12,33]
print(t[-1]) #last element
print(t[-2]) # second last element

# Negative indexing is 1 based not 0 based

t = [6,54,56,12,33]
print(t[0:3]) #slicing to get element 0, 1 , 2
print(t[1:-1]) #all elements apart from 1st and last
print(t[2:]) # slicing till the end
print(t[:4]) # slicing from the beginning
print(t[:]) #get all elements used to copy a list

p = t[:] #full copy of a list
p[0] = 0
print(p) #different since the objects are different;
print(t)

#other shallow copying methods
p = t.copy()
p = list(t)

a = [[1,2], [3,4]]
b = a[:]
print(a is b) # false since a shallow copy
print (a == b) # true since value is same
print(a[0] is b[0]) #true since shallow copy does not copy the inside values

# Multiplication operator is used to initialize list when size is known
# Do not use when the list contains mutable objects
a = [[1,0]]
a = a * 3
print(a)
a[0].append(1)
print(a)

# Some list operations
w = 'Hello there'.split()
i = w.index('there')
print(i)
print(w.count('Hello'))
print('Hello' in w)

# delete from list
w = 'My name is Dhruv'.split()
print(w)
del w[3] # remove by index
print(w)
w.remove('is')
print(w) # remove by value

#insert in list
w = 'My name is '.split()
print(w)
w.insert(3,'Dhruv') #insert at index
print(w)

w += ['Phansalkar'] #insert at the end
print(w)

del w[-1]
w.extend(['Phansalkar']) #insert at end
print(w)

#List Manipulation, reverse && sort
a = [1,2,3,4]
print(a)
a.reverse()
print(a)
a.sort()
print(a)

#sort can take parameters reverse and key
a.sort(reverse=True) # decending order
print(a)

a = 'Hello My name is dhruv Phansalkar'.split()
print(a)
a.sort(key=len) #Sorting based on callable object
print(a)


# my own callable function
def assign_priority(word: str):
    if word[0].isupper():
        return -1
    else:
        return 1

a = 'Hello My name is dhruv Phansalkar'.split()
print(a)
a.sort(key=assign_priority)
print(a)

#sorted and reversed give a new list
a = [3,1,5,4]
b = sorted(a)
c = reversed(a) # gives a list_reverseiterator
print(a)
print(b)
print(list(c)) #need to pass to constructor for actual list




#Dictionary
#key object is always immutable

a = [('alice', 10), ('bob', 20), ('Peter', 30)]
d= dict(a) #convert list of tuples to dict
print(d)

# copys are shallow
d= dict(gold=123, copper=324)
f = dict(d)
print(f)
g=dict(silver='sil', lead='pb', copper='cu')
f.update(g) #add values from another dictionary and replace values if keys clash
print(f)

#dictionaries are iterable
for key in f:
    print(f'{key} -> {f[key]}') #Not ordered

#iterate over values
for val in f.values():
    print(val)

#Iterate over items
for item in f.items():
    print(f'{item[0]} -> {item[1]}') # can also use tuple unpacking

# use in or not in
print('silver' in f)

#del to delete item by key
del f['silver']
print(f)

from pprint import pprint as pp
pp(f)

#Set - unordered collection of unique elements
# Elements should be immutable

p = {6, 4,2, 1}
print(p)
print(type(p))

a = set()
#{} creates empty dict, hence set needs a constructor

#Sets are iterable but the order is arbitary

# in and not in operators work

# adding to set
a = {1,3,4}
a.add(6)
print(a)

a.add(1) # no change since already present
print(a)

#add multiple elements using update
a.update([1,6,7,89,7])
print(a)

# removing elemnts
a.remove(1) #key error if 1 not present
a.discard(1) # no error if not present
print(a)

#copying elements(shallow)

b = a.copy() #using copy method
b = set(a) #usinf set constructor

# set algebra operation
blue_eyes = {'A', 'B', 'C', 'D'}
blond_hair = {'A', 'C', 'E', 'F'}
smell_hcn = {'B', 'D'}

print(blue_eyes.union(blond_hair)) #commutative
print(blond_hair.intersection(blue_eyes)) #commutative
print(blue_eyes.difference(blond_hair)) #non commutative
print(blue_eyes.symmetric_difference(blond_hair)) #Commutative
print(smell_hcn.issubset(blue_eyes))

#Protocol


