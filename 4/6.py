n=int(input())
a=set()
for i in range(n):
    a|=set(input().split())
print(len(a))