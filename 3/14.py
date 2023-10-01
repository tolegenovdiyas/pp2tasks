input_str = input()
A = input_str.split()
unique_elements = []
for element in A:
    if A.count(element) == 1:
        unique_elements.append(element)
print(" ".join(unique_elements))