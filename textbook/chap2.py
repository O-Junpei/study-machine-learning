# Chap2.1
import numpy as np

# 四則演算
print(1 + 2)
print((1 + 2 * 3 - 4) / 5)

# 累乗
print(2 ** 8)

# Chap2.2
x = 1
y = 1 / 3
print(x + y)

Data_1 = 1 / 5
Data_2 = 3 / 5
print(Data_1 + Data_2)

# Chap 2.3
int_type = 1
float_type = 1.5
str_type = "leaning"
bool_type = False
list_type = [1, 2, 3]
taple_type = (1, 2, 3)
ndarray_type = np.array([1, 2, 3])

print(type(100))
print(type(100.1))

x = 100
print(type(x))

x = 100.1
print(type(x))

x = 'learning'
print(type(x))

# Chap 2.4
print('x= ' + str(x))

x = 100
print('weight = {0} kg'.format(x))

x = 1 / 3
y = 1 / 7
z = 1 / 4
print('weight: {0} kg, {1} kg, {2} kg'.format(x, y, z))
print('weight: {0:.2f} kg, {1:.2f} kg, {2:.2f} kg'.format(x, y, z))

# Chap 2.5
x = [1, 1, 2, 3, 5]
print(x)

print(x[0])
print(x[2])

print(type(x))
print(type(x[2]))

s = ['SUN', 1, 'MON', 2]
print(type(s[0]))
print(type(s[1]))

a = [[1, 2, 3], [4, 5, 6]]

print(a)
print(a[0][1])

x = [1, 1, 2, 3, 5]
x[3] = 100
print(x)

print(len(x))

y = range(5, 10)
print(y[0], y[1], y[2], y[3], y[4])
print(y)

z = list(range(5, 10))
print(z)

print(list(range(10)))

# Chap 2.6
a = (1, 2, 3)
print(a)
print(a[1])

print(type(a))

a = (1,)
print(type(a))

# Chap 2.7
x = 11
if x > 10:
    print('x is ')
    print('larger than 10')
else:
    print('x is smaller than 11')

x = 15
if 10 <= x and x <= 20:
    print('x is between 10 and 20')

# Chap 2.8
for i in [1, 2, 3]:
    print(i)

num = [2, 4, 6, 8, 10]
for i in range(len(num)):
    num[i] = num[i] * 2
print(num)

# Chap 2.9
print([1, 2] + [3, 4])

x = np.array([1, 2, 3])
print(x)

y = np.array([4, 5, 6])
print(x + y)

a = np.array([1, 1])
b = a
print('a = ' + str(a))
print('b = ' + str(b))
b[0] = 100
print('a = ' + str(a))
print('b = ' + str(b))

a = np.array([1, 1])
b = a.copy()
print('a = ' + str(a))
print('b = ' + str(b))
b[0] = 100
print('a = ' + str(a))
print('b = ' + str(b))