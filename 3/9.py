input_str = input()
A = input_str.split()
for i in range(0, len(A) - 1, 2):
    A[i], A[i + 1] = A[i + 1], A[i]
print(" ".join(A))