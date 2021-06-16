import sys
from math import log
DIGIT_MAP = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
}

#returns integer
#Best way
def convert(s):
    numbers = []
    try:
        for token in s:
            numbers.append(DIGIT_MAP[token])
        return int(''.join(numbers))
    except (KeyError, TypeError) as e: #will only pick up the specified exception
        print(f'Conversion error Error {e!r}') #use !r with exceptions to get more details
        raise ValueError('The passed value is incorrect')


def convert_1(s):
    numbers = []
    try:
        for token in s:
            numbers.append(DIGIT_MAP[token])
        return int(''.join(numbers))
    except TypeError as e: #will only pick up the specified exception
        print(f'Conversion error Error {e!r}')
    except KeyError as e:
        pass #does nothing, ignores the exception

print(convert('one two three'.split()))

def string_log(s) :
    v = convert(s)
    return log(v)

try:
    print(string_log(['three', 'Liverpool']))
except ValueError as e:
    print('value error Present')