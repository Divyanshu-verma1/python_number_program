
n = int(input('Enter any number to check armstronge number or not : ')) # 153
l = len(str(n))
dup = n
arm = 0
while dup != 0:
    rem = dup % 10
    arm += rem**l
    dup //= 10

print(f'Armstronge number: {n}' if arm == n else f'Not Armstronge number: {n}')
