#int string are immutable
x = 100 #refernce x points to int 100,
x = 10 #refernce x points to int 10, int 500 is garbage collected
y = x #new reference in created which points ro 10 independently
x = 30 # y is not updated as it still points to int 10

# id()
c = 10
print(id(c))
d = 20
print(id(d))
d = c
print(id(c) == id(d)) #same id for c and d

c += 2
print(id(c)) # id changes

# for mutable objects like lists
r = [2,4,6]
s = r
s[1] = 10
print(s is r)
print(s, r) #same since lists are mutable and both point to the same list

# value vs identity
p = [1,2,3]
q = [1,2,3]

print(p == q) #value equivalence is true
print(p is q) #Identity equivalence is false

# Argument passing
m = [1,2,3,4]
print(m)
def modify(k):
    k.append(5)
    print('k = ', k)
modify(m)
print('m = ', m)
# m will also be modified, passing to functions is equivalent to k = m;

def replace(g):
    g = [5, 6, 7, 8, 8]
    print(len(g))
    print('g = ', g)

replace(m)
print('m = ', m)
# g and m will be different

#default arguments
def banner(message, border = '-'): # if border is not passed value will be -
    print(message, border)
# arguments with default values come after arguments without
banner('abc')
banner('abc', '*')

import time
def showTime(arg=time.ctime()):
    print(arg)
showTime()
time.sleep(1)
showTime() #time value will be the same, default value is assigned only once, when def is executed for the first time
#No problem when immutable problem when mutable

def add_spam(menu = []):
    menu.append('spam')
    return menu

print(add_spam(['bacon', 'eggs']))
print(add_spam(['pancakes']))
print(add_spam())
print(add_spam()) #empty list is created only once when def executes, keeps appending so same string
print(add_spam(['pancakes']))
print(add_spam())

def add_spam_fix(menu = None): #None is immutable
    if menu is None:
        menu = []
    menu.append('spam')
    return menu
print(add_spam_fix(['bacon', 'eggs']))
print(add_spam_fix(['pancakes']))
print(add_spam_fix())
print(add_spam_fix())
print(add_spam_fix(['pancakes']))
print(add_spam_fix())

#Scope System
#Local - Inside current function
#Enclosing - Inside enclosing functions
#Global - At the top level of the module;
#BuiltIn - In special built in module

count = 0
def show_count():
    print(count)

def set_count(count1):
    count = count1 #shadows the global variable and hence wont change the global count value
show_count()
set_count(5)
show_count()

def set_count_fix(count1):
    global count #now count refers the global value, java equivalent of this.
    count = count1

show_count()
set_count_fix(5)
show_count()



