b = set()
c = set()
x = set()
for i in range(int(input())):
    a = set()
    for j in range(int(input())):
        a.add(input())
    if i == 0:
        b = a
    else:    
        b = b & a
    c = c | a
print(len(b))
for i in sorted(b):
    print(i)
print(len(c))
for i in sorted(c):
    print(i)