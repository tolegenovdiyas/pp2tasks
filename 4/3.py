a = set(input().split())
b = set(input().split())
a.intersection_update(b)
l = list(a)
ll = []
for i in range(0, len(l)): ll.append(int(l[i]))
ll.sort()
for i in ll: print(i, end= ' ')