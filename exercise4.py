
# https://pythonmasterhome.files.wordpress.com/2019/06/hw2106-1.pdf

'''
1. A function is a block of code which only runs when it is called from within the programme.
2. In Python it's defined with the word def.
3. Arguments sent to the function will appear after the function name in parentheses. In the method definition
it will be stipulated what arguments it expects to receive when called. Those arguments are used to send
information to the method when called. When defining default values in the method, default parameters must
be aligned to the right (once one parameter is set with a default value, all those to its right must do
the same).
4. when the method is called, e.g. foo(a = 3)
5. Returning a value from the method allows the code calling the method to use information from within
the method. A method returns a value using the command return.
6. Method body cannot be empty, it will generate that error - in order to create an "empty" method, use
the command pass.
7. From the random library (code: import random), with a function defined in it; syntax such as
random.randint(from, to)

'''
import math


# ex8
def getCircumference(radius):
    return radius * 2 * math.pi

# ex9
def add(x = 0, y = 0):
    return x + y

def sub(x = 0, y = 0):
    return x - y

def mul(x = 0, y = 0):
    return x * y

def div(x = 0, y = 0):
    if y != 0:
        return x / y
    else:
        return 'Cannot divide by 0!'

num9_1 = int(input('Please enter the first number: '))
num9_2 = int(input('Please enter the second number: '))
print(f'{num9_1} + {num9_2 } = {add(num9_1, num9_2)}')
print(f'{num9_1} - {num9_2 } = {sub(num9_1, num9_2 )}')
print(f'{num9_1} * {num9_2 } = {mul(num9_1, num9_2 )}')
print(f'{num9_1} / {num9_2 } = {div(num9_1, num9_2 )}')

# ex10
def getInRange(min, max):
    while True:
        num = int(input(f'Please enter number between {min} and {max}: '))
        if max >= num >= min:
            return num
        else:
            print('Number not in range!')

num10 = getInRange(10, 100)
print(f'Number {num10} is in range 10-100!')

# ex11
def min_num(a, b, c):
    if not (a == b and a == c and b == c):
        if a < b and a < c:
            return a
        elif b < c:
            return b
        else:
            return c
    else:
        return 'Numbers are the same!'

num11 = min_num(3, 1, 1)
print('The smallest of these numbers is', num11)

