n, m = ([int(s) for s in input().split()])
N = set()
M = set()
for i in range(n):
    N.add(int(input()))
for j in range(m):
    M.add(int(input()))
print(len(N & M))
print(*sorted(N & M))
print(len(N - M))
print(*sorted(N - M))
print(len(M - N))
print(*sorted(M - N))