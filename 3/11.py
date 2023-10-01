input_str = input()
A = input_str.split()
k = int(input())
for i in range(k, len(A) - 1):
    A[i] = A[i + 1]
A.pop()
print(" ".join(A))