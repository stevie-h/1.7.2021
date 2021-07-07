#  https://pythonmasterhome.files.wordpress.com/2019/05/hw3105.pdf

'''
1. input received input from the user, it returns String type
2. The returned type can be changed into a number using casting, e.g. int(input...) or float(input...)
3. split separates a string into a list of its characters, with the default by spaces (split()), but can be split by
other characters by specifying it in the command: split('x') would split by the char x.
4. format allows a placeholder for variables inside the string given without needing to separate the sentence
to several strings/argments etc.
5. in checks whether a value exists within a list, string etc.  It can also be used for loops as iteration within
the examined list or range.
6. Conditions are written using the command if followed by the condition and :.
The command elif occurs in case the if condition it connects to has not occurred; else occurs if all preceding
conditions (if, elifs) did not occur.
7. Python coding uses indentation to indicate lines are included in the statement block.

'''

# ex8

num8_1 = int(input('Please enter the first number: '))
num8_2 = int(input('Please enter the second number: '))
if num8_1 > num8_2:
    print(f'{num8_1} is larger than {num8_2}')
else:
    print(f'{num8_2} is larger than {num8_1} or equal to it')

print()

# ex9
num9_1 = int(input('Please enter the first number: '))
num9_2 = int(input('Please enter the second number: '))
num9_3 = int(input('Please enter the third number: '))

if not (num9_1 == num9_2 and num9_1 == num9_3 and num9_2 == num9_3):
    if num9_1 >= num9_2 and num9_1 > num9_3:
        print(f'{num9_1} is the largest of the three')
    elif num9_2 > num9_3:
        print(f'{num9_2} is the largest of the three')
    else:
        print(f'{num9_3} is the largest of the three')
else:
    print('The three numbers are equal!')

print()

# ex10

state10 = input("Please enter an addition phrase, formatted as a + b = c: ")

nums10 = state10.split()

if int(nums10[0]) + int(nums10[2]) == int(nums10[4]):
    print(True)
else:
    print(False)

# ex11

state11 = input("Please enter a math phrase, formatted as a ? b = c: ")

nums11 = state11.split()
op11 = nums11[1]
a = int(nums11[0])
b = int(nums11[2])
c = int(nums11[4])

if op11 in ["+", "-", "*", "/", "^"]:

    if op11 == "+":
        if a + b == c:
            print(True)
        else:
            print(False)
    elif op11 == "-":
        if a - b == c:
            print(True)
        else:
            print(False)
    elif op11 == "*":
        if a * b == c:
            print(True)
        else:
            print(False)
    elif op11 == "/":
        if b != 0:
            if a / b == c:
                print(True)
            else:
                print(False)
        else:
            print('Cannot divide by 0!')
    elif op11 == "^":
        if a ** b == c:
            print(True)
        else:
            print(False)
else:
    print(f'{op11} is not a legal operator in this exercise!')

# obviously for more operators, more conditions are needed. etc.

