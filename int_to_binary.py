n = int(input('Enter any integer to convert it into binary number : '))
dup = n
binary = 0
pos = 1
while dup :
    rem = dup % 2
    binary += rem * pos
    pos *= 10
    dup //= 2
print(f'Integer {n} to binary is: {binary}')