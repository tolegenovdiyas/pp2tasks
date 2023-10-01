N, K = input().split()
N, K = int(N), int(K)
kegels = ['I'] * N
for _ in range(K):
    left, right = input().split()
    left, right = int(left), int(right)
    for i in range(left - 1, right):
        kegels[i] = '.'
print("".join(kegels))