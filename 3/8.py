input_str = input()
A = input_str.split()
unique_elements = []
count = 0
for element in A:
    if element not in unique_elements:
        unique_elements.append(element)
        count += 1
print(count)