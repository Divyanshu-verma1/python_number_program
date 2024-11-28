n = int(input('Enter the number to check happy number or not : '))

dup = n
while dup > 9:
    ans = 0
    while dup:
        rem = dup % 10
        ans += rem ** 2
        dup //= 10
    dup = ans
print('Happy number' if dup==1 or dup == 7 else 'Not happy number')