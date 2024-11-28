n = int(input('Enter number to check stronge number or not : ')) # 145

dup = n
stronge = 0
while dup:
    rem  = dup % 10
    fact = 1
    while rem:
        fact *= rem
        rem -= 1
    stronge += fact
    dup //= 10

print(f'Stronge number {n}' if n == stronge else 'Not stronge number')