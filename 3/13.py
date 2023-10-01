input_str = input()
A = input_str.split()
count = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == A[j]:
            count += 1
print(count)