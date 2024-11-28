n = int(input('Enter the number to check tech number : '))

dup = n
if len(str(dup)) % 2 == 0:
    f = dup % (10 ** (len(str(dup)) // 2))
    s = dup // (10 ** (len(str(dup)) // 2))
    ans = f + s
    ans = ans ** 2
    print(f'Tech number : {n}' if ans == n else 'Not a tech number')

else:
    print('Not a tech number')