input_str = input()
A = input_str.split()
count = 0
for i in range(1, len(A) - 1):
    if int(A[i]) > int(A[i - 1]) and int(A[i]) > int(A[i + 1]):
        count += 1
print(count)