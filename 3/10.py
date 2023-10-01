input_str = input()
A = input_str.split()
min_index = A.index(min(A))
max_index = A.index(max(A))
A[min_index], A[max_index] = A[max_index], A[min_index]
print(" ".join(A))