input_str = input()
A = input_str.split()
k, C = input().split()
k, C = int(k), int(C)
A.append(None)
for i in range(len(A) - 1, k, -1):
    A[i] = A[i - 1]
A[k] = str(C)
print(" ".join(A))