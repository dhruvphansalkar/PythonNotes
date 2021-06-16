from math import factorial
from pprint import pprint
import math
#list comprehension
a = ['abc', 'ajskdj', 123, []]
type_comprehension = [type(item) for item in a]
print(type_comprehension)

#set comprehension
len_of_factorial = {len(str(factorial(item))) for item in range(0,20)}
print(len_of_factorial)

#Dict Comprehension
country_to_capital = {
    'uk' : 'london',
    'india' : 'delhi',
    'usa' : 'dc'
}
capital_to_country = {country_to_capital[item] : item for item in country_to_capital}
pprint(capital_to_country)

#example of tuple unpacking in for
country_to_capital_again = {country:capital for capital, country in capital_to_country.items()}
pprint(country_to_capital_again)

#Filtering Comprehensions
def is_vowel(char):
    if char in 'aeiou':
        return True
    else:
        return False

string = 'qwertyuiop'
filter_vowel = [char for char in string if is_vowel(char)]
print(filter_vowel)

# iteration protocol
def get_the_end(interable):
    iterator = iter(interable)
    try:
        return next(iterator)
    except StopIteration:
        print('Value Error')

get_the_end('')

#Generator Function
def generator123():
    print('first yield')
    yield 1
    print('second yield')
    yield 2
    print('third yield')
    yield 3
g = generator123()
for a in g:
    print(a)

