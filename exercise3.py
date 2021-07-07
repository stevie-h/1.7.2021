
# https://pythonmasterhome.files.wordpress.com/2019/06/hw1406.pdf


'''
1. The range function in a for loop will iterate the block of code a specific number of times.
2. By default the range function "jumps" by 1, but in syntax any jump can be defined in the third element
it can be sent:
range(1, 20, 2)  --> jump is 2, from 1 to 19
range(1, 20, -1)  --> jump is -1 (simple reverse)
3. using syntax such as list(range(20)) would create a list of the numbers in the range given
4. while and do-while loops enable executing a block of code as long as (or until) a condition is true.
5. while runs the code if the condition stipulated is true, possibly never;
do-while will run an iteration and then check the condition.
6. with the condition for the while being True + break in the code if needed.
7. break stops the loop, while continue just jumps to the next iteration, thus allowing some code to be
skipped without stopping the entire process.

'''

'''
# ex8
for i in range(200, 1, -1):
    print(i)

# ex9
for i in range(1, 100):
    if i % 7 == 0:
        print(i)

# ex10
sum10 = 0;
while True:
    x = int(input('Please enter a positive number (to exit enter negative number): '))
    if x < 0:
        break
    sum10 += x

print(f'Sum of positive numbers entered is {sum10}')

# ex11

num11 = int(input('Please enter a number: '))
fact = 1
for i in range(1, num11 + 1):
    fact *= i

print(f'{num11}! = {fact}')

'''

# ex12

lucky_nums12 = (2, 13, 24, 35, 46)
lucky_rem = list(lucky_nums12)
attempts = 0
while len(lucky_rem) != 0:
    guess = int(input(f'#{attempts+1} guess for a number from 2 to 49: '))
    attempts += 1
    if guess not in range(2, 50):
        print(f'Not in range!')
        continue
    if guess in lucky_rem:
        lucky_rem.remove(guess)
        print(f'Success! {len(lucky_rem)} numbers left to guess!')
    else:
        print(f'No luck there! {len(lucky_rem)} numbers left to guess!')

print('The lucky numbers were:', lucky_nums12)
print(f'It took you {attempts} attempts to guess all the numbers.')
