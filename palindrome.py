n = int(input('Enter the number to check palindrome number or not : '))
dup = n
rev = 0
while dup:
    rem = dup % 10
    rev = rev * 10 + rem
    dup //= 10

if rev == n:
    print(f'Given number is palindrome : {n}')
else:
    print('Not palindrome number')