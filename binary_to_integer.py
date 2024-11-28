n = int(input('Enter the binary number : '))
dup = n
integer = 0
pos = 1
while dup:
    rem = dup % 10
    integer += rem * pos
    pos *= 2
    dup //= 10
print(f'Integer of given binary number {n} is: {integer}')
