
# https://pythonmasterhome.files.wordpress.com/2019/06/hw0706.pdf


'''
1. A loop is useful when the same command or code is run more than once consequentially.
2. for x in (object):
    <code>
'''


# ex3
nums3 = [1, 5, 7, 8, 100]
for i in range(int(len(nums3) / 2)):
    print(f'#{i} : {nums3[i]}')

# ex4
words4 = ['hello', 'python', 'pen', 'world of coding']
for word in words4:
    print(word.upper())

# ex5
for word in words4:
    if len(word) < 4:
        break
    else:
        print(word.upper())

print()

# ex6
str6 = "John Smith"

print(str6[-5:])

print(str6[:int(len(str6)/3)])

print(str6.count('a'))

print('b' in str6)

sepName = str6.split()
print(sepName)

sepName.reverse()
print(sepName)

last_name = sepName[0].upper()
print(last_name)

first_name = sepName[1]
mid = int(len(first_name)/2)
if len(first_name) % 2 == 0:
    name_edit = first_name[:mid - 1] + first_name[mid + 1:]
else:
    name_edit = first_name[:mid] + first_name[mid + 1:]
print(name_edit)

final_name = name_edit + ' ' + last_name
print(final_name)

# ex7

str7 = 'Hello world!'

print(str7[:str7.find('o')])
print(str7[str7.rfind('o') + 1:])

# ex8

print(str7.replace('o', ''))

# ex9

nums9 = [8, 1000, -3, 2, 5]

print()

print(max(nums9))

print(min(nums9))

print(sum(nums9) / len(nums9))

print()

del nums9[int(len(nums9) / 2)]
print(nums9)
nums9.sort()
print(nums9)

print()

i = 1
while i <= 5:
    print(nums9)
    i += 1

print()

del nums9[0]
print(nums9)

print()

nums9 = [8, 1000, -3, 2, 5]
nums9_undermean = []
for n in nums9:
    if n < sum(nums9) / len(nums9):
        nums9_undermean.append(n)
print(nums9_undermean)

print()

# ex10
nums10 = [1, 5, 7, 8, 100]
max_n = nums10[0]

for n in nums10:
    if n > max_n:
        max_n = n
print(max_n)
