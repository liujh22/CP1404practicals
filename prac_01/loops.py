for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n_stars = int(input("Number of stars: "))
for i in range(1, n_stars + 1, 1):
    print(i*"*")
print()
