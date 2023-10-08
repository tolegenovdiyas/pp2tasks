N=int(input())
A=[i for i in range(N)]
s=set(A)
while True:
    n=input()
    if n=="HELP":
        break
    answer=input()
    if answer=="NO":
        s-=set(n.split())
    elif answer=="YES":
        s&=set(n.split())
print(*s)
