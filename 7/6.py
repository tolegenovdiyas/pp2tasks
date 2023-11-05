import re
with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
data = re.sub(r'[ ,.]', ':', data)
with open("newRow.txt", "w", encoding="utf-8") as file:
    file.write(data)
