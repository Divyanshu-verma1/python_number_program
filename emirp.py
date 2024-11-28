n = int(input('Enter the number to find emirp or not : '))
dup = n
rev = 0
while dup:
    rem = dup % 10
    rev = rev * 10 + rem
    dup //= 10

if rev != n:
    for den in range(2,rev//2 + 1):
        if rev % den == 0:
            print('Not emirp number')
            break
    else:
        for den in range(2,n//2 + 1):
            if n % den == 0:
                print('Not emirp number')
                break
        else:
            print(f'Emirp number : {n}')

else:
    print('Not Emirp number')