heights_str = input()
heights = heights_str.split()
x = int(input())
position = 1
for height_str in heights:
    height = int(height_str)
    if height >= x:
        position += 1
    else:
        break
print(position)