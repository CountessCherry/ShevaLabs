# 1
s = input('введіть прізвище та ім\'я: ')
print(s[2])
y = len(s)
print(s[y - 2])
print(s[0:5])
print(s[0:y - 2])
print(s[0::2])
print(s[1::2])
print(s[y::-1])
print(s[y::-2])
print(y)
# 2
s = input('введіть символьний рядок: ')
whitespace = 1
for i in range(len(s) - 1):
    if s[i] == ' ' and s[i + 1] != ' ' and s[i + 1] != '.':
        whitespace = whitespace + 1
print('words =', whitespace)
s = s.replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
print(s)

# 3


def revers(s):
    s = s.split()
    s.reverse()
    print(s[0], end=' ')
    print(s[1])


string = input('введіть прізвище та ім\'я ')
revers(string)
# 4
s = input('введіть прізвище та ім\'я ')
y = len(s) // 2
s1 = s[0:y+1]
s2 = s[y:len(s)]
print(s2 + s1)
# 5
s = input('введіть рядок ')
sn = ''
for i in range(1, len(s)):
    if i % 3 != 0:
        sn = sn + s[i]
    else:
        sn = sn + ' '
print(s[0] + sn)
# 6
s = input('введіть прізвище, ім\'я, по батькові ')
s = s.split()
m = s[1]
n = s[2]
print(s[0], '{}.{}.'.format(m[0], n[0]))
# 7
s = input('введіть арифметичний вираз ').split()
dic = {'*': lambda a, b: int(a) * int(b), '/': lambda a, b: int(a) / int(b),
       '+': lambda a, b: int(a) + int(b), '-': lambda a, b: int(a) - int(b)}
if (s[1] == '+' or s[1] == '-') and (s[3] == '*' or s[3] == '/'):
    m = dic[s[1]](s[0], dic[s[3]](s[2], s[4]))
else:
    m = dic[s[3]](dic[s[1]](s[0], s[2]), s[4])
print(m)