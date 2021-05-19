# ENSF 592 Spring 2021
# May 18 Lab 4
# Exercise 1

# Solve each question below using comprehensions or generator expressions.

from itertools import count

# 1. Construct a list consisting of the double of n for each n up to 50 that is divisible by 5. Print the list.

L = [n * 2 for n in range(50) if n % 5 == 0]
print(L)


# Map and filter can't be used on their own to solve this
for val in map(lambda n:n * 2, range(50)):
    print(val, end=' ')

print()

for val in filter(lambda x: x % 5 == 0, range(50)):
    print(val, end=' ')

print()

# Could be combined!
L = []
for val in filter(lambda x: x % 5 == 0, range(50)):
    L.append(val)
for val in map(lambda n:n * 2, L):
    print(val, end=' ')

print()

# OR we can use range to filter out the values first- thanks Amir!
print(*map(lambda x:2*x, range(0,50,5)))



# 2. Construct a generator expression for calculating all the powers of 8. Print the first 8 values of the expression.

G = (8 ** i for i in count())

for i, val in enumerate(G):
    print(val, end=' ')
    if i > 7: break
print()


# 3. Given the list of complex numbers below, construct a dictionary that holds the real component as the key and imaginary component as the value.
# Print the final dictionary.

values = [2 + 4j, 6 + 3j, -5 + 1j, 3 + 5j, 4 + 2j]
D = {val.real:val.imag for val in values}
print(D)


# 4. Construct a generator expression for calculating the first ten triangular numbers, starting with 0. Print the results.
# Hint: 0, 0 + 1 = 1, 0 + 1 + 2 = 3, 0 + 1 + 2 + 3 = 6, etc.

G = (int(n * (n + 1) / 2) for n in range(10))
print(*G)


# 5. Given the list of coordinate tuples below, create a single set that lists each number that appears at least once.

coord = [(0, 1), (1, 2), (3, 4), (4, 1), (5, 2), (3, 6), (-1, 9), (7, 5), (4, 8), (6, 1), (0, 2)]

x, y = zip(*coord)
S1 = {i for i in x}
S2 = S1.union({i for i in y})
print(S2)

### OR

coord = [(0, 1), (1, 2), (3, 4), (4, 1), (5, 2), (3, 6), (-1, 9), (7, 5), (4, 8), (6, 1), (0, 2)]

x, y = zip(*coord)
S1 = set(x)
S2 = S1.union(set(y))
print(S2)

# Other possible solutions exist!
