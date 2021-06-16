#Comprehensions - Concise syntax for describing lists sets or dictionaries

words = 'hello my name is dhruv'.split()
wordLength = [len(word) for word in words]
print(wordLength)
# [expr(item) for item in iterable]

from math import factorial
f = [len(str(factorial(x))) for x in range(10)]
print(f)

#same can be used for creating sets using {}
f = {len(str(factorial(x))) for x in range(30)}
print(f)

#Similarly for dict {key_expr(item): value_expr(item) for item in iterable}
words = 'hello my name is dhruv'.split()
word_dict = {item : len(item) for item in words}
print(word_dict)

#Invertng a dictionary
capitol_to_country = {'Delhi' : 'India',
                      'London' : 'UK',
                      'Madrid' : 'Spain'}

# iterating over dicts just gives us the keys
country_to_capital = {country : capital for capital, country in capitol_to_country.items()}
from pprint import pprint
pprint(country_to_capital)

#Filtering using comprehensions
def is_long(x) :
    if len(x) > 4 :
        return True
    return False

words = 'hello my name is dhruv'.split()
long_words = [x for x in words if is_long(x)]
print(long_words)




#Iteration Protocols
 # 1. iterable - can be passed to iter() to produce an iterator. Ex list, dict, str
 # 2. iterator - can be passed to next() to get the next value in the sequence.

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) -> will give an exception after reaching end of the list
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

def first(iterable_in_func):
    func_iterator = iter(iterable_in_func)
    try:
        return next(func_iterator)
    except StopIteration as e:
        return 'iterable is empty'

print(first('asasda'))
print(first([]))





#Generator - It is an iterator which describe iterable series with functions, must have yield once, can have return with no arguments

def gen123():
    yield 1
    yield 2
    yield 2

g = gen123()
print(g) #gives a generator function
print(next(g)) #returns first value
print(next(g)) #returns second value
print(next(g)) #returns third value
# print(next(g)) StopIteration exception

for v in gen123(): #generators are iterators and can be used in for loops
    print(v)

h = gen123()
i = gen123()

print(i is h) #will be false since they are independent objects and can be used seperately

print(next(i)) # will return 1
print(next(h)) # will also return 1 since independent from i

def gen246():
    print("about to yield 2")
    yield 2
    print("about to yield 4")
    yield 4
    print("about to yield 6")
    yield 6
    print("about to return")

g = gen246()
print(next(g)) #will execute till the first yield statement which is 2
print(next(g)) #will execute till the next yield statement which is 4
print(next(g)) #will execute till the next yield statement which is 6 which is last
# print(next(g)) #will execute all the code in the generator function then raise exception



# Maintaining state in generator

#demonstrates lazy behaviour of generator
def take(count, func_iterable): # generator distinct is passed as an iterable
    counter = 0
    for item in func_iterable: # distinct will be called now as the values it yields are required
        if counter == count:
            return # ends execution on of generator.
        counter += 1
        yield item

def distinct(func_iterable) : # here the iterable passed is a list
    seen = set()
    for item in func_iterable:
        if item in seen :
           continue #finishes the current iteration and begins the next iteration
        yield item # yields the value to the take function and then take function resumes immdiately after a value is yielded.
        seen.add(item) # next time take calls for value, execution will resume from here.


def run_pipeline() :
    items = [3,6,6,2,1,1]
    for item in take(3, distinct(items)) : # normally inner function will be implemented before outer function but since generators are lazy
                                           # take() will be called before distinct()
        print(item)

run_pipeline()

print('Printing lucas numbers using for')
def lucas() :
    yield 2
    a = 2
    b =1
    for itr in range(10):
        yield b
        a, b = b, a + b

#printing lucas numbers using for loop, will print all values
for x in lucas():
    print(x)

print('Printing lucas numbers using next')
#printing lucas numbers one at a time
l = lucas()
print(next(l))
print(next(l))
print(next(l))
print(next(l))



#Generator Expressions - Combination of comprehensions and generator functions
# (expr(item) for item in iterable)

million_squares = (x*x for x in range(1000000))
print(million_squares) #will print the generator expression object. it is created but not evaluated
print(list(million_squares)[-10:]) #to evaluate it pass it to the list constructor [-10:] will print the last 10 values
print(list(million_squares)) # will be empty since generator is an iterator which has already reached its end, its a one time use object

# each time we run a generator function we create a generator object, to recreate a generator for generator expression re must execute the expression again

def give_gen_expression() :
    return (x*x for x in range(1000000))

print('re initialized the expression using def give_gen_expression()')
million_squares = give_gen_expression();
print(list(million_squares)[-10:]) #will print values
print(list(million_squares)[-10:]) #will not print values

# printing sum using generator expression
print(sum(x*x for x in range(1000000)))

# printing sum using generator comprehension -> memory overload
# print(sum([x*x for x in range(100000000)]))

# printing sum using generator expression with condition
print(sum(x*x for x in range(1000000) if x % 10 == 0))




#Iteration Tools
# itertools module is important
#zip synchronizes two iterables into a tuple
sunday = [1, 8, 15, 22]
monday = [2, 9, 16, 23]

for item in zip(sunday, monday):
    print(item)

#string formatting with tuple unpacking with zip
sunday = [22, 23, 22, 26]
monday = [21, 25, 22, 23]

for temp in zip(sunday, monday):
    print(f'{temp[0]} {temp[1]}')
