n = int(input('Enter any number to check disarm number or not : ')) # 135

dup = n
dis = 0
while dup:
    rem = dup % 10
    dis += rem ** len(str(dup))
    dup //= 10

print(f'Disarm number : {n}' if dis == n else f'Not disarm number: {n}')