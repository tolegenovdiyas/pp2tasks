import re
with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

matches = re.findall('a[b]*', data)
edited_data = '\n'.join(matches)

with open("newRow.txt", "w", encoding="utf-8") as file:
    file.write(edited_data)
