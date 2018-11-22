import random
# 1


def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


for i in range(5):
    a = random.randint(1, 20)
    factorial(a)
    print('{:>3}'.format(a), '|', factorial(a))
# 2


def fac(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fac(n-2) * n


for i in range(5):
    a = random.randint(1, 20)
    fac(a)
    print('{:>3}'.format(a), '|', fac(a))
# 3


def combinations(n, k):
    if k == n or k == 0:
        return 1
    return combinations(n - 1, k) + combinations(n - 1, k - 1)


for i in range(5):
    a = random.randint(5, 20)
    b = random.randint(1, a)
    combinations(a, b)
    print('{:>3}'.format(a), '{:>3}'.format(b), '|', combinations(a, b))
# 4


def sum(k):
    if 1 <= k <= 9:
        return k
    return sum(k // 10) + (k % 10)


for i in range(5):
    a = random.randint(1, 200)
    sum(a)
    print('{:>5}'.format(a), '|', sum(a))
# 5


def approx_sqv(x, k, n):
    if n == 0:
        return 1
    f = approx_sqv(x, k, n - 1)
    return f - (((f - x) / f**(k - 1)) / k)


x1 = round(random.uniform(0.02, 100), 4)
k1 = random.randint(2, 10)
for i in range(5):
    n1 = random.randint(100, 300)
    print('{:>4}'.format(x1), '{:>2}'.format(k1), '{:>4}'.format(n1), '{:>6}'.format(approx_sqv(x1, k1, n1)))
# 6


def nsd(x, y):
    if y == 0:
        return x
    else:
        return nsd(y, x % y)


for i in range(5):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    c = random.randint(1, 50)
    d = random.randint(1, 50)
    print('{:>3}'.format(a), '{:>3}'.format(b), '|', nsd(a, b))
    print('{:>3}'.format(a),'{:>3}'.format(c), '|', nsd(a, c))
    print('{:>3}'.format(a),'{:>3}'.format(d), '|', nsd(a, d), '\n')
# 7


def maxi(a, m):
    if len(a) == 0:
        return m
    else:
        return maxi(a[1:], max(m, a[0]))


a1 = random.randint(1, 21)
a2 = random.randint(1, 21)
a3 = random.randint(1, 21)
n = random.randint(1, 11)
l1 = random.sample(range(-128, 128), n * a1)
l2 = random.sample(range(-128, 128), n * a2)
l3 = random.sample(range(-128, 128), n * a3)
print('{:>2}'.format('n'), '{:>2}'.format('a'), '{:>4}'.format('max'))
print('{:>2}'.format(n), '{:>2}'.format(a1), '{:>4}'.format(maxi(l1, l1[0])))
print('{:>2}'.format(n), '{:>2}'.format(a2), '{:>4}'.format(maxi(l2, l2[0])))
print('{:>2}'.format(n), '{:>2}'.format(a3), '{:>4}'.format(maxi(l3, l3[0])))

# 8


def fsum(k):
    if (k == 1) or (k == 2):
        return 1
    return fsum(k-2) + fsum(k-1)


for i in range(5):
    a = random.randint(1, 20)
    fsum(a)
    print('{:>3}'.format(a), '|', fsum(a))