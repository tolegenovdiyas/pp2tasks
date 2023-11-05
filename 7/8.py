import re
with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
split_data = re.split(r'(?=[A-Z])', data)
edited_data = '\n'.join(split_data)
with open("newRow.txt", "w", encoding="utf-8") as file:
    file.write(edited_data)
