n=int(input())
h=int(n % (60 * 24) // 60)
m=(n%60)
print(h, m)
