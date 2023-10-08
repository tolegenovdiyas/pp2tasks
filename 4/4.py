l = [int(i) for i in input().split()]
s = set()
for i in l:
    if i not in s:
        print('NO')
        s.add(i)
    else:
        print('YES')