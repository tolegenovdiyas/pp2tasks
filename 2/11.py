a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
dx = abs(a1 - b1)
dy = abs(a2 - b2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')