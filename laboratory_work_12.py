# 1
n = int(input('Enter n '))
a = int(input('Enter A '))
d = int(input('Enter D '))
c = [a + n * d for n in range(0, n)]
print(c)
# 2
n = int(input('Enter n '))
a = int(input('Enter '))
b = int(input())
c = [a, b, a + b]
for u in range(2, n):
    x = c[u] * 2
    list.append(c, x)
print(c)
# 3
k = int(input('Enter k '))
a = input('Enter list ').split()
n = len(a)
d = n // k + 1
app = []
for i in range(k, k * d, k):
    list.append(app, a[i])
print(app)
# 4
a = input('Enter list ').split()
n = len(a)
n1 = n
n2 = (n // 2) * 2
ap1 = []
ap2 = []
for i in range(1, n1, 2):
    list.append(ap1, a[i])
for i in range(0, n2, 2):
    list.append(ap2, a[i])
print(ap1)
print(ap2)
# 5
a = input('Enter list of numbers ').split()
k = int(input('Enter k '))
l = int(input('Enter l '))
m = 0
for i in range(k - 1, l - 1, 1):
    m = m + int(a[i])
print(m)
# 6
a = input('Enter list ').split()
n = len(a)
ap = []
for i in range(1, n, 2):
    list.append(ap, a[i])
print(min(ap))
# 7
a = input('Enter list ').split()
n = len(a)
ap = []
for i in range(0, n, 2):
    list.append(ap, a[i])
print(max(ap))
# 8
a = input().split()
r = float(input())
m = min(a, key=lambda x: abs(float(x) - r))
print(m)

