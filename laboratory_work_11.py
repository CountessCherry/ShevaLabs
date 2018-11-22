import random
# 1
a = random.randint(0, 20)
b = input('Enter string ')
c = len(b)
s = ''
c1 = c - a
if c == a:
    print(b)
elif c >= a:
    for i in range(c - 1, c1 - 1, -1):
        s = b[i] + s
else:
    for i in range(a - c):
        s = '.' + b
print('random number = ', a)
print(s)
# 2
n1 = random.randint(1, 8)
n2 = random.randint(1, 8)
s1 = input('Enter first name ')
s2 = input('Enter last name ')
result_string = ''
for i in range(0, n1):
    result_string = result_string + s1[i]
result_string = result_string + ' '
for i in range(0, n2):
    result_string = result_string + s2[i]
print('n1 = ', n1, 'n2 = ', n2)
print(result_string)
# 3
s = input('Enter string ').split()
if len(s) == 2:
    s1 = ''
else:
    s1 = s[1]
print(s1)
# 4
s = input('Enter file name ').split('\\')
c = len(s) - 1
s1 = s[c].split('.')
print(s1[0])
# 5
s = input('Enter file name ')
m = s.rindex('.')
print(s[m+1:])
# 6
s = input('Enter string ')
s1 = ''
for c in s:
    if c.isalpha():
        u = ord(c) + 1
        if u < ord('A') and u > ord('Z') and u < ord('a') and u > ord('z'):
            n = chr(u - 26)
        else:
            n = chr(u)
        s1 = s1 + n
    else:
        s1 = s1 + c
print(s1)
# 7
s = input('Enter string ')
s1 = ''
k = int(input('Enter k '))
for c in s:
    if c.isalpha():
        u = ord(c) + k
        if c.isupper() and u <= ord('Z') or c.islower() and u <= ord('z'):
            n = chr(u)
        else:
            n = chr(u - 26)
        s1 = s1 + n
    else:
        s1 = s1 + c
print(s1)